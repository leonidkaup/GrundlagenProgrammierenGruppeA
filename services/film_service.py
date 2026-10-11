# All services/functions related to films

from datetime import datetime
from utils.helper import validate_date
import json

from models.film_model import Film
from storage.store_service import append_and_store_films
from storage.store_service import get_films_from_json
from storage.store_service import get_all_persisted_films
from storage.store_service import store_films
from pathlib import Path

from tkinter import filedialog


# writes a new film to the JSON file
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


def _read_date(prompt):
    while True:
        date_text = input(prompt)

        if validate_date(date_text):
            return date_text
        else:
            print("Please enter a valid date in dd.mm.yyyy format.")

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


def _read_watch_date():
    while True:
        date_text = _read_date("Watch date (dd.mm.yyyy): ")

        if datetime.strptime(date_text, "%d.%m.%Y") > datetime.now():
            print("The watch date cannot be in the future.")
            continue
        return date_text

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

# writes all films back to the JSON file, returns True if it worked
def _save_films(films):
    try:
        store_films([film.to_dict() for film in films])
        return True
    except OSError as error:
        print(f"The films could not be saved: {error}")
        return False

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

# asks a yes/no question, only "y" counts as yes
def _confirm(question):
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer == "y"


# TODO: get_film()
# TODO: get_all_films()
# TODO: update_film()
# TODO: delete_film()
# TODO: search_films()
# TODO: top_films()
# TODO: films_by_genre()
# TODO: films_by_contributor()
