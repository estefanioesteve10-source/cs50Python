import emoji

def main():
    # Solicita a entrada do usuário
    user_input = input("Input: ")

    # Converte códigos e aliases em emojis
    # O parâmetro language='alias' é crucial para aceitar códigos como :thumbsup:
    output = emoji.emojize(user_input, language='alias')

    # Exibe o resultado
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
