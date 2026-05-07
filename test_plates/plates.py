def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # 1. Comprimento: Mínimo 2, Máximo 6
    if len(s) < 2 or len(s) > 6:
        return False

    # 2. Início: Deve começar com pelo menos duas letras
    if not s[0:2].isalpha():
        return False

    # 3. Pontuação: Apenas letras e números são permitidos
    if not s.isalnum():
        return False

    # 4. Regras numéricas
    for i in range(len(s)):
        if s[i].isdigit():
            # O primeiro número não pode ser '0'
            if s[i] == "0":
                return False

            # Uma vez que um número aparece, tudo depois dele deve ser número
            # (Não pode haver letras após um número)
            if not s[i:].isdigit():
                return False

            # Se passou pelos checks acima, paramos o loop porque o resto já foi validado
            break

    return True

if __name__ == "__main__":
    main()
