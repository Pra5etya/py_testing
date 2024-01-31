from codes.calculator import add, subtract

def test_add():
    assert add(2, 3) == 5, 'The input results do not match the output'
    assert add(-1, 1) == 0, 'The input results do not match the output'
    assert add(-1, -1) == -2, 'The input results do not match the output'

def test_subtract():
    assert subtract(5, 3) == 2, 'The input results do not match the output'
    assert subtract(-1, 1) == -2, 'The input results do not match the output'
    assert subtract(-1, -1) == 0, 'The input results do not match the output'
