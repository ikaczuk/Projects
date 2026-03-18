from systemy.generatory.referencje import generator_referencji
from systemy.LRU import LRU

def LRU2(referencje):
    # tablica "replace" służy do przechowywania ostatnio użytych stron
    # zmienne "pierwszy", "drugi" i "trzeci" przechowują trzy ostatnio otwarte strony
    replace = []
    pierwszy = referencje[0]
    drugi = 0
    trzeci = 0
    czwarty = 0
    blad = 1
    bledy_zbior = []

    bledy_zbior.append(blad)
    replace.append((pierwszy, drugi, trzeci, czwarty))  # komenda uzupełnia tablicę "replace" o 3 nowe ostatnio otwarte strony

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
        elif czwarty == pomocnicza:
            pierwszy, drugi, trzeci, czwarty == czwarty, pierwszy, drugi, trzeci

        # jeżeli żadna ze stron nie zostaje ponownie otwarta, to ostatnia używana zostaje zamknięta
        # zamieniona zostaje kolejność stron, aby odpowiadały kolejności co do ich otwarcia
        else:
            pierwszy, drugi, trzeci = pomocnicza, pierwszy, drugi
            blad += 1

        bledy_zbior.append(blad)
        replace.append((pierwszy, drugi, trzeci))

    return referencje, replace, bledy_zbior