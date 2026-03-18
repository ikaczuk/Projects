from systemy.generatory.procesy import generator_procesów
from systemy.FCFS import FCFS
from systemy.SJF import SJF

#Jak metody poradzą sobie z 25, 75, 125 procesów o losowych czasach nadejścia od 0 do 100 oraz czasie wykonania równym 5
#Jak metody poradzą sobie z 25, 75, 125 procesów o czasie nadejścia 0 oraz losowych czasach wykonania z przedziału od 1 do 10

def zapis(procesy, plik):
    #zmienna "tablica" przekazuje wygenerowane wartości procesów (czas wprzybycia, czas wykonywania)
    #zmienna "plik" przekazuje plik, w którym będą zapisane wyniki eksperymentu
    plik.write("FCFS:\n")
    wyniki = FCFS(procesy)
    plik.write("CZAS OCZEKIWANIA\tSREDNI CZAS OCZEKIWANIA\n")

    for i in range(len(wyniki[0])):
        plik.write(f"{wyniki[0][i]}\t{wyniki[1][i]}\n")

    plik.write("\n\n\n")

    plik.write("SJF:\n")
    wyniki1 = SJF(procesy)
    plik.write("CZAS OCZEKIWANIA\tSREDNI CZAS OCZEKIWANIA\n")

    for i in range(len(wyniki1[0])):
        plik.write(f"{wyniki1[0][i]}\t{wyniki1[1][i]}\n")










#taki sam czas wykonania
with open("procesy1.txt", "w") as przyklad1:
    procesy = generator_procesów(125, 0, 100, 5, 5)
    zapis(procesy, przyklad1)

#taki sam czas przybycia
with open("procesy2.txt", "w") as przyklad2:
    procesy = generator_procesów(125, 0, 0, 1, 10)
    zapis(procesy, przyklad2)

#czas przybycia (0) i wykonania jest taki sam (5)
with open("procesy3.txt", "w") as przyklad3:
    procesy = generator_procesów(125, 0, 0, 5, 5)
    zapis(procesy, przyklad3)

#wszystkie wartości są różne
with open("procesy4.txt", "w") as przyklad4:
    procesy = generator_procesów(125, 0, 100, 1, 25)
    zapis(procesy, przyklad4)

#sprawdzenie co się stanie, jeśli wszystkie procesy dotrą w tym samym czasie, ale pierwszy proces będzie miał czas wykonani równy 100 jednostek czasu
with open("procesy5.txt", "w") as przyklad5:
    procesy = [(0, 100), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
    zapis(procesy, przyklad5)