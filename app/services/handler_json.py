import json
from json.decoder import JSONDecodeError

from app.exceptions.user_exc import EmailAlreadyExistsError

FILEPATH = "app/database/database.json"

def read_json(filepath:str) -> list:
    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)
    except (JSONDecodeError, FileNotFoundError):
        with open(filepath, "w") as json_file:
            json.dump({"data": []}, json_file)
            return {"data": []}

def write_json(filepath: str, payload: dict):
        json_list = read_json(filepath)
        json_list["data"].append(payload)

        with open(filepath, "w") as json_file:
            json.dump(json_list, json_file, indent=2)
        return payload

def generate_id():
    data = read_json(FILEPATH)
    MaxID = 0
    for user in data["data"]:
        if MaxID < user["id"]:
            MaxID = user["id"]
    return MaxID+1

def check_unique_email(email):
    data = read_json(FILEPATH)
    if len(data["data"]) > 0:
        for user in data["data"]:
            print(user)
            if email.lower() == user["email"]:
               raise EmailAlreadyExistsError


