# Ścieżka do pliku z danymi
plik_ze_znakami = "a"

# Odczyt znaków z pliku i konwersja na ASCII
def zamien_znaki_na_ascii(sciezka_pliku):
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as plik:
            znaki = plik.read().splitlines()  # Wczytaj linie jako listę
        # Zamień znaki na kody ASCII
        wynik = {znak: ord(znak) for znak in znaki}
        return wynik
    except FileNotFoundError:
        return "Plik nie istnieje!"
    except Exception as e:
        return f"Wystąpił błąd: {e}"

# Wywołanie funkcji i zapis wyników
wyniki = zamien_znaki_na_ascii(plik_ze_znakami)

# Wyświetlenie wyników
if isinstance(wyniki, dict):
    for znak, kod in wyniki.items():
        #print(f"Znak: '{znak}' ma kod ASCII: {kod}")
        print(kod)
else:
    print(wyniki)
