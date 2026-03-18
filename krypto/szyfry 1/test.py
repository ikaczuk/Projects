plik = open("plain.txt", "r")
plik1 = open("substitute_proprietary.txt", "r")
plik2 = open("substitute_encoded.txt", "w")
tekst = plik.read()
szyfr = plik1.read()

k = 1 #klucz przesunięcia
alfabet = "abcdefghijklmnopqrstuvwxyz"

def szyfrowanie(tekst, k):
    szyfr = ""
    for i in range(len(tekst)):
        Flaga = False
        znak = tekst[i]

        if znak.isalpha():
            if znak.isupper():
                znak = znak.lower()
                Flaga = True

            index = alfabet.find(znak)
            nowyIndex = index + k

            if nowyIndex > 25:
                nowyIndex -= 26

            litera = alfabet[nowyIndex]

            if Flaga:
                litera = litera.upper()

        else:
            litera = znak

        szyfr += litera

    #plik1.write(szyfr)
    print(szyfr)




def odszyfrowywanie(szyfr, k):
    wiadomosc = ""

    for i in range(len(szyfr)):
        Flaga = False
        znak = szyfr[i]

        if znak.isalpha():
            if znak.isupper():
                znak = znak.lower()
                Flaga = True

            index = alfabet.find(znak)
            nowyIndex = index - k

            if nowyIndex < 0:
                nowyIndex += 26

            litera = alfabet[nowyIndex]

            if Flaga:
                litera = litera.upper()

        else:
            litera = znak

        wiadomosc += litera
    #plik2.write(wiadomosc)
    print(wiadomosc)





szyfrowanie(tekst, k)
print()
odszyfrowywanie(szyfr, k)

plik.close()
plik1.close()
plik2.close()