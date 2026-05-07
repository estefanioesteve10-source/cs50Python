import sys
import csv

def main():
    # 1. Verificar a quantidade de argumentos na linha de comando
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Lista para armazenar os dados processados
        students = []

        # 2. Abrir e ler o arquivo de entrada
        with open(input_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # O formato em 'name' é "Sobrenome, Nome"
                # Usamos split(", ") para separar os dois
                last, first = row["name"].split(", ")

                # Adicionar à lista no novo formato
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # 3. Escrever os dados no arquivo de saída
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Escreve o cabeçalho (first, last, house)
            writer.writeheader()
            # Escreve as linhas processadas
            writer.writerows(students)

    except IOError:
        sys.exit(f"Could not write to {output_file}")

if __name__ == "__main__":
    main()
