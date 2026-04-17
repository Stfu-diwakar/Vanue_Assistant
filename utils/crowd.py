import random

zones = ["Gate A", "Gate B", "Food Court", "Seats"]

def get_crowd_density():
    data = {}
    for zone in zones:
        data[zone] = random.randint(30, 90)
    return data

def get_overall_density():
    values = get_crowd_density().values()
    return sum(values) // len(values)
    
