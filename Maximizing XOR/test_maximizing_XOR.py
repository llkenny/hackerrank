import pytest
from maximizing_XOR import maximizingXor

def test_case_1():
    assert maximizingXor(11, 12) == 7


def test_case_2():
    assert maximizingXor(10, 15) == 7


def test_case_3():
    assert maximizingXor(11, 100) == 127
