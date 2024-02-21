import json

def save_tasks_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}