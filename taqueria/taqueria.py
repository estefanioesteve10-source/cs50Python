def main():
    # Cardápio fornecido pelo exercício
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            # Solicita o item ao usuário
            item = input("Item: ").title()

            # Verifica se o item existe no dicionário
            if item in menu:
                total_cost += menu[item]
                # Exibe o total formatado com 2 casas decimais
                print(f"Total: ${total_cost:.2f}")

        except EOFError:
            # Quando o usuário pressiona Ctrl+D, encerra o loop
            # Imprime uma nova linha para organizar o terminal
            print()
            break
        except KeyError:
            # Caso ocorra um erro de chave (embora o 'if' acima já previna isso)
            pass

if __name__ == "__main__":
    main()
