# All services/functions related to films

from datetime import datetime

from models.film_model import Film
from storage.store_service import get_all_films, store_film


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
    store_film(film.to_dict())
    print("Film saved.")


def _read_date(prompt):
    while True:
        date_text = input(prompt)
        try:
            parsed_date = datetime.strptime(date_text, "%d.%m.%Y")
            if parsed_date.strftime("%d.%m.%Y") == date_text:
                return date_text
        except ValueError:
            pass
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


# TODO: get_film()
# TODO: get_all_films()
# TODO: update_film()
# TODO: delete_film()
# TODO: import_film()
# TODO: rate_film()
# TODO: search_films()
# TODO: top_films()
# TODO: films_by_genre()
# TODO: films_by_contributor()
