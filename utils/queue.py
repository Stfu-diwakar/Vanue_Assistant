import random

base_wait_times = {
    "Food Stall 1": 10,
    "Washroom A": 5
}

def predict_wait_time(location):
    base = base_wait_times.get(location, 5)
    fluctuation = random.randint(-3, 5)
    return max(1, base + fluctuation)
