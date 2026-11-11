# All services/functions related to films

from datetime import datetime
from utils.helper import validate_date
import json

from models.film_model import Film
from storage.store_service import append_and_store_films
from storage.store_service import get_films_from_json, get_all_persisted_films
from pathlib import Path

from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from tkinter import filedialog


# writes a new film to the JSON file
# Léon ALbert
def new_film():
    film = Film(
        title=input("Titel: "),
        date_of_release=_read_date("Date of release (dd.mm.yyyy): "),
        genre=input("Genre: "),
        rating=_read_rating(),
        description=input("Description: "),
        actors=[
            actor.strip()
            for actor in input("Actors (comma-separated): ").split(",")
            if actor.strip()
        ],
        watch_date=_read_date("Watch date (dd.mm.yyyy): "),
    )
    append_and_store_films(film.to_dict())
    print("Film saved.")

# Léon ALbert
def _read_date(prompt):
    while True:
        date_text = input(prompt)

        if validate_date(date_text):
            return date_text
        else:
            print("Please enter a valid date in dd.mm.yyyy format.")

# Léon ALbert
def _read_rating():
    while True:
        rating_text = input("Rating (1-10): ").strip()
        try:
            rating = int(rating_text)
        except ValueError:
            print("Please enter a whole number from 1 to 10.")
            continue

        if not 1 <= rating <= 10:
            print("Rating must be between 1 and 10.")
            continue
        return rating

#import films from a .json file
#Leonid Kaup
def import_file():
    try:
        print("Please select a .json File you want to import.")

        #filepicker
        import_file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All files", "*.json")]
        )
        # call file import
        imported_films = get_films_from_json(Path(import_file_path))

        if not isinstance(imported_films, list):
            raise TypeError
        for film in imported_films:
            #validation - if it fails it throws an Error that gets catched 
            Film.from_dict(film)

            #add each film to current list and persist
        if (imported_films):
            for film in imported_films:
                append_and_store_films(film)

        print("Import was successfull!")

    except (json.JSONDecodeError, KeyError, TypeError, PermissionError, ValueError) as error:
            print(f"Import was not successfull: {error}")
            return

#Leonid Kaup
def export_films():
    ## Check if films are available
    persisted_films = get_all_persisted_films()
    if(not persisted_films or persisted_films == None):
        print("No Films available to export")
        return

    export_option = input("Please type 1 for JSON and 2 for PDF\n").strip()
    if not (export_option == "1" or export_option == "2"):
        print("Please selecte a valid option")
        export_films()
        return

    ## as json on disred location 
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
        except:
            print("Export was not Successful!")

    ## first pdf gets formatted based on existing data with reportlab and then it gets saved.
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
                    Paragraph(f"<b>{escape(str(film['titel']))}</b>", styles["Heading2"]),
                    Paragraph(f"Genre: {escape(str(film['genre']))}", styles["BodyText"]),
                    Paragraph(f"Erscheinungsdatum: {escape(str(film['dateOfRelease']))}", styles["BodyText"]),
                    Paragraph(f"Bewertung: {escape(str(rating))}", styles["BodyText"]),
                    Paragraph(f"Gesehen am: {escape(str(film['watchdate']))}", styles["BodyText"]),
                    Paragraph(f"Schauspieler: {escape(actors)}", styles["BodyText"]),
                    Paragraph(f"Beschreibung: {escape(str(film['description']))}", styles["BodyText"]),
                    Spacer(1, 12),
                ])

            pdf=SimpleDocTemplate(export_file_location, pagesize=A4)
            pdf.build(content)
            print("Export was Successful!")
        except:
            print("Export was not Successful!")
        
# TODO: get_film()
# TODO: get_all_films()
# TODO: update_film()
# TODO: delete_film()
# TODO: rate_film()
# TODO: search_film()
#Leonid Kaup
def search_by_title(filmlist, title):
    result = []
    for film in filmlist:
        if film["title"].lower().strip() == title.lower().strip():
            result.append(film)
    return result
#Leonid Kaup
def search_by_genre(filmlist, genre):
    result = []
    for film in filmlist:
        if film["genre"].lower().strip() == genre.lower().strip():
            result.append(film)
    return result
#Leonid Kaup
def search_by_actors(filmlist, actors):
    result = []
    for actor in actors:
        for film in filmlist:
            for filmactor in film["actors"]:
                if filmactor.lower().strip() == actor.lower().strip():
                    result.append(film)
    return result
#Leonid Kaup
def sort_list_by_rating(filmlist):
    sortedList= sorted(filmlist, key=rating, reverse=True)
    return sortedList
#Leonid Kaup
def rating(film):
    return film["rating"]
#Leonid Kaup
def top_films(filmlist, top_number):
    top_number = top_number
    sorted_list = sort_list_by_rating(filmlist)
    if top_number > len(sorted_list):
        top_number = len(sorted_list)
    return sorted_list[:top_number]
#Leonid Kaup
def flop_films(filmlist, flop_number):
    sorted_list = sort_list_by_rating(filmlist)
    if flop_number > len(sorted_list):
         flop_number = len(sorted_list)
    return sorted_list[-flop_number:]

