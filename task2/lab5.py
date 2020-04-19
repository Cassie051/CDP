import data, sys
import itertools as it

PDProcesses = data.AllProcesses.copy()

N = data.n

def PDi(PDProcesses):
    Processes = PDProcesses.copy()
    F = [[] for i in range(0, N-1)]
    for i in range(0, N-1):
        for j in range(0, int(2**(N-1))):
            F[i].append(-1)

    for x in it.permutations('1100', 4 ):
        print(x)

PDi(PDProcesses)


