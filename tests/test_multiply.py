from app.my_functions import multiply

def test_positive_numbers():
    total = multiply(1,2)
    assert total == 2

def test_negative_numbers():
    total = multiply(-5,-2)
    assert total == 10