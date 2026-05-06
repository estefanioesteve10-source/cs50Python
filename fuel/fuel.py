def main():
    percentage = get_fuel_percentage()

    # Lógica para exibir E, F ou a porcentagem
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_fuel_percentage():
    while True:
        fraction = input("Fraction: ")
        try:
            # Divide a string em X e Y usando a barra "/"
            x_str, y_str = fraction.split("/")

            # Converte para inteiros
            x = int(x_str)
            y = int(y_str)

            # Verifica se X é maior que Y ou se Y é zero
            # Se X > Y, não é uma fração de tanque válida (mais de 100%)
            if x > y or x < 0:
                continue

            # Cálculo da porcentagem arredondada
            # O round() lida com o arredondamento para o inteiro mais próximo
            result = (x / y) * 100
            return int(round(result))

        except (ValueError, ZeroDivisionError):
            # Se não for número ou se dividir por zero, o loop recomeça
            pass

if __name__ == "__main__":
    main()
