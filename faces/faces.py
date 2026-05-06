# faces.py

def convert(texto):

    texto = texto.replace(":)", "🙂")

    texto = texto.replace(":(", "🙁")
    return texto

def main():

    frase = input()


    resultado = convert(frase)


    print(resultado)


if __name__ == "__main__":
    main()
