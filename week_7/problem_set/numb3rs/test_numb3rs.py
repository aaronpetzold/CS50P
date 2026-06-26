from numb3rs import validate as v


def test_longer_length():
    assert v("255.255.255.255.255") == False


def test_shorter_length():
    assert v("255.255.255") == False


def test_correct_length():
    assert v("255.255.255.255") == True


def test_range():
    assert v("266.255.255.255") == False
    assert v("1.277.255.255") == False



def test_leading_zeros():
    assert v("001.255.255.255") == False
    assert v("01.255.255.255") == False
