def main():
    # Solicita a saudação do usuário
    greeting = input("Greeting: ")
    # Chama a função value e armazena o resultado
    result = value(greeting)
    # Exibe o valor final com o cifrão
    print(f"${result}")

def value(greeting):
    # Converte para minúsculas e remove espaços extras para facilitar a comparação
    greeting = greeting.lower().strip()

    # Verifica as condições em ordem de prioridade
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
