import random


def char_to_bin_utf8(char):
    return ''.join([bin(byte)[2:].zfill(8) for byte in char.encode('utf-8')])


def bin_to_char_utf8(bin_str):
    bytes_list = [int(bin_str[i:i + 8], 2) for i in range(0, len(bin_str), 8)]
    return bytes(bytearray(bytes_list)).decode('utf-8')


def split_secret(secret):
    secret_bin = ''.join([char_to_bin_utf8(c) for c in secret])
    n = len(secret_bin)

    shadow1 = ''.join([str(random.randint(0, 1)) for _ in range(n)])
    shadow2 = ''.join([str(random.randint(0, 1)) for _ in range(n)])

    shadow3 = ''.join(['1' if shadow1[i] != shadow2[i] else '0' for i in range(n)])

    return shadow1, shadow2, shadow3


def combine_shadows(shadow1, shadow2, shadow3):
    n = len(shadow1)
    secret_bin = ''.join(['1' if shadow1[i] != shadow2[i] != shadow3[i] else '0' for i in range(n)])
    secret = ''.join([bin_to_char_utf8(secret_bin[i:i + 8]) for i in range(0, len(secret_bin), 8)])

    return secret


secret = "Pieniądze są zakopane pod starą jabłonią w ogrodzie"
shadow1, shadow2, shadow3 = split_secret(secret)

print("Shadow 1:", shadow1)
print("Shadow 2:", shadow2)
print("Shadow 3:", shadow3)

combined_secret = combine_shadows(shadow1, shadow2, shadow3)
print("Recovered Secret:", combined_secret)