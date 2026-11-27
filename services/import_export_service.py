import json
from pathlib import Path
from tkinter import filedialog, TclError
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from models.film_model import Film
from storage.store_service import (
    append_and_store_films,
    get_all_persisted_films,
    get_films_from_json,
)

#import films from a .json file
#Leonid Kaup
def import_file():
    try:
        print("Please select a .json File you want to import.")

        import_file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All files", "*.json")],
        )
        if not import_file_path:
            print("Import cancelled.")
            return

        imported_films = get_films_from_json(Path(import_file_path))

        if not isinstance(imported_films, list):
            raise TypeError

        for film in imported_films:
            Film.from_dict(film)

        if imported_films:
            for film in imported_films:
                append_and_store_films(film)

        print("Import was successfull!")

    except json.JSONDecodeError as error:
        print(
            "Import failed: The selected file does not contain valid JSON "
            f"(line {error.lineno}, column {error.colno})."
        )
    except KeyError as error:
        print(f"Import failed: A required film field is missing: {error}.")
    except TypeError as error:
        print(f"Import failed: The data has an unexpected type: {error}.")
    except PermissionError as error:
        print(f"Import failed: You do not have permission to read or write the file: {error}.")
    except ValueError as error:
        print(f"Import failed: A film contains invalid data: {error}.")

#Leonid Kaup
def export_films():
    persisted_films = get_all_persisted_films()
    if not persisted_films:
        print("No Films available to export")
        return

    export_option = input("Please type 1 for JSON and 2 for PDF\n").strip()
    if export_option not in ("1", "2"):
        print("Please selecte a valid option")
        export_films()
        return

    if export_option == "1":
        try:
            print("Please select where the JSON export should be saved.", end="\n")
            export_file_location = filedialog.asksaveasfilename(
                title="Save film export",
                defaultextension=".json",
                filetypes=[("JSON files", "*.json")],
            )
            if not export_file_location:
                print("Export cancelled.")
                return

            with open(export_file_location, "w", encoding="utf-8") as file:
                json.dump(persisted_films, file, indent=2, ensure_ascii=False)
                file.write("\n")
            print("Export was Successful!")
        except PermissionError:
            print("Export failed: You do not have permission to save the file.")
        except OSError as error:
            print(f"Export failed: The file could not be saved: {error}")
        except (TypeError, ValueError) as error:
            print(f"Export failed: The film data could not be written as JSON: {error}")
        except TclError as error:
            print(f"Export failed: The save dialog could not be opened: {error}")

    elif export_option == "2":
        try:
            print("Please select where the PDF export should be saved.")
            export_file_location = filedialog.asksaveasfilename(
                title="Save film export",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
            )
            if not export_file_location:
                print("Export cancelled.")
                return

            styles = getSampleStyleSheet()
            content = [Paragraph("Meine Filmsammlung", styles["Title"]), Spacer(1, 16)]

            for film in persisted_films:
                actors = ", ".join(film["actors"])
                rating = film["rating"] if film["rating"] is not None else "Keine Bewertung"

                content.extend([
                    Paragraph(f"<b>{escape(str(film['title']))}</b>", styles["Heading2"]),
                    Paragraph(f"Genre: {escape(str(film['genre']))}", styles["BodyText"]),
                    Paragraph(f"Erscheinungsdatum: {escape(str(film['dateOfRelease']))}", styles["BodyText"]),
                    Paragraph(f"Bewertung: {escape(str(rating))}", styles["BodyText"]),
                    Paragraph(f"Gesehen am: {escape(str(film['watchdate']))}", styles["BodyText"]),
                    Paragraph(f"Schauspieler: {escape(actors)}", styles["BodyText"]),
                    Paragraph(f"Beschreibung: {escape(str(film['description']))}", styles["BodyText"]),
                    Spacer(1, 12),
                ])

            pdf = SimpleDocTemplate(export_file_location, pagesize=A4)
            pdf.build(content)
            print("Export was Successful!")
        except Exception as error:
            print("Export was not Successful!", error)
