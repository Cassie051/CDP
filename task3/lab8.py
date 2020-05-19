import data, lab6
import sys

Processes = data.data
N = data.n
M = data.m

def Bound(BProcesses, pi, case):
    result = 0
    Ctmp = 0
    p = 0
    pall = 0
    if(case == 1):
        for i in range(0, M):
            for j in range(0, len(BProcesses)-1):
                p += BProcesses[j][i]
                result = max(result, pi[len(pi)-1][i] + p)
        return result
    elif(case == 2):
        pmin = int(sys.maxsize)
        for i in range(0, M):
            for j in range(0, len(BProcesses)):
                p += BProcesses[i][j]
                for k in range(i+1, M):
                    for g in range(0, N):
                        pmin = min(pmin, BProcesses[k][g])
                    pall += pmin
                result = max(result, pi[len(pi)-1][i] + p + pall)
        return result
    elif(case == 3):
        return result
    elif(case == 4):
        return result
    else:
        return print("No LB type")

def BnB(j, BProcesses, pi):
    UB = int(sys.maxsize)
    pi.append(j)
    BProcesses.remove(j)
    if not (len(BProcesses) == 0):
        LB =  Bound(BProcesses, pi, 1)
        if(LB <= UB):
            for j in BProcesses:
                BnB(j, BProcesses, pi)
    else:
        Cmax =  lab6.Cmax(pi)
        if(Cmax < UB):
            UB = Cmax
            best = pi         # zapamietujemy najlepsza permutacja
    return UB


def initBnB(BProcesses):
    pi = []
    pern = []
    for j in BProcesses:
        return BnB(j, BProcesses, pi)

print(initBnB(Processes))
