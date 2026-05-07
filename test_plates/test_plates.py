from plates import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("OUTATIME") == False

def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False

def test_number_placement():
    # Números no meio não são permitidos
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    # O primeiro número não pode ser zero
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50!") == False

def test_only_letters():
    assert is_valid("HELLO") == True
