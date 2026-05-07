import sys
import csv
from tabulate import tabulate

def main():
    # 1. Validação de argumentos (mesma lógica do exercício anterior)
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # 2. Validação da extensão .csv
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # 3. Leitura e formatação
    try:
        with open(filename, "r") as file:
            # Usamos DictReader para capturar o cabeçalho automaticamente
            reader = csv.DictReader(file)

            # tabulate pode receber uma lista de dicionários diretamente
            # O parâmetro tablefmt="grid" gera a arte ASCII solicitada
            print(tabulate(reader, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
