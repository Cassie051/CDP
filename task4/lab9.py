import data, sys

Processes = data.data.copy()
N = data.n
M = data.m

def Cmax(CProcesses):
    Cstart = 0
    Cend = 0
    endList = [[0 for i in range(N)]  for j in range(M)]
    startList = [[0 for i in range(N)]  for j in range(M)]
    for i in range(0, M):
        for j in range(0, len(CProcesses[0])):
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
    return endList[M-1][N-1]

def Neh(NProcesses):
    k = 1
    W = []
    for j in NProcesses:
        tmp = 0
        for i in range(M):
            tmp += j[i]
        W.append(tmp, j)
    W.sort(key = lambda x: (x[0]))
    while len(W) != 0 :
        