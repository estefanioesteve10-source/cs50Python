import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    # Loop infinito para coletar nomes
    while True:
        try:
            # Solicita o nome ao usuário
            line = input("Name: ")
            names.append(line)
        except EOFError:
            # Captura o Ctrl+D (End of File)
            print() # Pula uma linha após o Ctrl+D para manter a formatação
            break

    # Formata a lista usando o método join do inflect
    # O método join lida automaticamente com 1, 2 ou n nomes
    output = p.join(names)

    # Exibe o resultado final
    print(f"Adieu, adieu, to {output}")

if __name__ == "__main__":
    main()
