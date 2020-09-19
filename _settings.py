from json import loads

with open("data/settings.json", "r") as file: SETTINGS = loads(file.read())
