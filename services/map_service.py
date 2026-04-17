from config import DEFAULT_LOCATION

def get_map_center():
    return DEFAULT_LOCATION["lat"], DEFAULT_LOCATION["lon"]

def get_crowd_markers():
    return [
        {
            "location": [28.6005, 77.2005],
            "type": "high",
            "label": "Gate A"
        },
        {
            "location": [28.601, 77.201],
            "type": "low",
            "label": "Gate B"
        },
        {
            "location": [28.602, 77.202],
            "type": "moderate",
            "label": "Food Court"
        }
    ]
