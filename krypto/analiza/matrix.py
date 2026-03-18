from collections import Counter

def upload_files(plik):
    with open(plik, "r") as file:
        text = file.read().strip().upper()
    return text

def fill_grid(text, a=28, b=30):
    # Tworzy pustą tablicę axb
    grid = [[" " for _ in range(a)] for _ in range(b)]

    index = 0

    # Przechodzi przez wiersze(row) i kolumny(col)
    for row in range(b):
        for col in range(a):
            # Sprawdza, czy wciąż są znaki do zapisania
            if index < len(text):
                grid[row][col] = text[index]
                index += 1
            else:
                break
    return grid

def check_for_letters(grid, word="CRYPTOGRAPHY"):
    # Zlicza wymagane litery w słowie
    required_letters = Counter(word)

    # Przechodzi przez każdy wiersz w macierzy
    for row_index, row in enumerate(grid):
        # Tworzy licznik dla liter w danym wierszu
        row_counter = Counter(row)

        # Sprawdza, czy każdy wymagany znak występuje przynajmniej tyle razy, ile potrzeba
        if all(row_counter[char] >= required_letters[char] for char in required_letters):
            print(f"Wiersz {row_index + 1} zawiera wszystkie litery do stworzenia słowa '{word}':")
            print("".join(row))
            return True

    print(f"Żaden wiersz nie zawiera wszystkich liter potrzebnych do stworzenia słowa '{word}'.")
    return False


text = upload_files("szyfr1.txt")
grid = fill_grid(text, 10, 84)

# Wypisuje macierz
for row in grid:
    print(" ".join(row))

check_for_letters(grid)