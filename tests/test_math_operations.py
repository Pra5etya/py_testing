from functions.math_operations import multiply, divide

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
