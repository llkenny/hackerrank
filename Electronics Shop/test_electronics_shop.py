import pytest
from electronics_shop import getMoneySpent

def test_case_1():
    b = 60
    keyboards = [40, 50, 60]
    drives = [5, 8, 12]
    assert getMoneySpent(keyboards, drives, b) == 58
