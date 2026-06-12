import pytest
from datetime import date
from seasons import parse_date, get_minutes, get_minutes_in_words


def test_parse_date_valid():
    assert parse_date("2007-11-23") == date(2007, 11, 23)


def test_parse_date_invalid_format():
    with pytest.raises(ValueError):
        parse_date("2007/11/23")
    with pytest.raises(ValueError):
        parse_date("23rd November, 2007")
    with pytest.raises(ValueError):
        parse_date("23.11.2007")


def test_parse_date_invalid_value():
    with pytest.raises(ValueError):
        parse_date("2007-23-11")
    with pytest.raises(ValueError):
        parse_date("2007-11-40")


def test_get_minutes():
    assert get_minutes(1) == 1440
    assert get_minutes(22) == 31680


def test_get_minutes_in_words():
    assert get_minutes_in_words(0) == "Zero minutes"
    assert get_minutes_in_words(1) == "One minutes"
    assert get_minutes_in_words(1440) == "One thousand, four hundred forty minutes"
