import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    birth_date_str = input("Date of Birth: ")
    try:
        # Tenta validar e converter a string para um objeto date
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        sys.exit("Invalid date")

    # Calcula a diferença em minutos
    today = date.today()
    minutes = calculate_minutes(birth_date, today)

    # Converte o número para palavras
    words = minutes_to_words(minutes)
    print(words)

def calculate_minutes(start_date, end_date):
    """Calcula a diferença em minutos entre duas datas."""
    delta = end_date - start_date
    # delta.days nos dá o número total de dias
    return delta.days * 24 * 60

def minutes_to_words(minutes):
    """Converte o inteiro de minutos para extenso em inglês."""
    # Convertemos para palavras e removemos o "and" conforme solicitado
    words = p.number_to_words(minutes, wantlist=False)
    words = words.replace(" and", "")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
