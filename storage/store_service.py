import json
from pathlib import Path

FILMS_FILE = Path(__file__).resolve().with_name("films.json")

# get films from persistent JSON-file
def get_all_films():
    if not FILMS_FILE.exists():
        return []

    with FILMS_FILE.open("r", encoding="utf-8") as file:
        films = json.load(file)
    if not isinstance(films, list):
        raise ValueError("The films JSON file must contain a list")
    return films

# Store films in persistent JSON-file
def store_film(film):
    films = get_all_films()

    films.append(film)
    with FILMS_FILE.open("w", encoding="utf-8") as file:
        json.dump(films, file, indent=2, ensure_ascii=False)
        file.write("\n")

# Check if the JSON file exists
def json_exists():
    file_path = Path("storage/films.json")

    if file_path.is_file():
        print("JSON exists")
        return True
    else:
        print("JSON does not exist - either import a json-file or create a new film")
        return False