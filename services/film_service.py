# All services/functions related to films

from datetime import datetime
from utils.helper import validate_date
import json

from utils.sort_filter_helper import search_by_title, search_by_actors, sort_list_by_rating, top_films, flop_films, _read_result_count, _print_search_results, unrated_films

from models.film_model import Film
from storage.store_service import append_and_store_films
from storage.store_service import get_films_from_json
from storage.store_service import get_all_persisted_films
from storage.store_service import store_films
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
        title=input("Title: "),
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

#Johnatan Engel
# rates a film and stores the rating together with the watch date
def rate_film():
    films = _load_films()
    if films is None:
        return
    index = _select_film(films, "rate")
    if index is None:
        return

    film = films[index]
    print(f"Rating \"{film.title}\" (current rating: {film.rating})")
    film.rating = _read_rating()
    film.watch_date = _read_watch_date()

    if _save_films(films):
        print(f"\"{film.title}\" rated {film.rating}/10, watched on {film.watch_date}.")

#Johnatan Engel
def _read_watch_date():
    while True:
        date_text = _read_date("Watch date (dd.mm.yyyy): ")

        if datetime.strptime(date_text, "%d.%m.%Y") > datetime.now():
            print("The watch date cannot be in the future.")
            continue
        return date_text
#Johnatan Engel
# loads all persisted films as Film objects, returns None if the file is not valid
def _load_films():
    try:
        films = get_all_persisted_films()

        if not isinstance(films, list):
            raise TypeError("expected a list of films")
        return [Film.from_dict(film) for film in films]

    except (json.JSONDecodeError, KeyError, TypeError, PermissionError, ValueError) as error:
        print(f"The films could not be read: {error}")
        return None
#Johnatan Engel
# writes all films back to the JSON file, returns True if it worked
def _save_films(films):
    try:
        store_films([film.to_dict() for film in films])
        return True
    except OSError as error:
        print(f"The films could not be saved: {error}")
        return False
#Johnatan Engel
# shows all films numbered and lets the user pick one, returns the index
def _select_film(films, action):
    if not films:
        print("There are no films yet. Use \"new_film\" or \"import_file\" first.")
        return None

    for number, film in enumerate(films, start=1):
        print(f"{number}. {film.title} ({film.date_of_release}) - Rating: {film.rating}")

    while True:
        choice = input(f"Number of the film to {action} (or \"q\" to cancel): ").strip()

        if choice.lower() == "q":
            print("Cancelled.")
            return None
        if not choice.isdigit() or not 1 <= int(choice) <= len(films):
            print(f"Please enter a number from 1 to {len(films)}.")
            continue
        return int(choice) - 1
#Johnatan Engel
# asks a yes/no question, only "y" counts as yes
def _confirm(question):
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer == "y"

#Johnatan Engel
# changes the data of an existing film, rating and watch date are changed by rate_film
def update_film():
    films = _load_films()
    if films is None:
        return
    index = _select_film(films, "update")
    if index is None:
        return

    old_film = films[index]
    print("Press Enter to keep the value shown in [brackets].")
    updated_film = Film(
        title=_read_title_or_keep(old_film.title, films, index),
        date_of_release=_read_date_or_keep("Date of release (dd.mm.yyyy)", old_film.date_of_release),
        genre=_read_text_or_keep("Genre", old_film.genre),
        rating=old_film.rating,
        description=_read_text_or_keep("Description", old_film.description),
        actors=_read_actors_or_keep(old_film.actors),
        watch_date=old_film.watch_date,
    )

    print("\nPreview:")
    _print_film(updated_film)
    if not _confirm("Save changes?"):
        print("Changes discarded.")
        return

    films[index] = updated_film
    if _save_films(films):
        print(f"\"{updated_film.title}\" has been updated.")

#Johnatan Engel
def _read_text_or_keep(prompt, current):
    text = input(f"{prompt} [{current}]: ").strip()

    if text == "":
        return current
    return text
#Johnatan Engel
# the title must not be used by another film in the list
def _read_title_or_keep(current, films, index):
    while True:
        title = _read_text_or_keep("Titel", current)
        duplicate = False

        for number, film in enumerate(films):
            if number != index and film.title.lower() == title.lower():
                duplicate = True

        if duplicate:
            print(f"A film called \"{title}\" already exists.")
            continue
        return title
#Johnatan Engel
def _read_date_or_keep(prompt, current):
    while True:
        date_text = input(f"{prompt} [{current}]: ").strip()

        if date_text == "":
            return current
        if validate_date(date_text):
            return date_text
        else:
            print("Please enter a valid date in dd.mm.yyyy format.")
#Johnatan Engel
def _read_actors_or_keep(current):
    actors_text = input(f"Actors (comma-separated) [{', '.join(current)}]: ").strip()

    if actors_text == "":
        return current
    return [actor.strip() for actor in actors_text.split(",") if actor.strip()]

def _print_film(film):
    print(f"Titel: {film.title}")
    print(f"Date of release: {film.date_of_release}")
    print(f"Genre: {film.genre}")
    print(f"Rating: {film.rating}")
    print(f"Description: {film.description}")
    print(f"Actors: {', '.join(film.actors)}")
    print(f"Watch date: {film.watch_date}")

#Johnatan Engel
# removes a film from the list after the user confirmed it
def delete_film():
    films = _load_films()
    if films is None:
        return
    index = _select_film(films, "delete")
    if index is None:
        return

    film = films[index]
    if not _confirm(f"Really delete \"{film.title}\"?"):
        print("Deletion cancelled.")
        return

    films.pop(index)
    if _save_films(films):
        print(f"\"{film.title}\" has been deleted.")


# TODO: get_film()
# TODO: get_all_films()
# TODO: search_films()
# TODO: top_films()
# TODO: films_by_genre()
# TODO: films_by_contributor()
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
        except Exception as e:
            print("Export was not Successful!", e)
        
# TODO: get_all_films()
# TODO: update_film()
# TODO: delete_film()

#Leonid Kaup
def search_filter_sort_movie():
    while True:
        action = input(
            "\nHow would you like to browse your movies?\n"
            "  1: Search by title or actor\n"
            "  2: Show a list sorted by rating\n"
            "  3: Show the top-rated movies\n"
            "  4: Show the lowest-rated movies\n"
            "  5: Show unrated movies\n"
            "  B: Back to menu\n"
            "\nPlease enter 1, 2, 3, 4, 5, or B: "
        ).strip().lower()

        if action == "1":
            search_movies()
        elif action == "2":
            sort_movies_by_rating()
        elif action == "3":
            show_top_movies()
        elif action == "4":
            show_flop_movies()
        elif action == "5":
            show_unrated_movies()
        elif action == "b":
            return
        else:
            print("Please enter 1, 2, 3, 4, 5, or B.")

#Leonid Kaup
def search_movies():
    while True:
        filter_action = input(
            "\nWhat would you like to search by?\n"
            "  A - Actor\n"
            "  T - Movie title\n"
            "  B - Back to menu\n"
            "\nPlease enter A, T, or B: "
        ).strip().lower()

        if filter_action == "b":
            return
        elif filter_action == "a":
            search_movies_by_actor()
        elif filter_action == "t":
            search_movies_by_title()
        else:
            print("Please enter A, T, or B.")

#Leonid Kaup
def search_movies_by_actor():
    while True:
        try:
            actor_names = input(
                "\nEnter actor names separated by commas, or B to go back: "
            ).strip()
            if actor_names.lower() == "b":
                return
            if not actor_names:
                raise ValueError("Please enter at least one actor name.")

            actors = []
            for actor in actor_names.split(","):
                actor = actor.strip()
                if actor:
                    actors.append(actor)

            films = get_all_persisted_films()
            results = search_by_actors(films, actors)
            _print_search_results(results)
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Search failed: {error}")

#Leonid Kaup
def search_movies_by_title():
    while True:
        try:
            title = input(
                "\nEnter the movie title, or B to go back: "
            ).strip()
            if title.lower() == "b":
                return
            if not title:
                raise ValueError("Please enter a movie title.")

            films = get_all_persisted_films()
            results = search_by_title(films, title)
            _print_search_results(results)
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Search failed: {error}")

#Leonid Kaup
def sort_movies_by_rating():
    try:
        films = get_all_persisted_films()
        _print_search_results(sort_list_by_rating(films))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Sorting failed: {error}")

#Leonid Kaup
def show_top_movies():
    try:
        top_number = _read_result_count("Enter the number of top-rated movies")
        if top_number is None:
            return
        films = get_all_persisted_films()
        _print_search_results(top_films(films, top_number))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not get the top-rated movies: {error}")

#Leonid Kaup
def show_flop_movies():
    try:
        flop_number = _read_result_count("Enter the number of lowest-rated movies")
        if flop_number is None:
            return
        films = get_all_persisted_films()
        _print_search_results(flop_films(films, flop_number))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not get the lowest-rated movies: {error}")

#Leonid Kaup
def show_unrated_movies():
    try:
        films = get_all_persisted_films()
        _print_search_results(unrated_films(films))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not get the unrated movies: {error}")
