import time

import pygame as pg
import sys

pg.init()

czcionka = pg.font.SysFont('Bodoni MT Black', 50)
screen_size = 750,750
screen = pg.display.set_mode((screen_size))
pg.display.set_caption("Kółko i krzyżyk")
tablica = [["0","0","0"],
            ["0","0","0"],
            ["0","0","0"]]
tura = "O"



def rys_tło():
    screen.fill(pg.Color("grey"))
    i = 1
    while i * 80 < 720:
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(i * 245 + 15, 15), pg.Vector2(i * 245 + 15, 735),8)  # rysowanie pionowych pasków
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, i * 245 + 15), pg.Vector2(735, i * 245 + 15),8)  # rysowanie poziomych pasków
        i += 1


def rys_XO():
    kolumna = 0
    for i in range(len(tablica)):
        wiersz = 0
        for j in range(len(tablica[i])):
            if tablica[i][j] == "O":
                pg.draw.circle(screen, "blue", (kolumna*245+135, wiersz*245+135), 100, 8)
            if tablica[i][j] == "X":
                pg.draw.line(screen, "green", (kolumna*245 + 50, wiersz*245 + 50), (kolumna*245 + 210, wiersz*245 + 210), 8)
                pg.draw.line(screen, "green", (kolumna * 245 + 50, wiersz * 245 + 210), (kolumna * 245 + 210, wiersz * 245 + 50), 8)
            wiersz += 1
        kolumna += 1


def czy_wygrana():
    wygrana = None
    for kolumna in range(3):
        if tablica[kolumna][0] == tablica[kolumna][1] == tablica[kolumna][2] and tablica[kolumna][0] != "0":
            wygrana = tablica[kolumna][0]
            return wygrana

    for wiersz in range(3):
        if tablica[0][wiersz] == tablica[1][wiersz] == tablica[2][wiersz] and tablica[0][wiersz] != "0":
            wygrana = tablica[0][wiersz]
            return wygrana

    if tablica[0][0] == tablica[1][1] == tablica[2][2] and tablica[0][0] != "0":
        wygrana = tablica[0][0]
        return wygrana

    if tablica[0][2] == tablica[1][1] == tablica[2][0] and tablica[0][2] != "0":
        wygrana = tablica[0][2]
        return wygrana

    if wygrana is None:
        for i in range(len(tablica)):
            for j in range(len(tablica[i])):
                if tablica[i][j] == "0":
                    return None
        return "REMIS"



def napis_końcowy():
    if czy_wygrana() == "REMIS":
        tekst = "REMIS!"
    else:
        tekst = "WYGRYWA GRACZ " + str(czy_wygrana()) + " !"
    obrazek = czcionka.render(tekst, True, "red")
    pg.draw.rect(screen, "white", (750//4, 750//4, 380, 30))
    screen.blit(obrazek, (750//4, 750//4))





while True:
    rys_tło()
    rys_XO()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pozycja = pg.mouse.get_pos()
            kolumna = pozycja[0]//245
            wiersz = pozycja[1]//245
            if tablica[kolumna][wiersz] == "0" and tura == "O":
                tablica[kolumna][wiersz] = tura
                tura = "X"
            elif tablica[kolumna][wiersz] == "0" and tura == "X":
                tablica[kolumna][wiersz] = tura
                tura = "O"

        pg.display.update()

        if czy_wygrana() == "REMIS":
            napis_końcowy()
            time.sleep(1)
        elif czy_wygrana() == "O":
            napis_końcowy()
            time.sleep(1)
        elif czy_wygrana() == "X":
            napis_końcowy()
            time.sleep(1)

    pg.display.update()
