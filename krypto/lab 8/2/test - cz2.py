import random
from sympy import symbols, Eq, solve, mod_inverse

def string_to_numbers(text, alphabet):
    return [alphabet.index(char.lower()) for char in text]

def numbers_to_string(numbers, alphabet):
    return ''.join([alphabet[num] for num in numbers])

def evaluate_polynomial(coeffs, x, p):
    return sum(c * (x ** i) for i, c in enumerate(coeffs)) % p

def generate_shares(secret, threshold, num_shares, field_size):
    coeffs = [secret] + [random.randint(0, field_size - 1) for _ in range(threshold - 1)]
    shares = [(x, evaluate_polynomial(coeffs, x, field_size)) for x in range(1, num_shares + 1)]
    return shares, coeffs

def reconstruct_secret(shares, field_size):
    x_values, y_values = zip(*shares)
    secret = 0
    for i in range(len(shares)):
        xi, yi = x_values[i], y_values[i]
        li = 1
        for j in range(len(shares)):
            if i != j:
                xj = x_values[j]
                li *= (0 - xj) * mod_inverse(xi - xj, field_size)
                li %= field_size
        secret += yi * li
        secret %= field_size
    return secret

def simulate_error_in_share(shares, bit_position):
    share_index = random.randint(0, len(shares) - 1)
    x, y = shares[share_index]
    y ^= (1 << bit_position)  # Flip a single bit in the y-value
    shares[share_index] = (x, y)
    return shares

# Define the sentence and alphabet
sentence = "Pieniądze są zakopane pod starą jabłonią w ogrodzie"
alphabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]

# Convert sentence to numerical representation
numerical_representation = string_to_numbers(sentence, alphabet)
print("Numerical Representation:", numerical_representation)

# Combine numbers into a single integer (secret)
secret = int(''.join(map(str, numerical_representation))) % 97  # Use a small field size for simplicity
print("Secret (M):", secret)

# Generate shares
threshold = 3
num_shares = 5
field_size = 97
shares, coeffs = generate_shares(secret, threshold, num_shares, field_size)
print("Shares:", shares)
print("Polynomial Coefficients:", coeffs)

selected_shares = shares[:threshold]
recovered_secret = reconstruct_secret(selected_shares, field_size)
print("Recovered Secret:", recovered_secret)