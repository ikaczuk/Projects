import pygame as pg
import sys


pg.init()

pg.display.set_caption("Kółko i krzyżyk")
screen_size = 750,750   #tworzy okno 750 x 750 pixeli
screen = pg.display.set_mode(screen_size)
czcionka = pg.font.SysFont('Bodoni MT Black', 80)
tablica = [["0", "0", "0"],
["0", "0", "0"],
["0", "0", "0"]]

def rys_tlo():  #rysowanie planszy
    screen.fill(pg.Color("grey"))
    i = 1
    while i * 80 < 720:
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(i * 245 + 15, 15), pg.Vector2(i * 245 + 15, 735), 5)  # rysowanie pionowych pasków
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, i * 245 + 15), pg.Vector2(735, i * 245 + 15), 5)  # rysowanie poziomych pasków
        i += 1

def rys(x,y):
    if str(tablica[x][y]) != "0":
        znak = czcionka.render(str(tablica[x][y]),True, pg.Color("blue"))
        screen.blit(znak, pg.Vector2(y*245, x*245))


def rys_smbole():
    for x in range(3):
        for y in range(3):
            rys(x, y)



def gra(gracz):
    runda = ["o", "x"]
    pozycja = pg.mouse.get_pos()  # zczytuje pozycje myszki
    wiersz = pozycja[1] // 245
    kolumna = pozycja[0] // 245
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == :
                    tablica[kolumna][wiersz] == "o"
                    figura = czcionka.render(str(runda[0]), True, pg.Color("blue"))
                    screen.blit(figura, (kolumna * 245, wiersz * 245))
                    pg.display.update()
                    return
                else:
                    tablica[kolumna][wiersz] == "x"
                    figura = czcionka.render(str(runda[1], True, pg.Color("blue")))
                    screen.blit(figura, (kolumna * 245, wiersz * 245))
                    pg.display.update()
                    return


def czy_wygrana():
    if tablica[0][0] != "0":
        if tablica[0][0]==tablica[1][1]==tablica[2][2] or tablica[2][0]==tablica[1][1]==tablica[0][2]:
            print("WYGRYWA ", tablica[1][1])
    for i in range(3):
        if tablica[i][0] != "0" or tablica[0][i] != "0":
            if tablica[i][0]==tablica[i][1]==tablica[i][2]:
                print("WYGRYWA ", tablica[i][0])
            elif tablica[0][i]==tablica[1][i]==tablica[2][i]:
                print("WYGRYWA ", tablica[0][i])




def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            gra()
            czy_wygrana()

    rys_tlo()
    rys_smbole()
    pg.display.flip()

while True:
    game_loop()