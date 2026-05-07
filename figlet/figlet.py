import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    # 1. Validar argumentos da linha de comando
    if len(sys.argv) == 1:
        # Escolhe uma fonte aleatória se não houver argumentos
        selected_font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # Verifica se a fonte solicitada existe
        selected_font = sys.argv[2]
        if selected_font not in available_fonts:
            sys.exit("Invalid usage")
    else:
        # Qualquer outra combinação de argumentos é inválida
        sys.exit("Invalid usage")

    # 2. Configurar a fonte no objeto Figlet
    figlet.setFont(font=selected_font)

    # 3. Solicitar texto ao usuário
    user_input = input("Input: ")

    # 4. Exibir o resultado formatado
    print("Output:")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
