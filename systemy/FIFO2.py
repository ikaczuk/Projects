def FIFO2(referencje):
    #tablica "replace" służy do przechowywania otwartych stron
    #zmienne "pierwszy", "drugi" i "trzeci" przechowują trzy obecnie otwarte strony
    replace = []
    pierwszy = referencje[0]
    drugi = 0
    trzeci = 0
    czwarty = 0

    blad = 1
    bledy_zbior = []
    bledy_zbior.append(blad)
    #zmienne "pierwszy_czas", "drugi_czas" i "trzeci_czas" przechowują czas z jakim dana strona jest otwarta
    #zmienna "pierwszy_czas" jest ustawiona na 1, ponieważ pierwsza w kolejności strona zostanie od razu otwarta
    #zatem jej czas otwarcia wynosi 1 podczas sprawdzania kolejnych elementów tablicy "referencje"
    pierwszy_czas = 1
    drugi_czas = 0
    trzeci_czas = 0
    czwarty_czas = 0

    replace.append((pierwszy, drugi, trzeci, czwarty))   #komenda uzupełnia tablicę "replace" o nowe 3 otwarte strony

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
        elif trzeci != 0 and referencje[i] != pierwszy and referencje[i] != drugi and referencje[i] != trzeci:
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas += 1
            czwarty_czas += 1
            blad += 1

        #jeśli któryś z elementów ma taką samą wartość jak obecnie sprawdzana strona, to wszystkie trzy będą otwarte o jedną jednostkę dłużej
        #ponieważ nie zachodzą żadne zmiany
        elif pierwszy == referencje[i] or drugi == referencje[i] or trzeci == referencje[i] or czwarty == referencje[i]:
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas += 1
            czwarty_czas += 1

        #jeśli żaden element nie jest pusty oraz nie jest równy obecnie sprawdzanej stronie
        #to należy sprawdzić, którą ze stron należy zamknąć i w jej miejsce otworzyć nową
        #można to sprawdzić na podstawie tego, który czas otwarcia strony jest najdłuższy
        #wszystkie czasy zostaną powiększone o jedną jednostkę, oprócz strony, która została zamieniona
        #czas nowo otwartej strony będzie wynosił 1
        elif pierwszy_czas > drugi_czas and pierwszy_czas > trzeci_czas and pierwszy_czas > czwarty_czas:
            pierwszy_czas = 1
            drugi_czas += 1
            trzeci_czas += 1
            pierwszy = referencje[i]
            blad += 1
        elif drugi_czas > pierwszy_czas and drugi_czas > trzeci_czas and drugi_czas > czwarty_czas:
            pierwszy_czas += 1
            drugi_czas = 1
            trzeci_czas += 1
            drugi = referencje[i]
            blad += 1
        elif trzeci_czas > pierwszy_czas and trzeci_czas > drugi_czas and trzeci_czas > czwarty_czas:
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas = 1
            trzeci = referencje[i]
            blad += 1
        elif czwarty_czas > pierwszy_czas and czwarty_czas > drugi_czas and czwarty_czas > trzeci_czas:
            pierwszy_czas += 1
            drugi_czas += 1
            trzeci_czas = 1
            trzeci = referencje[i]
            blad += 1
        bledy_zbior.append(blad)
        replace.append((pierwszy, drugi, trzeci))   #komenda uzupełnia tablicę "replace" o nowe 3 otwarte strony

    return referencje, replace, bledy_zbior