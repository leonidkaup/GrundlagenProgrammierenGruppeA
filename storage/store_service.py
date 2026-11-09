import json
from pathlib import Path

from models.film_model import Film

FILMS_FILE = Path(__file__).resolve().with_name("films.json")


# get films from the defined persistent JSON-file
# Leonid Kaup
def get_all_persisted_films():
    return get_films_from_json(FILMS_FILE)

# get films from a json file in general
def get_films_from_json(file):
    if not file.exists():
        return []

    with file.open("r", encoding="utf-8") as file:
            films = json.load(file)
    return films

# Leonid Kaup
# Read persisted films, Append to current list and Store films in persistent JSON-file
def append_and_store_films(films):
    persisted_films = get_all_persisted_films()
    persisted_films.append(films)
    store_films(persisted_films)


# Store input list of this function in json
def store_films(films):
    if films is not None:
        with FILMS_FILE.open("w", encoding="utf-8") as file:
            json.dump(films, file, indent=2, ensure_ascii=False)
            file.write("\n")
    else: 
        print("An error occured while persiting the films to json. No action taken")

#Léon Albert
# Check if the JSON file exists
def json_exists():
    if not FILMS_FILE.is_file():
        print(
            "JSON does not exist - either import a json-file "
            "or create a new film"
        )
        return False

    try:
        films = get_all_persisted_films()
        if not isinstance(films, list):
            raise TypeError
        for data in films:
            Film.from_dict(data)
    except (json.JSONDecodeError, KeyError, TypeError):
        print("The persistant JSON data structure does not match the Film model or is corrupted. Please delete the current file to reset it, or fix it manually. If you delete it your data will be lost.")
        exit()

    print("JSON exists")
    return True
