import pytest
from matrix import Matrix

def test_1():
    assert Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) == Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])

def test_2():
    assert Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) + Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) == Matrix([2, -6, 10], [14, -10, -2], [6, -4, 4]) 

def test_3():
    assert Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) * Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) == Matrix([-5, 2, 18], [-31, 6, 38], [-5, -3, 21] )

if __name__ == '__main__':
    pytest.main(['-v'])