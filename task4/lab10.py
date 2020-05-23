import data
import random
import sys
import math


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

#Kowalstwo

def deltaCmac(pi, pi_new):
    return Cmax(pi)-Cmax(pi_new)

def probability(pi, pi_new, T):
    delta = deltaCmac(pi, pi_new)
    prob = math.exp(delta/T)
    return prob

def chillLinear(T,x):
    Ice_Cold_T = T - x
    return Ice_Cold_T

def chillLog(T, iter):
    Ice_Cold_T = T/math.log(iter+1)
    return Ice_Cold_T

def SAA():
    T0 = sys.maxsize
    T = T0