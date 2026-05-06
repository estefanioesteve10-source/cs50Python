def main():
    grocery_list = {}

    while True:
        try:
            # Solicita o item e converte para maiúsculas imediatamente
            item = input().strip().upper()

            # Se o item já estiver no dicionário, incrementa a contagem
            if item in grocery_list:
                grocery_list[item] += 1
            # Se for a primeira vez que o item aparece, define como 1
            else:
                grocery_list[item] = 1

        except EOFError:
            # Pula uma linha para o terminal ficar limpo
            print()

            # Ordena as chaves do dicionário em ordem alfabética
            # O sorted() retorna uma lista com as chaves "A-Z"
            for item in sorted(grocery_list.keys()):
                count = grocery_list[item]
                print(f"{count} {item}")

            # Encerra o programa
            break

if __name__ == "__main__":
    main()
