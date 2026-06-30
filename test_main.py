from main import Calc

def test_getZegop_positive():
    calc = Calc()
    assert calc.getZegop(3) == 9


def test_getZegop_zero():
    calc = Calc()
    assert calc.getZegop(0) == 0


def test_getZegop_negative():
    calc = Calc()
    assert calc.getZegop(-4) == 16