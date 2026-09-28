from pathlib import Path


def csv_exists():
    file_path = Path("storage/films.csv")

    if file_path.is_file():
        print("CSV exists")
        return True
    else:
        print("CSV does not exist - either import a csv-file or create a new film")
        return False