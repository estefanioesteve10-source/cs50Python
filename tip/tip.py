def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove o '$' inicial e converte o restante para float
    # O fatiamento [1:] pega do segundo caractere em diante
    d_sem_cifrao = d.replace("$", "")
    return float(d_sem_cifrao)


def percent_to_float(p):
    # Remove o '%' final e converte para float
    p_sem_porcento = p.replace("%", "")
    # Divide por 100 para transformar, por exemplo, 15.0 em 0.15
    return float(p_sem_porcento) / 100


if __name__ == "__main__":
    main()
