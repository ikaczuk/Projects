from dokusan import generators
import numpy as np
import pygame as pg
import sys



#win = screen

#robienie okna wyświetlającego sudoku
pg.init()
pg.display.set_caption("Sudoku")
screen_size = 750,750   #tworzy okno 750 x 750 pixeli
screen = pg.display.set_mode(screen_size)
czcionka = pg.font.SysFont('Bodoni MT Black', 80)


def rys_tlo():  #rysowanie kwadratów na planszy
    screen.fill(pg.Color("grey"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 725, 725), 10)    #tworzy obramowanie gry (duży kwadrat)
    i = 1
    while i*80 < 720:
        if i%3 > 0:
            grubosc_lini = 5
        else:
            grubosc_lini = 10
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(i*80 + 15, 15), pg.Vector2(i*80 + 15, 735), grubosc_lini)   #rysowanie pionowych pasków
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, i*80 + 15), pg.Vector2(735, i*80 + 15), grubosc_lini)   #rysowanie poziomych pasków
        i += 1

def numerki(x,y,tablica,kolor):
    if str(tablica[x][y]) != "0":
        numer = czcionka.render(str(tablica[x][y]),True, pg.Color(kolor))
        screen.blit(numer, pg.Vector2(y*80+37, x*80+37))


#losowanie numerków do sudoku
tablica = np.array(list(str(generators.random_sudoku(avg_rank=150))))  # generuję tablicę z randomowymi numerami
tablica = tablica.reshape(9, 9)  # zmienia tablicę na kwadratową 9x9
tablica1 = [['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0']]

def rys_cyfry(tab, kolor):    #rysowanie numerków w sudoku
    for x in range(9):
        for y in range(9):
            numerki(x, y, tab, kolor)



def CzyCyfraMozeTamByc(wiersz, kolumna, nr):
    for i in range(0,9):
        if tablica1[wiersz][i] == nr or tablica[wiersz][i] == nr:
            return False
    for i in range(0,9):
        if tablica1[i][kolumna] == nr or tablica[i][kolumna] == nr:
            return False
    x = (kolumna//3)*3
    y = (wiersz//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if tablica1[y+i][x+j] == nr or tablica[y+i][x+j] == nr:
                return False

    return True




#robienie działąjącej części gry
def uzupelnianie(screen, pozycja):  #screen = win
    i = pozycja[1]
    j = pozycja[0]
    czcionkaWpis = pg.font.SysFont('Bodoni MT Black', 80)
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:  # wciśnięcie klawisza
                if tablica[i][j] != "0":
                    return
                #zamiast rysować kwadratu, zrobić drugą identczną tablicę, która będzie przechowywała wartości wpisane
                #żeby nie było problemu z rysowaniem kwadratu, ani edycją bazowych cyfr
                #będę rysowała obie tablice w różnych kolorach i na bieżąco sprawdzała, czy cyfra może siętam znaleźć
                if event.key == 48:         #48 to wartość dla 0
                    tablica1[i][j] = event.key - 48
                    pg.draw.rect(screen, "grey", (j*80+30, i*80+30, 80-20, 80-20))
                    pg.display.update()
                if 0 < event.key-48 < 10:  #sprawdzanie, czy wpisywane wartości są ok
                    if CzyCyfraMozeTamByc(j,i,str(event.key-48)) == False:
                        kolor = "red"
                    else:
                        kolor = "grey"
                    pg.draw.rect(screen, kolor, (j*80+30, i*80+30, 80-20, 80-20))
                    wartosc = czcionkaWpis.render(str(event.key-48), True, "black")
                    screen.blit(wartosc, (j*80+37, i*80+37))
                    tablica1[i][j] = event.key - 48
                    pg.display.update()
                return
            return


def game_loop():
    rys_tlo()
    rys_cyfry(tablica, "blue")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:  # 1 oznacza lewy przycisk myszy
            pozycja = pg.mouse.get_pos()  # zczytuje pozycje myszki
            wiersz = pozycja[1]//80
            kolumna = pozycja[0]//80
            uzupelnianie(screen, (kolumna, wiersz))
            nr = tablica1[kolumna][wiersz]

    rys_cyfry(tablica1,"black")
    pg.display.flip()

while True:
    game_loop()