from lonely_integer import lonelyinteger
import pytest

def test_first():
    assert lonelyinteger([1, 2, 2]) == 1

def test_not_first():
    assert lonelyinteger([3, 3, 1, 2, 2]) == 1
