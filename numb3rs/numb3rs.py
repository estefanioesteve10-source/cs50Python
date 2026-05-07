
import re
import sys

def main():
    # Certifique-se de que 'print' esteja alinhado aqui
    print(validate(input("IPv4 Address: ")))

def validate(ip):
         # O bloco abaixo deve estar exatamente com 4 espaços de recuo
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
            # Este 'for' tem 8 espaços de recuo (4 da função + 4 do if)
        for group in matches.groups():
            if not (0 <= int(group) <= 255):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
