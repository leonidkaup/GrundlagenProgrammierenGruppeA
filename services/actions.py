from services import film_service

# All possible actions and their descriptions
ACTIONS = {
    "new_film": "Create and save a film.",
    "list_films": "Display saved films (not implemented yet).",
    "update_film": "Update a film (not implemented yet).",
    "delete_film": "Delete a film (not implemented yet).",
    "import_file": "Import films from a file (not implemented yet).",
    "help": "Show this list of commands.",
    "end": "Exit the program.",
}


# handles action and redirects to the appropriate service function
def handle_action(action):
    if action == "help":
        for name, description in ACTIONS.items():
            print(f"{name}: {description}")
    elif action in ACTIONS:
        service_action = getattr(film_service, action, None)
        if callable(service_action):
            service_action()
        else:
            print(f"Action is not implemented: {action}")
    else:
        print(f"Unknown action: {action}")
