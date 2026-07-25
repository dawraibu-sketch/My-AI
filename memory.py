import json

def load_memory():
    with open("memory.json", "r") as file:
        return json.load(file)
