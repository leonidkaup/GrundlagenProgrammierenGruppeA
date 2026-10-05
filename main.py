from storage.store_service import json_exists
from services.actions import handle_action

# gets called when starting project
print("Welcome to the film rating tool")

if json_exists():
    prompt = "What do you want to do? (type \"help\" for commands): "
else:
    prompt = "What do you want to do? (\"import_file\"/\"new_film\"): "

# While actions is not "end", user gets asked to input action
while True:
    action = input(prompt)
    handle_action(action)
    prompt = "What do you want to do? (type \"help\" for commands): "