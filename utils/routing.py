graph = {
    "Gate 1": ["Corridor A"],
    "Gate 2": ["Corridor B"],
    "Corridor A": ["Seat A", "Washroom"],
    "Corridor B": ["Food Court", "Exit"],
    "Food Court": ["Washroom"],
    "Washroom": ["Exit"],
    "Seat A": [],
    "Exit": []
}

def get_best_route(start, end):
    visited = set()
    queue = [(start, [start])]

    while queue:
        node, path = queue.pop(0)

        if node == end:
            return " → ".join(path)

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))

    return "Route not available"
