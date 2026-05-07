import random

def main():
    level = get_level()
    score = 0

    # Gera 10 problemas
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        tries = 0

        # Loop de 3 tentativas para o mesmo problema
        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

            # Se falhou 3 vezes, mostra a resposta
            if tries == 3:
                print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        # Nível 1 inclui o 0 (0 a 9)
        return random.randint(0, 9)
    elif level == 2:
        # Nível 2: números de 10 a 99 (2 dígitos)
        return random.randint(10, 99)
    elif level == 3:
        # Nível 3: números de 100 a 999 (3 dígitos)
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
