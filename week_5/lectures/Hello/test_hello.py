from Week_5.Lectures.Hello.hello import hello


def test_default():
    assert hello() == "hello, world"


def test_agrument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
