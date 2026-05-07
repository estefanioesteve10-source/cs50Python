from bank import value

def test_value_zero():
    # Testa variações de "hello" que devem retornar 0
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Newman") == 0

def test_value_twenty():
    # Testa palavras que começam com "h" (mas não hello) que devem retornar 20
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("How you doing?") == 20

def test_value_hundred():
    # Testa qualquer outra coisa que deve retornar 100
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("123") == 100

def test_case_insensitivity():
    # Garante que a capitalização não mude o resultado
    assert value("hElLo") == 0
    assert value("HiYa") == 20
