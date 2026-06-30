import pytest

from main import Calc


def test_sample():
    assert 1 == 1
    pytest.fail()

def test_get_minus():
    calc = Calc()
    assert calc.get_minus(1, 2) == -1