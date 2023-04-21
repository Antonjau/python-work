import bank

def test_value_hello():
    assert bank.value("hello, world") == 0
    assert bank.value("Hello, World") == 0
    assert bank.value("HELLO, WORLD") == 0

def test_value_h():
    assert bank.value("hi") == 20
    assert bank.value("Happiness") == 20
    assert bank.value("House") == 20

def test_value_other():
    assert bank.value("world") == 100
    assert bank.value("goodbye") == 100
    assert bank.value("123") == 100

def test_value_empty():
    assert bank.value("") == 100

def test_value_whitespace():
    assert bank.value(" hello") == 100
    assert bank.value("hi there") == 100
    assert bank.value("   ") == 100
