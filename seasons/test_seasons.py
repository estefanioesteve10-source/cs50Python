import pytest
from datetime import date
from seasons import calculate_minutes, minutes_to_words

def test_calculate_minutes():
    # 2001 a 2002 NÃO é bissexto (365 dias)
    assert calculate_minutes(date(2001, 1, 1), date(2002, 1, 1)) == 525600

    # 2000 a 2001 É bissexto (366 dias)
    assert calculate_minutes(date(2000, 1, 1), date(2001, 1, 1)) == 527040

    # Um dia comum
    assert calculate_minutes(date(2023, 1, 1), date(2023, 1, 2)) == 1440

def test_minutes_to_words():
    # Testando a formatação das palavras (sem o "and")
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
