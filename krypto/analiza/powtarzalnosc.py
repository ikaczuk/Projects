from collections import Counter

def upload_files(plik):
    with open(plik, "r") as file:
        text = file.read().strip().upper()
    return text

def analyze_frequency(text):
    text = text.upper()  # Zamiana tekstu na duże litery
    letters = [char for char in text if char.isalpha()]  # Filtracja tylko liter
    total_letters = len(letters)
    frequency = Counter(letters)

    hash = text.count("#")

    for letter, count in frequency.items():
        percent = (count / len(text)) * 100 #obliczanie procentowej iloci wystąpień danej litery
        print(f"Litera '{letter}': {count} wystąpień, {percent:.2f}%")  #wyświetlanie litery, jej ilości wystąpień oraz procentowej ilości wystąpień(do dwóch miejsc po przecinku)

    percent = (hash / len(text)) * 100
    print(f"Znak '#': {hash} wystąpień, {percent: .2f}%")



text = upload_files("szyfr1.txt")
text1 = upload_files("szyfr2.txt")
#analyze_frequency(text)
# analyze_frequency(text1)

t = upload_files("kp.txt")
analyze_frequency(t)