def SJF(procesy):
    # zmienna "czas" odpowiada za symulację faktycznego czasu wykonywania i docierania procesów
    # tablica "użyte" przechowuje już wykonane procesy w odpowiedniej kolejności wykonania
    czas = 0
    użyte = []
    wt = []

    # pętla sprawdza, czy w kolejce czekają jakieś procesy do wykonania, jeśli nie, to nie jest wykonywana
    while len(procesy) != 0:
        # tablica "dotarły" przechowuje procesy, które już zdążyły dotrzeć i czekają na wykonanie
        dotarły = []
        # pętla for sprawdza, które z listy procesów dotarły do danego momentu w czasie
        # jeśli proces dotarł to jest dodawany do tablicy "dotarły"
        for i in range(len(procesy)):
            if procesy[i][0] <= czas:
                dotarły.append(procesy[i])

        # "if" sprawdza, czy jakieś procesy dotarły w międzyczasie wykonywania innego procesu
        # jeżeli nie, to czas zostaje zwiększony o 1 w oczekiwaniu na nowy proces
        # oraz do tablicy "dotarły" zostaje dodana wartość (0,0), aby móc obliczyć czas oczekiwania
        # jeżeli tablica "dotarły" nie jest pusta, to znajdujące się w niej procesy są sortowane po czasie wykonywania
        if len(dotarły) == 0:
            czas += 1
            # dotarły.append((0,0))
            continue
        else:
            for x in range(len(dotarły)):
                for y in range(1, len(dotarły) - x):
                    if procesy[y - 1][1] > procesy[y][1]:
                        procesy[y - 1], procesy[y] = procesy[y], procesy[y - 1]

            proces_wykonywany = dotarły[0]
            czas_przybycia = proces_wykonywany[0]
            czas_wykonywania = proces_wykonywany[1]

            # tablica "użyte" dostaje nową zmienną, która przechowuje obecnie wykonany proces
            użyte.append((czas_przybycia, czas_wykonywania))
            czas_oczekiwania = 0
            if czas - czas_przybycia > 0:
                czas_oczekiwania = czas - czas_przybycia
            wt.append(czas_oczekiwania)

            # z tablicy procesów usunięty zostaje ten, który został właśnie wykonany
            # zostaje usunięty, aby nie brać go ponownie pod uwagę i zmniejszyć ilość wykonywanych działań
            procesy.remove(proces_wykonywany)

            # czas zostaje zwiększony o czas wykonywania kolejnego procesu
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

    return wt, srednia_wartosc