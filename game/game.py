import random

def main():
    # 1. Solicita o nível (n) até obter um inteiro positivo
    level = get_positive_int("Level: ")

    # 2. Gera o número secreto entre 1 e o nível escolhido
    target = random.randint(1, level)

    # 3. Loop de adivinhação
    while True:
        guess = get_positive_int("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_positive_int(prompt):
    """Função auxiliar para garantir que a entrada seja um inteiro > 0"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            # Ignora erros de conversão (ex: se o usuário digitar 'cat')
            pass

if __name__ == "__main__":
    main()
