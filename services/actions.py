from services import film_service
from storage import store_service

FILM_ACTIONS = {"new_film", "list_films", "update_film", "delete_film"}

# handles action and redirects to the appropriate service function
def handle_action(action):
    if action in FILM_ACTIONS:
        service_action = getattr(film_service, action, None)
        if callable(service_action):
            return service_action()
        print(f"Film action is not implemented: {action}")
        return

    service_action = getattr(store_service, action, None)
    if callable(service_action):
        return service_action()

    print(f"Unknown action: {action}")