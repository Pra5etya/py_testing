# import sys
# sys.path.insert(0, 'D:\GIT Data\py_unit_test\functions')

from codes.calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
