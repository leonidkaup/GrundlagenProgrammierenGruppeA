from storage.store_service import csv_exists
from services.actions import handle_action

action = ""

# gets called when starting project
print("Welcome to the film rating tool")

# TODO: Look for csv-file. If none is there, ask user for import or new film
if csv_exists():
    action = input("What do you want to do? (type \"help\" for commands): ")
else:
    action = input("What do you want to do? (\"import_file\"/\"new_film\"): ")

handle_action(action)