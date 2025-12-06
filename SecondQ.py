import json
import yaml

def loadtickets():

    try:
        with open("CommonData.yaml", "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
    except Exception:
        with open("data.json", "r") as json_file:
            json.load(data, json_file, indent=4)

    clean = {}
    for key, value in data.items():
        new_key = key.strip().lower()
        clean[new_key] = value

    with open("clean.json", "w") as f:
        json.dump(clean, f, indent=2)

    return clean

loadtickets()
