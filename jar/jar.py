class Jar:
    def __init__(self, capacity=12):
        # Valida se a capacidade é um inteiro não negativo
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacidade deve ser um inteiro não negativo")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Retorna o emoji de biscoito multiplicado pelo número de biscoitos no pote
        return "🍪" * self.size

    def deposit(self, n):
        # Verifica se n é positivo e se não ultrapassa a capacidade total
        if n > (self.capacity - self.size):
            raise ValueError("Não há espaço suficiente no pote")
        self._size += n

    def withdraw(self, n):
        # Verifica se n é positivo e se há biscoitos suficientes para retirar
        if n > self.size:
            raise ValueError("Não há biscoitos suficientes para retirar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
