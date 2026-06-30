import pytest
from main import Calc


def test_get_divide():
    calc = Calc()
    assert calc.getDivide(4, 2) == 2
    assert calc.getDivide(4, 0) == 0
    

@pytest.mark.parametrize("a,b,res", [(2, 3, 6), (12, 12, 144)])
def test_gop(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res


@pytest.mark.parametrize("a,b,res", [(2, 0, 0), (0, 12, 0)])
def test_gop_zero(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res


@pytest.mark.parametrize("a,b,res", [(2, -1, -2), (-12, 12, -144)])
def test_gop_plus_minus(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res


@pytest.mark.parametrize("a,b,res", [(-2, -1, 2), (-12, -12, 144)])
def test_gop_minus_minus(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res

    
def test_get_sum():
    calc = Calc()
    assert calc.get_sum(1, 2) == 3

    
def test_get_sum_sum():
    calc = Calc()
    assert calc.get_sum_sum(1, 2, 3) == 6

    
def test_get_minus():
    calc = Calc()
    assert calc.get_minus(1, 2) == -1
