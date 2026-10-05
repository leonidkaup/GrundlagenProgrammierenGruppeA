# All services/functions related to films

from models.film_model import Film
from storage.store_service import get_all_films, store_film

# writes a new film to the JSON file
def new_film():
	film = Film(
		title=input("Titel: "),
		date_of_release=input("Date of release: "),
		genre=input("Genre: "),
		rating=_read_rating(),
		description=input("Description: "),
		actors=[
			actor.strip()
			for actor in input("Actors (comma-separated): ").split(",")
			if actor.strip()
		],
		watch_date=input("Watch date: "),
	)
	store_film(film.to_dict())
	print("Film saved.")

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