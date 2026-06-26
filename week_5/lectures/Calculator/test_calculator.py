"""
from a_calculator import square


def main():
    test_square()


def test_square():

    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(4) == 9
    except AssertionError:
        print("3 squared was not 9")



if __name__ == "__main__":
    main()
"""

import pytest

from Week_5.Lectures.Calculator.calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
