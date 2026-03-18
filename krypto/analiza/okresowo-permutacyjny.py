from collections import Counter

def upload_files(plik):
    with open(plik, "r") as file:
        text = file.read().strip().upper()
    return text

def periodic_permutation(text, max_period=10):
    # Lista przechowująca długości okresów, które wykazują powtarzalność
    pos_periods = []

    # Przechodzimy przez możliwe długości okresu od 2 do max_period
    # Zaczyna się od 2, ponieważ nie ma sensu sprawdzanie okresowości dla 1 znaku
    for period in range(2, max_period + 1):
        blocks = [text[i:i + period] for i in range(0, len(text), period)]

        # Odrzuca ostatni blok, gdy jest niepełny
        if len(blocks[-1]) != period:
            blocks = blocks[:-1]

        # Zlicza częstotliwości znaków w bloku
        patterns = [Counter(block) for block in blocks]

        # Sprawdza, czy wzorce w blokach się powtarzają
        if all(pat == patterns[0] for pat in patterns):
            pos_periods.append(period)

    if len(pos_periods) > 0:
        print(f"Prawda dla okresów: {pos_periods}")
    else:
        print("Nie może być okresowo permutacyjny.")


text = upload_files("szyfr1.txt")
result = periodic_permutation(text, 84)
