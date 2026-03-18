def FCFS(procesy):
    #procesy, to tablica, która przechowuje dwie wartości dla każdego procesu, które zostały uprzednio wygenerowane losowo dzięki funkcji generator_procesów
    #index 0 - czas przybycia procesu, index 1 - czas wykonywania procesu
    #obliczanie czasu oczekiwania (wt - wait time)
    #tablica "wt" przechowuje obliczony czas oczekiwania każdego procesu
    wt = []
    czas = procesy[0][0] + procesy[0][1]
    wt = []
    wt.append(0)
    for i in range(1, len(procesy)):
        if czas >= procesy[i][0]:
            wait = czas - procesy[i][0]
            czas += procesy[i][1]
        else:
            wait = 0
            czas = procesy[i][0] + procesy[i][1]
        wt.append(wait)

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

    return wt, avg_wait_time