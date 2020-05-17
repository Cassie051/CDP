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
    picopy = []
    UB = int(sys.maxsize)
    picopy.append(j)
    BProcesses.remove(j)
    if(len(BProcesses) != 0):
        LB =  Bound(BProcesses, picopy, 1)
        if(LB <= UB):
            for j in BProcesses:
                BnB(j, BProcesses, picopy)
    else:
        Cmax =  lab6.Cmax(picopy)
        if(Cmax < UB):
            UB = Cmax
            best = picopy         # zapamietujemy najlepsza permutacja
    return UB


def initBnB(BProcesses):
    pi = []
    pern = []
    for j in BProcesses:
        return BnB(j, BProcesses, pi)

print(initBnB(Processes))
