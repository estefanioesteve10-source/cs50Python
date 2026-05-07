import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. Verificar o número de argumentos
    check_arguments()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # 2. Verificar extensões e se são iguais
    check_extensions(input_path, output_path)

    # 3. Processar a imagem
    try:
        # Abrir a camisa (shirt.png)
        shirt = Image.open("shirt.png")
        size = shirt.size

        # Abrir a foto de entrada
        with Image.open(input_path) as photo:
            # Redimensionar e recortar a foto para o tamanho da camisa
            # ImageOps.fit faz o "crop" automático para preencher o tamanho
            photo_fitted = ImageOps.fit(photo, size)

            # Sobrepor a camisa na foto
            # O segundo argumento 'shirt' serve como máscara para transparência
            photo_fitted.paste(shirt, shirt)

            # Salvar o resultado
            photo_fitted.save(output_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_arguments():
    """Verifica se existem exatamente 2 argumentos."""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_extensions(in_file, out_file):
    """Verifica extensões válidas e compatibilidade entre elas."""
    valid_extensions = [".jpg", ".jpeg", ".png"]

    # Extrair extensões e converter para minúsculas
    ext1 = os.path.splitext(in_file)[1].lower()
    ext2 = os.path.splitext(out_file)[1].lower()

    if ext1 not in valid_extensions:
        sys.exit("Invalid input")
    if ext2 not in valid_extensions:
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
