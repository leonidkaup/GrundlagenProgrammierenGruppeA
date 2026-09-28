from storage.store_service import csv_exists

# gets called when starting project
print("Welcome to the film rating tool")

# TODO: Look for csv-file. If none is there, ask user for import or new film
if csv_exists():
    print("CSV exists")
else:
    action = input("What do you want to do? (import_file/new_film): ")