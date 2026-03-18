import numpy as np

def lfsr(seed, wsp, length):
    register = seed.copy()
    n = len(seed)
    output = []

    for _ in range(length):
        new_bit = sum(register[t] for t in wsp) % 2
        output.append(register[-1])
        register = [new_bit] + register[:-1]

    return output

def xor_str(stream1, stream2):
    result = []
    for b1, b2 in zip(stream1, stream2):
        xor_result = b1 ^ b2
        result.append(xor_result)
    return result


seed = [1, 0, 0, 1, 1]
wsp = [4, 2]  # Współczynniki
period = (2**len(seed)) - 1

# Generowanie str pseudolosowego
key = lfsr(seed, wsp, length=period*3)
text = [1] * len(key)
cipher = xor_str(text, key)
recovery = xor_str(cipher, key)


print("Jawny:           ", text)
print("Szyfrogram:      ", cipher)
print("Odszyfrowany:    ", recovery)

cipher[9] = 0
altered = xor_str(cipher, key)
print("Po błędzie bitu: ", altered)