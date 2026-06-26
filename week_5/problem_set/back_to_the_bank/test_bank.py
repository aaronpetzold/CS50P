from Week_5.Problem_Set.Back_to_the_Bank.bank import value as v

import pytest


def test_hello():
    assert v("hello") == 0
    assert v("HELLO") == 0
    assert v("Hello") == 0
    assert v("hello world") == 0


def test_h_not_hello():
    assert v("hi") == 20
    assert v("hey") == 20
    assert v("how you doing") == 20
    assert v("h") == 20
    assert v("HEY") == 20
    assert v("Hi there") == 20


def test_other():
    assert v("what´s up") == 100
    assert v("good morning") == 100
    assert v("welcome") == 100
    assert v("123") == 100
    assert v("") == 100
