import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Regex explicada:
    # \\b -> Limite de palavra (garante que não seja parte de outra palavra)
    # um -> A string que procuramos
    # \\b -> Outro limite de palavra
    # re.IGNORECASE -> Ignora se é maiúscula ou minúscula
    find_um = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(find_um)

if __name__ == "__main__":
    main()
