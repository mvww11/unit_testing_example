from unit_testing_example.my_functions import add

def test_positive_numbers():
    total = add(1,2)
    assert total == 3

def test_negative_numbers():
    total = add(-5,-2)
    assert total == -7