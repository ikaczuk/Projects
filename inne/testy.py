from systemy.generatory.procesy import generator_procesów
from systemy.FCFS import FCFS
from systemy.SJF import SJF

procesy = generator_procesów(20, 0,0,1,1)
procesy[0] = (0, 100)
print(procesy)

print(FCFS(procesy)[0])
print(SJF(procesy)[0])
