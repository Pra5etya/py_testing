# import sys
# sys.path.insert(0, 'D:\GIT Data\py_unit_test\functions')

from codes.math_operations import multiply, divide

def test_multiply():
    assert multiply(2, 3) == 6, 'The input results do not match the output'
    assert multiply(-1, 1) == -1, 'The input results do not match the output'
    assert multiply(-1, -1) == 1, 'The input results do not match the output'

def test_divide():
    assert divide(6, 3) == 2, 'The input results do not match the output'
    assert divide(-1, 1) == -1, 'The input results do not match the output'
    assert divide(5, 2) == 2.5, 'The input results do not match the output'

def test_divide_by_zero():
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
