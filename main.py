from storage.store_service import json_exists
from services.actions import handle_action


# gets called when starting project
print("Welcome to the film rating tool")

def run():
    if json_exists():
        prompt = "What do you want to do? (type \"help\" for commands): "
        while True:
            action = input(prompt)
            if action == "end":
                break
            handle_action(action)
            prompt = "What do you want to do? (type \"help\" for commands): "
    else:
        prompt = "What do you want to do? (\"import_file\"/\"new_film\"/\"end\"): "
        while True:
            action = input(prompt)
            if action == "end":
                break
            elif action == "import_file":
                handle_action(action)
                run()
                break
            elif action == "new_film":
                handle_action(action)
                run()
                break
run()