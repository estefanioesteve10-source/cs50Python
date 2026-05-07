import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regex explicada:
    # src=" -> procura o início do atributo
    # https?:// -> procura http ou https
    # (?:www\.)? -> grupo que não captura, procura 'www.' opcional
    # youtube\.com/embed/ -> procura o domínio e a pasta obrigatória
    # ([a-zA-Z0-9_-]+) -> GRUPO 1: captura o ID do vídeo (letras, números, traços e underscores)
    # " -> termina a captura quando encontra a aspa de fechamento

    regex = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'

    if matches := re.search(regex, s):
        # Retorna o formato curto usando o ID capturado no grupo 1
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
