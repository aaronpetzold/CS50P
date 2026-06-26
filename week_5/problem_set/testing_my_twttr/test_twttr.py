from Week_5.Problem_Set.Testing_my_twttr.twttr import shorten as s

import pytest


def test_lowercase():
    assert s("hello") == "hll"


def test_uppercase():
    assert s("HELLO") == "HLL"


def test_mixed():
    assert s("HeLlO") == "HLl"


def test_no_vowels():
    assert s("bcdfg") == "bcdfg"


def test_only_vowels():
    assert s("aeiou") == ""


def test_empty():
    assert s("") == ""


def test_numbers():
    assert s("cs50") == "cs50"


def test_puncuation():
    assert s("hello!") == "hll!"


def test_spaces():
    assert s("hello world") == "hll wrld"
