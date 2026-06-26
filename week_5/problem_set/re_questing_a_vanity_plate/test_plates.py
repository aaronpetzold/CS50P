from plates import is_valid as v

import pytest


def test_length():
    assert v("A") == False
    assert v("ABCD1234") == False
    assert v("AB12") == True


def test_alphanumeric():
    assert v("AB.12") == False
    assert v("A-12") == False
    assert v("AB12") == True


def test_first_two_letters():
    assert v("A1") == False
    assert v("1A") == False
    assert v("11") == False
    assert v("AB") == True


def test_numbers_at_end():
    assert v("A1A2") == False
    assert v("AB11AB") == False
    assert v("AB1234") == True


def test_first_number_not_zero():
    assert v("AB01") == False
    assert v("AB10") == True


def test_valid_plates():
    assert v("CS50") == True
    assert v("HELLO") == True
    assert v("ABCDEF") == True
    assert v("AB") == True
