import json

FILE = "memory.json"

def save_memory(key, value):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    data[key] = value

    with open(FILE, "w") as f:
        json.dump(data, f)

def get_memory(key):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return data.get(key, None)
    except:
        return None
