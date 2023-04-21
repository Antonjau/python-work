from numb3rs import validate


def test_valid_ipv4():
    assert validate('192.168.1.1') == True
    assert validate('10.0.0.1') == True
    assert validate('172.16.0.1') == True


def test_invalid_ipv4():
    assert validate('256.0.0.1') == False
    assert validate('0.0.0.0.0') == False
    assert validate('1.2.3.4.5') == False
