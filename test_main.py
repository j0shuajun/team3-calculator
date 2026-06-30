import pytest

from main import Calc


def test_divide():
    calc = Calc()
    assert calc.getDivide(4, 2) == 2
    assert calc.getDivide(4, 0) == 0