import validators

def main():
    # Solicita o e-mail ao usuário
    email = input("What's your email address? ")
    
    # Valida e imprime o resultado
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(s):
    # A função validators.email(s) retorna True se for válido
    # ou um objeto de erro (ValidationFailure) se for inválido.
    if validators.email(s):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
