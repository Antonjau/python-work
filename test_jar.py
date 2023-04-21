from jar import Jar


def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0
    assert str(j) == ""

    j = Jar(20)
    assert j.capacity == 20
    assert j.size == 0
    assert str(j) == ""


def test_init_errors():
    try:
        j = Jar(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError"

    try:
        j = Jar("foo")
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError"


def test_deposit():
    j = Jar()
    j.deposit(5)
    assert j.size == 5
    assert str(j) == "🍪🍪🍪🍪🍪"

    j.deposit(7)
    assert j.size == 12
    assert str(j) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    try:
        j.deposit(1)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError"

    try:
        j.deposit(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError"

    assert j.size == 12
    assert str(j) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
