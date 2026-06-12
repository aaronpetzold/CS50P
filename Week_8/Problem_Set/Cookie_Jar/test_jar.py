import pytest
from jar import Jar

# --- Test Initialization ---


# Valid
def test_init_valid():
    jar1 = Jar(12)
    assert jar1.capacity == 12
    assert jar1.size == 0

    jar2 = Jar(0)
    assert jar2.capacity == 0
    assert jar2.size == 0

    jar3 = Jar(30)
    assert jar3.capacity == 30
    assert jar3.size == 0


# Invalid
def test_init_invalid_type():
    with pytest.raises(ValueError):
        Jar("cat")
    with pytest.raises(ValueError):
        Jar(1.5)
    with pytest.raises(ValueError):
        Jar(True)


def test_init_invalid_int():
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


# Valid
def test_valid_deposit():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12


# Invalid
def test_invalid_deposit_negative_n():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-6)


def test_invalid_deposit_too_large():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)


# --- Test Withdraw ---


# Valid
def test_valid_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    assert jar.capacity == 12
    assert jar.size == 5


# Invalid
def test_invalid_withdraw_negative_n():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-5)


def test_invalid_withdraw_too_large():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(14)
