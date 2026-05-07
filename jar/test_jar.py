import pytest
from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar_default = Jar()
    assert jar_default.capacity == 12
    # Testa se capacidade negativa gera erro
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    # Testa depósito acima da capacidade
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
    # Testa retirada maior que o saldo atual
    with pytest.raises(ValueError):
        jar.withdraw(1)
