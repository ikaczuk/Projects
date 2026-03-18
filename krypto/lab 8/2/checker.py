alphabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]
numerical = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]
prime = 2**127 - 1
def string_to_numbers(text, alphabet, numerical):
    numbers = []
    for char in text:
        if char.lower() in alphabet:
            nr = alphabet.index(char.lower())
            symbol = numerical[nr]
            numbers.append(symbol)
        else:
            symbol = "00"
            numbers.append(symbol)
    return numbers


def secret_to_text(secret, alphabet, numerical):
    # Konwertujemy liczbę `secret` z powrotem na ciąg cyfr
    numerical_string = str(secret)

    # Rozbijamy ciąg cyfr na dwucyfrowe bloki (zgodne z `numerical`)
    numerical_representation = [
        numerical_string[i:i + 2] for i in range(0, len(numerical_string), 2)
    ]

    # Odtwarzamy oryginalny tekst na podstawie bloków numerycznych
    text = []
    for num in numerical_representation:
        if num in numerical:
            index = numerical.index(num)
            text.append(alphabet[index])
        else:
            text.append("?")  # Dla nieznanych symboli
    return ''.join(text)

text = "Pieniądze są zakopane pod starą jabłonią w ogrodzie"

numerical_representation = string_to_numbers(text, alphabet, numerical)
print("Wartości numeryczne:", numerical_representation)

secret = int(''.join(map(str, numerical_representation))) % prime
print(secret)

original_text = secret_to_text(secret, alphabet, numerical)
print("Odtworzony tekst:", original_text)

original_text = secret_to_text(secret, alphabet, numerical)
print("Odtworzony tekst:", original_text)