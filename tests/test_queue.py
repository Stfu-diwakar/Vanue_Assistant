from utils.queue import predict_wait_time

def test_wait_time():
    result = predict_wait_time("Food Stall 1")
    assert result >= 1
