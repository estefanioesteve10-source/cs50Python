def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x_str, y_str = fraction.split("/")

    # Se não forem inteiros, o int() vai gerar ValueError naturalmente
    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if x < 0:
        raise ValueError

    # Calcula e arredonda
    return int(round((x / y) * 100))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
