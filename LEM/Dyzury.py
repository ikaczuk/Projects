import csv

dane = open("dyzury.txt", "r")
Lista = []
liczba=[]

for line in dane:
    Lista.append(line.rstrip())

for i in range(len(Lista)):
    if Lista[i] not in liczba:
        print(Lista[i], Lista.count(Lista[i]))
        liczba.append(Lista[i])