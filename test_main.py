import pytest
from main import Calc


def test_get_sum():
    calc = Calc()
    assert calc.get_sum(1, 2) == 3

def test_get_sum_sum():
    calc = Calc()
    assert calc.get_sum_sum(1, 2, 3) == 6

def test_get_minus():
    calc = Calc()
    assert calc.get_minus(1, 2) == -1
