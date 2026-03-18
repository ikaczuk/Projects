def lfsr(seed, taps, length):
    register = seed.copy()
    output = []
    for _ in range(length):
        new_bit = sum(register[tap] for tap in taps) % 2
        output.append(register[-1])
        register = [new_bit] + register[:-1]
    return output

def xor_str(str1, str2):
    result = []
    for b1, b2 in zip(str1, str2):
        xor_result = b1^b2
        result.append(xor_result)
    return result

#1.dane
seed = [1, 1, 0, 0, 1, 1]
wsp = [5, 4, 0]  #współczynniki
period = 2 ** len(seed) - 1
str_len = 3 * period
#ciąg pseudolosowy
key_str = lfsr(seed, wsp, str_len)
#okres
key_str_tup = [tuple(key_str[i:i+len(seed)]) for i in range(len(key_str) - len(seed) + 1)]
period_len = len(set(key_str_tup))
print("Klucz pseudolosowy: ", key_str[:20])
print("Okres: ", period_len)


#2.generowanie info
plain = [1] * len(seed) #same jedynki


#3.szyfrowanie i deszyfrowanie
cip_txt = xor_str(plain, key_str[:len(plain)])
dec = xor_str(cip_txt, key_str[:len(plain)])
print("Szyfrowana wiadomość: ", cip_txt)
print("Odszyfrowana wiadomość: ", dec)


#4.wprowadzenie błędu
cip_error = cip_txt.copy()
cip_error[3] ^= 1 #zamienia bit: z 1 na 0, z 0 na 1
dec_error = xor_str(cip_error, key_str[:len(plain)])
print("Odszyfrowana z błędem: ", dec_error)


#5.przesunięcie bitu
cip_shift = cip_txt[1:] + [cip_txt[0]]
dec_shift = xor_str(cip_shift, key_str[:len(plain)])
print("Odszyfrowana z przesunięciem: ", dec_shift)
