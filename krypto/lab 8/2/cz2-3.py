import random
from sympy import nextprime, mod_inverse

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

# Funkcja do odwzorowania wartości wielomianu na współczynniki
def reverse_polynomial(polynomial_values, x, p):
    n = len(x)
    coefficients = [0] * n
    for i in range(n):
        xi = x[i]
        yi = polynomial_values[i]
        basis_poly = 1
        for j in range(n):
            if i != j:
                xj = x[j]
                basis_poly *= (xi - xj) % p
        # Obliczanie odwrotności modulo
        inv_basis_poly = mod_inverse(basis_poly, p)
        coefficients[i] = (yi * inv_basis_poly) % p
    return coefficients

# Odtworzenie współczynników
x = list(range(len(polynomial_values)))
recovered_coefficients = reverse_polynomial(polynomial_values, x, p)

# Odtworzenie tajemnicy (v_0)
recovered_secret = recovered_coefficients[0]
print(f"Odtworzony sekret (indeks): {recovered_secret}")
print(f"Odtworzony sekret (znak): {characters[recovered_secret]}")
