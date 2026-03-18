import random

#funkcja "generator_procesów" generuje randomowe wartości dla procesów -> czas przybycia oraz czas wykonywania
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