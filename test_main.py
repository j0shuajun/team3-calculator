import pytest

from main import Calc


def test_sample():
    assert 1 == 1
    pytest.fail()

@pytest.mark.parametrize("a,b,res", [(2,3,6), (12,12,144)])
def test_gop(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res

@pytest.mark.parametrize("a,b,res", [(2,0,0), (0,12,0)])
def test_gop_zero(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res

@pytest.mark.parametrize("a,b,res", [(2,-1,-2), (-12,12,-144)])
def test_gop_plus_minus(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res

@pytest.mark.parametrize("a,b,res", [(-2,-1,2), (-12,-12,144)])
def test_gop_minus_minus(a, b, res):
    sut = Calc()
    assert sut.get_gop(a, b) == res