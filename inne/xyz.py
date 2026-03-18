def LRU(referencje):
    # tablica "replace" służy do przechowywania ostatnio użytych stron
    # zmienne "pierwszy", "drugi" i "trzeci" przechowują trzy ostatnio otwarte strony
    replace = []
    pierwszy = referencje[0]
    drugi = 0
    trzeci = 0
    blad = 1
    bledy_zbior = []

    bledy_zbior.append(blad)
    replace.append((pierwszy, drugi, trzeci))  # komenda uzupełnia tablicę "replace" o 3 nowe ostatnio otwarte strony

    for i in range(1, len(referencje)):
        pomocnicza = referencje[i]

        # sprawdzenie, czy któraś z ostatnio otwartych stron zostaje ponownie otwarta
        if pierwszy == pomocnicza:
            replace.append((pierwszy, drugi, trzeci))
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
        replace.append((pierwszy, drugi, trzeci))

    return referencje, replace, bledy_zbior

referencje = [3, 3, 1, 5, 1, 5, 3, 5, 5, 4]
print(len(LRU(referencje)[2]))
print(len(LRU(referencje)[0]))