import sys

def main():
    # 1. Validar a quantidade de argumentos
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # 2. Validar a extensão do arquivo
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # 3. Tentar abrir o arquivo e contar as linhas
    try:
        count = 0
        with open(filename, "r") as file:
            for line in file:
                if is_code_line(line):
                    count += 1
        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")

def is_code_line(line):
    """
    Verifica se uma linha deve ser contada como código.
    Retorna False se for apenas espaço em branco ou comentário (#).
    """
    # Remove espaços em branco do início (lstrip) para facilitar a checagem
    stripped_line = line.lstrip()

    # Se a linha estiver vazia após o strip, era apenas espaço em branco
    if not stripped_line:
        return False

    # Se começar com #, é um comentário
    if stripped_line.startswith("#"):
        return False

    return True

if __name__ == "__main__":
    main()
