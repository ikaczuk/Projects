def upload_files(plik):
    with open(plik, "r") as file:
        text = file.read().strip().upper()
    return text

def write_in_file(plik, wartosc):
    # Zapisuję wynik funkcji do pliku
    with open(plik, "w") as f:
        f.write(wartosc)  # Zapis do pliku


def create_matrix(text, cols=95, rows=18):
    text = text.replace("\n", "") # Pozbywam się odstępów w tekście
    text = text.replace(" ", "")

    # Sprawdza, czy tekst jest wystarczająco krótki by wypełnić macierz
    if len(text) < cols * rows:
        raise ValueError("Ten tekst jest zbyt krótki, aby wypełnić całą macierz!!")

    # Tworzy macierz
    matrix = [list(text[i * cols: (i + 1) * cols]) for i in range(rows)]

    return matrix



def encryption(matrix, col=95, row=18):
    zaszyfrowane = ""

    # Wypisuję wszystkie kolumny po kolei
    for i in range(col):
        for j in range(row):
            zaszyfrowane += matrix[j][i]

    return zaszyfrowane


def decryption(text, rows=18):
    # Dzielimy tekst na wiersze o określonej długości
    wiersze = [list(text[i: i + rows]) for i in range(0, len(text), rows)]

    # Odwracam tablicę, zamieniając wiersze na kolumny
    kolumny = list(zip(*wiersze))

    # Zwracam listę kolumn
    odszyfrowane = [list(kolumna) for kolumna in kolumny]

    string_convert = ''
    for i in range(len(odszyfrowane)):
        for j in range(len(odszyfrowane[i])):
            string_convert += odszyfrowane[i][j]

    return string_convert








ed = str(input("Wpisz d jeśli chcesz odszyfrować tekst, a e jeśli chcesz zaszyfrować: "))

if ed == "e":
    plik = str(input("podaj nazwę i rozszerzenie pliku z tekstem do zaszyfrowania: "))
    text = upload_files(plik)
    matrix = create_matrix(text)
    encrypted = encryption(matrix)
    write_in_file("shuffle_propriertary.txt", encrypted)

elif ed == "d":
    plik = str(input("podaj nazwę i rozszerzenie pliku z tekstem do odszyfrowania: "))
    # Nie ma potrzeby tworzenia macierzy, ponieważ funkcja decryption wykorzystuje tekst ciągły zamiast listy
    text = upload_files(plik)
    decrypted = decryption(text)
    write_in_file("decrypted_text.txt", decrypted)

else:
    print("Nie rozumiem polecenia: ", ed, "\nPowinieneś podać literkę e lub d!!!")