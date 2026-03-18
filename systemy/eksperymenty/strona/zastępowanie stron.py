from systemy.generatory.referencje import generator_referencji
from systemy.FIFO import FIFO
from systemy.FIFO2 import FIFO2
from systemy.LRU import LRU
from systemy.LRU2 import LRU2


def zapis(referencje, plik, n):
    if n == 1:
        plik.write("FIFO:\n")
        plik.write("OBECNA STRONA\tKOLEJKA\tILOSC BLEDOW\n")
        wyniki = FIFO(referencje)
        for i in range(len(wyniki[0])):
            plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\t{wyniki[2][i]}\n")

        plik.write("\n\n\n")

        plik.write("LRU:\n")
        plik.write("OBECNA STRONA\tKOLEJKA\tILOSC BLEDOW\n")
        wyniki = LRU(referencje)
        for i in range(len(wyniki[0])):
            plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\t{wyniki[2][i]}\n")

    else:
        plik.write("FIFO:\n")
        plik.write("OBECNA STRONA\tKOLEJKA\tILOSC BLEDOW\n")
        wyniki = FIFO(referencje)
        for i in range(len(wyniki[0])):
            plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\t{wyniki[2][i]}\n")

        plik.write("FIFO2:\n")
        plik.write("OBECNA STRONA\tKOLEJKA\tILOSC BLEDOW\n")
        wyniki = FIFO2(referencje)
        for i in range(len(wyniki[0])):
            plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\t{wyniki[2][i]}\n")

        plik.write("\n\n\n")

        plik.write("LRU:\n")
        plik.write("OBECNA STRONA\tKOLEJKA\tILOSC BLEDOW\n")
        wyniki = LRU(referencje)
        for i in range(len(wyniki[0])):
            plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\t{wyniki[2][i]}\n")

        plik.write("\n\n\n")

        plik.write("LRU2:\n")
        plik.write("OBECNA STRONA\tKOLEJKA\tILOSC BLEDOW\n")
        wyniki = LRU2(referencje)
        for i in range(len(wyniki[0])):
            plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\t{wyniki[2][i]}\n")







with open("strony1.txt", "w") as przyklad1:
    referencje = generator_referencji(125, 5)
    zapis(referencje, przyklad1, 1)


with open("strony2.txt", "w") as przyklad2:
    referencje = generator_referencji(20, 5)
    zapis(referencje, przyklad2, 1)


with open("strony3.txt", "w") as przyklad3:
    referencje = generator_referencji(125, 40)
    zapis(referencje, przyklad3, 2)


with open("strony4.txt", "w") as przyklad4:
    referencje = generator_referencji(20, 5)
    zapis(referencje, przyklad4, 2)

with open("strony5.txt", "w") as przyklad5:
    referencje = generator_referencji(20, 5)
    zapis(referencje, przyklad5, 1)