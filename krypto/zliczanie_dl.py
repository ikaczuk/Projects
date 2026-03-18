alphabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]
numerical = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]

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

def numbers_to_string(numbers, alphabet, numerical):
    secret = ""
    for char in numbers:
        if char != "00":
            nr = numerical.index(char)
            symbol = alphabet[nr]
            secret += symbol
        else:
            secret += "#"
    return secret

text = "Pieniądze"
cyphered = string_to_numbers(text, alphabet, numerical)
print(cyphered)
print(numbers_to_string(cyphered, alphabet, numerical))