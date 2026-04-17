import json
import os

DATA_FILE = "data/sample_data.json"

def read_data():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_zone(zone, value):
    data = read_data()
    data[zone] = value
    write_data(data)

def get_zone_data():
    return read_data()
