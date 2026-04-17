from utils.routing import get_best_route

def test_route():
    route = get_best_route("Gate 1", "Seat A")
    assert "Seat A" in route
