import random
import functools

alphabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]
numerical = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]
prime = 2**127 - 1
rand_int = functools.partial(random.SystemRandom().randint, 0)

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

def eval(poly, x, prime):
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def generate_shares(secret, minimum, shares, prime=prime):
    if minimum > shares:
        raise ValueError("Potrzeba więcej fragmentów, aby móc odtworzyć hasło")
    poly = [secret] + [rand_int(prime - 1) for _ in range(minimum - 1)]
    points = [(i, eval(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

def extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        c = a // b
        a, b = b, a % b
        x, last_x = last_x - c * x, x
        y, last_y = last_y - c * y, y
    return last_x, last_y

def divmod(num, den, p):
    inv, _ = extended_gcd(den, p)
    return num * inv

def lagrange_interpolate(x, x_s, y_s, p):
    k = len(x_s)
    assert k == len(set(x_s)), "muszą być różne"
    def PI(vals):
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []
    dens = []

    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))

    den = PI(dens)
    num = sum([divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])

    return (divmod(num, den, p) + p) % p

def recover_secret(shares, prime=prime):
    if len(shares) < 3:
        raise ValueError("Potrzeba przynajmniej 3 fragmentów")
    x_s, y_s = zip(*shares)
    return lagrange_interpolate(0, x_s, y_s, prime)

text = "Pieniądze są zakopane pod starą jabłonią w ogrodzie"

numerical_representation = string_to_numbers(text, alphabet, numerical)
print("Wartości numeryczne:", numerical_representation)

secret = int(''.join(map(str, numerical_representation))) % prime
shares = generate_shares(secret, minimum=3, shares=5)

print('Hasło: ', secret)
print('Shares:')
if shares:
    for share in shares:
        print('  ', share)

recovered = recover_secret(shares[:3])
print('\nOdtworzone:', recovered)

#print('\nHasło to: ', numbers_to_string(str(recovered), alphabet, numerical))
