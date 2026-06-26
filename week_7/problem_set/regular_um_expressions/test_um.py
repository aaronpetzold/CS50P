import pytest

from um import count as c


def test_single_um():
    assert c("um") == 1


def test_um_with_punctuation():
    assert c("um?") == 1


def test_case_insensitive():
    assert c("Um") == 1
    assert c("UM") == 1


def test_multiple_um():
    assert c("Um, i don´t know, um...") == 2


def test_not_as_substring():
    assert c("yummy") == 0
    assert c("umbrella") == 0


def test_um_in_sentence():
    assert c("Hello um world") == 1
