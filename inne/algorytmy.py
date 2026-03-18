import random
#import numpy

#funckja "generator_procesów" generuje randomowe wartości dla procesów -> czas przybycia oraz czas wykonywania
def generator_procesów(ilosc_zadan, przyb_min, przyb_max, wyk_min, wyk_max):
    #ilosc_zadan - określa ile procesów jaka ma zostać utworzona
    #przyb_min - określa minimalny czas przybycia procesu
    #przyb_max - określa maksymalny czas przybycia procesu
    #wyk_min - określa minimalny czas wykonania procesu
    #wyk_max - określa maksymalny czas wykonania procesu
    #tablica procesy przechowuje wartości czasowe procesów
    procesy = [] # index 0 - określa czas przybycia procesu, index 1 - określa czaas wykonania procesu
    for i in range(ilosc_zadan):
        przybycie = random.randint(przyb_min, przyb_max)    #losuje liczbę, która określa czas przybycia procesu z przedziału od przyb_min do przyb_max
        wykonanie = random.randint(wyk_min, wyk_max)        #losuje liczbę, która określa czas wykonania procesu z przedziału od wyk_min do wyk_max
        procesy.append((przybycie,wykonanie))               #dodaje wartości procesu do tablicy procesy

    #sortuje procesy tak, aby były ustawione od tego, który przychodzi jako pierwszy, do tego, który przychodzi jako ostatni
    for i in range(ilosc_zadan):
        for j in range(1, ilosc_zadan - i):  #
            if procesy[j - 1][0] > procesy[j][0]:  #sprawdzanie, czy liczby powinny zostać zamienione miejscami zważywszy na czas dotarcia procesu
                procesy[j - 1], procesy[j] = procesy[j], procesy[j - 1]  #zamienienie liczb miejscami, aby były ustawione w dobrej kolejności według czasu dotarcia

    #zwraca wygenerowane wartości procesów ustawione w kolejności przybycia
    return procesy




#czas oczekiwania jest dosyć długi
#łatwy w wykonaniu i użyciu
#działa jak kolejka w sklepie
#krótkie procesy muszą czekać aż te długie, które wcześniej doszły, się skończą
#wt[i] =  at[i–1] + bt[i–1] + wt[i–1]) – at[i]  ------ wzór na obliczenie czasu oczekiwania
#wt[i] = czas oczekiwania obecnego procesu
#at[i-1] = czas przybycia poprzedniego procesu
#bt[i-1] = czas wykonania poprzedniego procesu
#wt[i-1] = czas oczekiwania poprzedniego procesu
#at[i] = czas przybycia obecnego procesu
#średni czas oczekiwania = suma czasów oczekiwania / ilość procesów
def FCFS(procesy):
    #procesy, to tablica, która przechowuje dwie wartości dla każdego procesu, które zostały uprzednio wygenerowane losowo dzięki funkcji generator_procesów
    #index 0 - czas przybycia procesu, index 1 - czas wykonywania procesu
    #obliczanie czasu oczekiwania (wt - wait time)
    #tablica "wt" przechowuje obliczony czas oczekiwania każdego procesu
    czas = procesy[0][0]
    wt = []
    wt.append(0)

    #obliczanie średniego czasu oczekiwania
    #avg_wt - zmienna przechowująca średnią wartość czasu oczekiwania wszystkich procesów
    avg_wt = 0
    for i in range(len(wt)):
        avg_wt += wt[i]

    avg_wt = avg_wt/len(wt)

    avg_wait_time = []

    i = 1
    while len(wt) >= i:
        pomocnicza = 0
        for j in range(i):
            pomocnicza += wt[j]

        sr = pomocnicza / i
        avg_wait_time.append(sr)
        i += 1

    # print("FCFS: ")
    # print("czas oczekiwania: ", wt)
    # print("średni czas oczekiwania do danego procesu: ", avg_wait_time)
    # print("średni czas oczekiwania wszystkich procesów: ", avg_wt)




def SJF(procesy):
    #zmienna "czas" odpowiada za symulację faktycznego czasu wykonywania i docierania procesów
    #tablica "użyte" przechowuje już wykonane procesy w odpowiedniej kolejności wykonania
    czas = 0
    użyte = []
    wt = []

    #pętla sprawdza, czy w kolejce czekają jakieś procesy do wykonania, jeśli nie, to nie jest wykonywana
    while len(procesy) != 0:
        #tablica "dotarły" przechowuje procesy, które już zdążyły dotrzeć i czekają na wykonanie
        dotarły = []
        #pętla for sprawdza, które z listy procesów dotarły do danego momentu w czasie
        #jeśli proces dotarł to jest dodawany do tablicy "dotarły"
        for i in range(len(procesy)):
            if procesy[i][0] <= czas:
                dotarły.append(procesy[i])

        #"if" sprawdza, czy jakieś procesy dotarły w międzyczasie wykonywania innego procesu
        #jeżeli nie, to czas zostaje zwiększony o 1 w oczekiwaniu na nowy proces
        #oraz do tablicy "dotarły" zostaje dodana wartość (0,0), aby móc obliczyć czas oczekiwania
        #jeżeli tablica "dotarły" nie jest pusta, to znajdujące się w niej procesy są sortowane po czasie wykonywania
        if len(dotarły) == 0:
            czas += 1
            #dotarły.append((0,0))
            continue
        else:
            for x in range(len(dotarły)):
                for y in range(1, len(dotarły) - x):
                    if procesy[y - 1][1] > procesy[y][1]:
                        procesy[y - 1], procesy[y] = procesy[y], procesy[y - 1]

            proces_wykonywany = dotarły[0]
            czas_przybycia = proces_wykonywany[0]
            czas_wykonywania = proces_wykonywany[1]

            #tablica "użyte" dostaje nową zmienną, która przechowuje obecnie wykonany proces
            użyte.append((czas_przybycia,czas_wykonywania))
            czas_oczekiwania = 0
            if czas - czas_przybycia > 0:
                czas_oczekiwania = czas - czas_przybycia
            wt.append(czas_oczekiwania)

            #z tablicy procesów usunięty zostaje ten, który został właśnie wykonany
            #zostaje usunięty, aby nie brać go ponownie pod uwagę i zmniejszyć ilość wykonywanych działań
            procesy.remove(proces_wykonywany)

            #czas zostaje zwiększony o czas wykonywania kolejnego procesu
            czas += czas_wykonywania

    avg_wt = 0
    for i in range(len(wt)):
        avg_wt += wt[i]

    avg_wt = avg_wt / len(wt)

    srednia_wartosc = []

    for i in range(len(wt)):
        j = 0
        pomocnicza = 0
        while j <= i:
            pomocnicza += wt[j]
            j += 1
        sr = pomocnicza / (i + 1)
        srednia_wartosc.append(sr)

    print("SJF: ")
    print("średni czas oczekiwania do danego procesu: ", srednia_wartosc)
    print("czas oczekiwania: ", wt)
    print("średni czas oczekiwania wszystkich procesów: ", avg_wt)

















def generator_referencji(ilosc_referencji, ilosc_stron):
    referencje = []
    for i in range(0, ilosc_referencji):
        ref = random.randint(1, ilosc_stron)
        referencje.append(ref)
    return referencje


def FIFO(referencje):
    #tablica "replace" służy do przechowywania otwartych stron
    #zmienne "pierwszy", "drugi" i "trzeci" przechowują trzy obecnie otwarte strony
    replace = []
    pierwszy = referencje[0]
    drugi = 0
    trzeci = 0

    blad = 1

    #zmienne "pierwszy_czas", "drugi_czas" i "trzeci_czas" przechowują czas z jakim dana strona jest otwarta
    #zmienna "pierwszy_czas" jest ustawiona na 1, ponieważ pierwsza w kolejności strona zostanie od razu otwarta
    #zatem jej czas otwarcia wynosi 1 podczas sprawdzania kolejnych elementów tablicy "referencje"
    pierwszy_czas = 1
    drugi_czas = 0
    trzeci_czas = 0

    replace.append((pierwszy, drugi, trzeci))   #komenda uzupełnia tablicę "replace" o nowe 3 otwarte strony

    for i in range(1,len(referencje)):
        if drugi == 0 and referencje[i] != pierwszy:    #sprawdza czy drugi element jest pusty oraz czy obecnie sprawdzana strona już się nie pojawiła jako pierwszy element
            #pierwszy oraz drugi czas otwarcia strony są zwiększane o 1, ponieważ żadna strona nie jest zamieniana, więc obie są otwarte o 1 jednostkę dłużej
            pierwszy_czas += 1
            drugi_czas += 1
            blad += 1
            #skoro druga strona nie jest tą samą co pierwsza oraz pozycja druga jest pusta, to należy przypisać ją do zmiennej "drugi"
            drugi = referencje[i]
        elif drugi != 0 and trzeci == 0 and referencje[i] != pierwszy and referencje[i] != drugi:   #sprawdza czy trzeci element jest pusty oraz czy obecnie sprawdzana strona już się nie pojawiła jako pierwszy lub drugi element
            #wszystkie trzy czasy otwarcia strony są zwiększane o 1, ponieważ żadna strona nie jest zamieniana, więc są one otwarte o 1 jednostkę dłużej
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas += 1
            blad += 1
            #skoro trzecia strona nie jest tą samą co pierwsza ani druga oraz pozycja trzecia jest pusta, to należy przypisać ją do zmiennej "trzeci"
            trzeci = referencje[i]

        #jeśli któryś z elementów ma taką samą wartość jak obecnie sprawdzana strona, to wszystkie trzy będą otwarte o jedną jednostkę dłużej
        #ponieważ nie zachodzą żadne zmiany
        elif pierwszy == referencje[i] or drugi == referencje[i] or trzeci == referencje[i]:
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas += 1

        #jeśli żaden element nie jest pusty oraz nie jest równy obecnie sprawdzanej stronie
        #to należy sprawdzić, którą ze stron należy zamknąć i w jej miejsce otworzyć nową
        #można to sprawdzić na podstawie tego, który czas otwarcia strony jest najdłuższy
        #wszystkie czasy zostaną powiększone o jedną jednostkę, oprócz strony, która została zamieniona
        #czas nowo otwartej strony będzie wynosił 1
        elif pierwszy_czas > drugi_czas and pierwszy_czas > trzeci_czas:
            pierwszy_czas = 1
            drugi_czas += 1
            trzeci_czas += 1
            pierwszy = referencje[i]
            blad += 1
        elif pierwszy_czas < drugi_czas and drugi_czas > trzeci_czas:
            pierwszy_czas += 1
            drugi_czas = 1
            trzeci_czas += 1
            drugi = referencje[i]
            blad += 1
        elif trzeci_czas > drugi_czas and pierwszy_czas < trzeci_czas:
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas = 1
            trzeci = referencje[i]
            blad += 1

        replace.append((pierwszy, drugi, trzeci))   #komenda uzupełnia tablicę "replace" o nowe 3 otwarte strony

    print("FIFO: ")
    print("otwierane strony: ", replace)
    print("ilość błędów: ", blad)



def LRU(referencje):
    # tablica "replace" służy do przechowywania ostatnio użytych stron
    # zmienne "pierwszy", "drugi" i "trzeci" przechowują trzy ostatnio otwarte strony
    replace = []
    pierwszy = referencje[0]
    drugi = 0
    trzeci = 0
    blad = 1
    replace.append((pierwszy, drugi, trzeci))   #komenda uzupełnia tablicę "replace" o 3 nowe ostatnio otwarte strony

    for i in range(1, len(referencje)):
        pomocnicza = referencje[i]

        #sprawdzenie, czy któraś z ostatnio otwartych stron zostaje ponownie otwarta
        if pierwszy == pomocnicza:
            replace.append((pierwszy, drugi, trzeci))
            continue
        elif drugi == pomocnicza:
            pierwszy, drugi = drugi, pierwszy
        elif trzeci == pomocnicza:
            pierwszy, drugi, trzeci = trzeci, pierwszy, drugi

        #jeżeli żadna ze stron nie zostaje ponownie otwarta, to ostatnia używana zostaje zamknięta
        #zamieniona zostaje kolejność stron, aby odpowiadały kolejności co do ich otwarcia
        else:
            pierwszy, drugi, trzeci = pomocnicza, pierwszy, drugi
            blad += 1

        replace.append((pierwszy, drugi, trzeci))

    print("LRU: ")
    print("otwierane strony: ", replace)
    print("ilość błędów: ", blad)














procesy = generator_procesów(25, 0, 100, 5,5)
#procesy = generator_procesów(15,0,75,5,50)
print("procesy: ", procesy)

print()

FCFS(procesy)

print()

SJF(procesy)

print()
print()

referencje = generator_referencji(10, 5)
print("referencje: ", referencje)

print()

FIFO(referencje)

print()

LRU(referencje)