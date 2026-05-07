def main():
    # Solicita a entrada do usuário
    text = input("Input: ")
    # Chama a função shorten e imprime o resultado
    print(f"Output: {shorten(text)}")

def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    # Itera sobre cada caractere da palavra
    for char in word:
        # Se o caractere não for uma vogal, adiciona ao resultado
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
