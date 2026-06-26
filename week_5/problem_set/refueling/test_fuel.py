from Week_5.Problem_Set.Refueling.fuel import convert as c, gauge as g

import pytest


def test_gauge():
    assert g(99) == "F"
    assert g(100) == "F"
    assert g(0) == "E"
    assert g(1) == "E"
    assert g(50) == "50%"


def test_normal():
    assert c("1/2") == 50


def test_round():
    assert c("1/3") == 33


def test_value_error():
    with pytest.raises(ValueError):
        c("5/1")
    with pytest.raises(ValueError):
        c("cat")
    with pytest.raises(ValueError):
        c("cat/dog")
    with pytest.raises(ValueError):
        c("1/-2")
    with pytest.raises(ValueError):
        c("-1/2")


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        c("1/0")


def test_boundaries():
    assert c("0/100") == 0
    assert c("100/100") == 100
