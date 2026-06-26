import pytest
from working import convert as c

# Valid Inputs


def test_no_minutes():
    assert c("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert c("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed_formats():
    assert c("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert c("9:00 AM to 5 PM") == "09:00 to 17:00"


def test_different_times():
    assert c("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert c("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_12_am_conversion():
    assert c("12:00 AM to 1:00 PM") == "00:00 to 13:00"


def test_12_pm_conversion():
    assert c("12:00 PM to 1:00 AM") == "12:00 to 01:00"


# Invalid Inputs


def test_invalid_hour_too_low():
    with pytest.raises(ValueError):
        c("0 AM to 5 PM")


def test_invalid_hour_too_high():
    with pytest.raises(ValueError):
        c("13 AM to 5 PM")


def test_invalid_minute_too_high():
    with pytest.raises(ValueError):
        c("9:60 AM to 5:00 PM")


def test_wrong_separator():
    with pytest.raises(ValueError):
        c("9 AM - 5 PM")


def test_missing_to():
    with pytest.raises(ValueError):
        c("9 AM 5 PM")


def test_invalid_period():
    with pytest.raises(ValueError):
        c("9 XM to 5 PM")
