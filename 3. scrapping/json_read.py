import json


with open('hh.json') as file:
    data = json.load(file)
    print(data)