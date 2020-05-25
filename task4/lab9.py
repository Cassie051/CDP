import data, sys

Processes = data.data.copy()
N = data.n
M = data.m

def Cmax(CProcesses):
    Cstart = 0
    Cend = 0
    endList = [[0 for i in range(len(CProcesses[0]))]  for j in range(len(CProcesses))]
    startList = [[0 for i in range(len(CProcesses[0]))]  for j in range(len(CProcesses))]
    for i in range(0, len(CProcesses)):
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
    return endList[len(CProcesses)-1][len(CProcesses[0])-1]

def Neh(NProcesses):
    k = 1
    W = []
    pi = []
    pitmp = []
    for j in NProcesses:
        tmp = 0
        for i in range(M):
            tmp += j[i]
        W.append([tmp, j])
    W.sort(key = lambda x: (x[0]))
    while len(W) != 0 :
        j = W[len(W)-1][1]
        for l in range(0, k):
            pitmp.insert(l, j)
            if len(pi) == 0:
                pi.insert(l, j)
            elif Cmax(pitmp) < Cmax(pi):
                pi.insert(l, j)
        del W[len(W)-1]
        k += 1
    return Cmax(pi)

print(Neh(Processes))