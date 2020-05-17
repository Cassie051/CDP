import data
import sys, itertools

Processes = data.data
N = data.n
M = data.m

def Cmax(CProcesses):
    Cstart = 0
    Cend = 0
    endList = [[0 for i in range(M)]  for j in range(N)]
    startList = [[0 for i in range(M)]  for j in range(N)]
    for i in range(0, N):
        for j in range(0, M):
            if(i == 0):
                Cstart = Cend
                Cend = Cstart + CProcesses[i][j]
            else:
                if(j == 0):
                    Cstart = endList[i-1][j]
                else:
                    Cstart = max(endList[i-1][j], Cend)
                Cend = Cstart + CProcesses[i][j]

            startList[i][j] = Cstart
            endList[i][j] = Cend
    return endList[N-1][M-1]

# not works yet
def BruteForce(BProcesses):
    price = int(sys.maxsize)
    result = []
    while True:
        tmp = Cmax(BProcesses)
        if(tmp < price):
            price = tmp
            result.clear()
            for i in range(0, N):
                result.append(BProcesses[i].index())
        for j in range(0, M):
            itertools.permutations(Processes[j], M).__next__()

        if (itertools.permutations(Processes[0], N).__next__() == 0):
            break
    return price

print (Cmax(Processes))