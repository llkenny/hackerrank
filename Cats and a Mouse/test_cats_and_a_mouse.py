import pytest
from cats_and_a_mouse import catAndMouse

def test_case_1():
    x = 2
    y = 5
    z = 4
    result = catAndMouse(x, y, z)
    assert result == "Cat B"
