a = str(input("podaj plik do zaszyfrowania: "))
b = str(input("podaj plik do odszyfrowania: "))

plik = open(a, "r")
plik1 = open(b, "r")

tekst = plik.read()
szyfr = plik1.read()

k = 1 #klucz przesunięcia
alfabet = "abcdefghijklmnopqrstuvwxyz"

def uploading_files(text, plik):
    with open(plik, 'w') as f:
        text = f.read()


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
    return szyfr




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
    return wiadomosc





szyfrowanie(tekst, k)
print()
odszyfrowywanie(szyfr, k)

# uploading_files(plik1, szyfr)
# uploading_files(plik2, wiadomosc)



plik.close()
plik1.close()
#plik2.close()
