import json
from pathlib import Path

from models.film_model import Film

FILMS_FILE = Path(__file__).resolve().with_name("films.json")


# get films from persistent JSON-file
def get_all_persisted_films():
    return get_films_from_json(FILMS_FILE)

# get films from a json file in general
def get_films_from_json(file):
    if not file.exists():
        return []

    with file.open("r", encoding="utf-8") as file:
            films = json.load(file)
    return films


# Store films in persistent JSON-file
def store_film(film):
    films = get_all_persisted_films()

    films.append(film)
    with FILMS_FILE.open("w", encoding="utf-8") as file:
        json.dump(films, file, indent=2, ensure_ascii=False)
        file.write("\n")


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
        print("The JSON data structure does not match the Film model.")
        raise SystemExit(1)

    print("JSON exists")
    return True
