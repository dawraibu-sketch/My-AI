import json

def load_knowledge():
    with open("knowledge.json", "r") as file:
        return json.load(file)

def save_knowledge(knowledge):
    with open("knowledge.json", "w") as file:
        json.dump(knowledge, file, indent=4)
