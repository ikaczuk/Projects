import random
from sympy import nextprime

# Definicja listy znaków z indeksami
characters = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]
message = "Pieniądze są zakopane pod starą jabłonią w ogrodzie"

# Zamiana zdania na listę indeksów
indices = [characters.index(char.lower()) for char in message]

# Znalezienie odpowiedniego ciała skończonego
max_index = max(indices)
p = nextprime(max_index + 1)

# Definicja wielomianu w ciele skończonym
def polynomial(x, coefficients, p):
    return sum(coeff * pow(x, i, p) % p for i, coeff in enumerate(coefficients)) % p

# Generowanie losowych współczynników dla wielomianu
def generate_coefficients(secret, degree, p):
    coefficients = [secret]  # v_0 = secret
    coefficients.extend(random.randint(0, p-1) for _ in range(degree - 1))
    return coefficients

# Przykład użycia
degree = len(indices)
secret = indices[0]  # Dla uproszczenia tajemnica to pierwszy indeks
coefficients = generate_coefficients(secret, degree, p)

# Obliczenie wartości wielomianu w punktach
polynomial_values = [polynomial(i, coefficients, p) % len(characters) for i in range(len(message))]

# Zamiana wartości wielomianu na znaki
decoded_message = ''.join([characters[value] for value in polynomial_values])
print(f"Odkodowane zdanie: {decoded_message}")
print(f"Użyte ciało skończone: GF({p})")
