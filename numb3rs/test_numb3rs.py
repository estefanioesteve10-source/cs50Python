from numb3rs import validate

def test_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("512.1.1.1") == False

def test_non_numeric():
    assert validate("cat") == False
    assert validate("1.2.3.dog") == False
    assert validate("192.168.0.1") == True
