import random

#funkcja "generator_referencji" tworzy ciąg liczb
# ilość liczb w ciągu jest określona przez zmienną "ilosc_referencji"
#natomiast ilość stron jest określona przez zmienną "ilosc_stron"
def generator_referencji(ilosc_referencji, ilosc_stron):
    referencje = []
    for i in range(0, ilosc_referencji):
        ref = random.randint(1, ilosc_stron)    #generuje liczbę z zakresu od 1 do ilosc_stron
        referencje.append(ref)                  #dodaje wygenerowanną liczbę do tablicy "referencje"
    return referencje