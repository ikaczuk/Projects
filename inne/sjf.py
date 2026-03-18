from systemy.generatory.referencje import generator_referencji



def LRU(referencje, n):
    # tablica "replace" służy do przechowywania ostatnio użytych stron
    # zmienne "pierwszy", "drugi" i "trzeci" przechowują trzy ostatnio otwarte strony
    # zmienna "n" oznacza liczbę ramek
    #replace = []
    blad = 1
    bledy_zbior = []

    bledy_zbior.append(blad)
    ramka = []
    for a in range(n-1):
        ramka.append(0)
    ramka.append(referencje[0])



    for i in range(1, len(referencje)):
        pomocnicza = referencje[i]

        # sprawdzenie, czy któraś z ostatnio otwartych stron zostaje ponownie otwarta
        if pomocnicza in ramka:
            for j in range(n):
                if pomocnicza == ramka[j]:
            bledy_zbior.append(blad)
            continue
        elif drugi == pomocnicza:
            pierwszy, drugi = drugi, pierwszy
        elif trzeci == pomocnicza:
            pierwszy, drugi, trzeci = trzeci, pierwszy, drugi

        # jeżeli żadna ze stron nie zostaje ponownie otwarta, to ostatnia używana zostaje zamknięta
        # zamieniona zostaje kolejność stron, aby odpowiadały kolejności co do ich otwarcia
        else:
            pierwszy, drugi, trzeci = pomocnicza, pierwszy, drugi
            blad += 1

        bledy_zbior.append(blad)
        #replace.append((pierwszy, drugi, trzeci))

    return bledy_zbior

referencje = generator_referencji(10, 4)
print(referencje)
LRU(referencje, 5)