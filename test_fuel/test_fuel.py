import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_errors():
    # Testa se gera ValueError quando X > Y
    with pytest.raises(ValueError):
        convert("5/4")
    # Testa se gera ValueError quando não são números
    with pytest.raises(ValueError):
        convert("three/four")
    # Testa se gera ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_labels():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentages():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
