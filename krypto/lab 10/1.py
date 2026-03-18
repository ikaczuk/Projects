import numpy as np

def lfsr(seed, taps, length):
    register = seed[:]
    output = []

    for i in range(length):
        new_bit = sum(register[tap] for tap in taps) % 2
        output.append(register[-1])
        register = [new_bit] + register[:-1]
    return output

def xor_str(stream1, stream2):
    result = []
    for b1, b2 in zip(stream1, stream2):
        xor_result = b1 ^ b2
        result.append(xor_result)
    return result


# 1. Parametry generatora
seed = [1, 1, 0, 0, 1, 1]
taps = [5, 4, 0]  # x^6 + x^5 + 1
period = 2 ** len(seed) - 1
stream_length = 3 * period

# Generowanie ciągu pseudolosowego
key_str = lfsr(seed, taps, stream_length)

key_str_tup = []
for i in range(len(key_str) - len(seed)):
    tuple_slice = tuple(key_str[i:i+len(seed)])
    key_str_tup.append(tuple_slice)

unique_tuples = np.unique(key_str_tup)
period_length = len(unique_tuples)

print("klucz pseudolosowy: ", key_str[:20])
print("kkres: ", period_length)

# 2. Generowanie informacji użytecznej
plain = [1] * len(seed)  # Ciąg jedynek o długości równej długości klucza

# 3. Szyfrowanie i deszyfrowanie
cipher_text = xor_str(plain, key_str[:len(plain)])
decrypted = xor_str(cipher_text, key_str[:len(plain)])

print("Szyfrowana wiadomość: ", cipher_text)
print("Odszyfrowana wiadomość: ", decrypted)

# 4. Wprowadzenie błędu w jednym bicie szyfrogramu
error_ind = 3  # Indeks błędu
cipher_error = cipher_text[:]
cipher_error[error_ind] ^= 1  # Zamiana bitu na przeciwny

# Deszyfrowanie z błędem
decrypted_error = xor_str(cipher_error, key_str[:len(plain)])
print("odszyfrowana z błędem: ", decrypted_error)

# 5. Przesunięcie bitu w szyfrogramie
cipher_text_with_shift = cipher_text[1:] + [cipher_text[0]]  # Przesunięcie bitu
decrypted_shift = xor_str(cipher_text_with_shift, key_str[:len(plain)])
print("odszyfrowana z przesunięciem: ", decrypted_shift)
