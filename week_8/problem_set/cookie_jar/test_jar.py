import pytest
from jar import Jar


# --- Test Initialization ---


def test_init():

    # Valid
    jar1 = Jar(12)
    assert jar1.capacity == 12
    assert jar1.size == 0

    jar2 = Jar(0)
    assert jar2.capacity == 0
    assert jar2.size == 0

    jar3 = Jar(30)
    assert jar3.capacity == 30
    assert jar3.size == 0

    # Invalid Type
    with pytest.raises(ValueError):
        Jar("cat")
    with pytest.raises(ValueError):
        Jar(1.5)
    with pytest.raises(ValueError):
        Jar(True)

    # Invalid Int
    with pytest.raises(ValueError):
        Jar(-1)


# --- Test Str ---


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# --- Test Deposit ---


def test_deposit():

    # Valid
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12

    # Invalid: Negative n
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-6)

    # Invalid: deposite too large
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)


# --- Test Withdraw ---


def test_withdraw():

    # Valid
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    assert jar.capacity == 12
    assert jar.size == 5

    # Invalid: withdraw negative n
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-5)

    # Invalid: withdraw too large
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(14)
