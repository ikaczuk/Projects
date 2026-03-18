import matplotlib.pyplot as plt

# Funkcja do wczytywania danych z pliku
def wczytaj_dane_z_pliku(nazwa_pliku):
    characters = []
    values = []
    with open(nazwa_pliku, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split()
            values.append(int(parts[0])-160000)
            characters.append(parts[1])
    return characters, values

# Wczytanie danych z pliku
nazwa_pliku = 'largefile.txt'
characters, values = wczytaj_dane_z_pliku(nazwa_pliku)

# Tworzenie wykresu słupkowego
plt.figure(figsize=(15, 10))
plt.bar(characters, values, color='skyblue')
plt.xlabel('Znaki')
plt.ylabel('Wartości')
plt.title('Wykres słupkowy wartości dla każdego znaku')
plt.xticks(rotation=90)
plt.show()
