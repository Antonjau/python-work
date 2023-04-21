import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert('0/1') == 0
    assert convert('1/1') == 100
    assert convert('1/2') == 50
    assert convert('49/50') == 98
    assert convert('50/50') == 100
    assert convert('0/100') == 0
    assert convert('99/100') == 99
    assert convert('100/100') == 100

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('2/1')
    with pytest.raises(ValueError):
        convert('1.0/2')
    with pytest.raises(ValueError):
        convert('1/2.0')

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
    assert gauge(98) == 'F'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_integration_valid():
    assert gauge(convert('0/1')) == 'E'
    assert gauge(convert('1/1')) == 'F'
    assert gauge(convert('1/2')) == '50%'
    assert gauge(convert('49/50')) == 'F'
    assert gauge(convert('50/50')) == 'F'
    assert gauge(convert('0/100')) == 'E'
    assert gauge(convert('99/100')) == 'F'
    assert gauge(convert('100/100')) == 'F'

def test_integration_invalid():
    with pytest.raises(ValueError):
        gauge(convert('1/0'))
    with pytest.raises(ValueError):
        gauge(convert('2/1'))
    with pytest.raises(ValueError):
        gauge(convert('1.0/2'))
    with pytest.raises(ValueError):
        gauge(convert('1/2.0'))
    with pytest.raises(ZeroDivisionError):
        gauge(convert('1/0'))
