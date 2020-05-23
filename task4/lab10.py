import data
import random
import sys
import math


Processes = data.data.copy()
N = data.n
M = data.m

T0 = 100 #100 10000
L = math.sqrt(N) #N N*N
x = T0/1000 #T0/10000 T0/100000
alpha = 0,97 #0,95 0,90


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

#ChilleraUtopia

def deltaCmac(pi, pi_new):
    return Cmax(pi)-Cmax(pi_new)

def probability(pi, pi_new, T):
    delta = deltaCmac(pi, pi_new)
    prob = math.exp(delta/T)
    return prob

def chillLinear(T, x):
    Ice_Cold_T = T - x
    return Ice_Cold_T

def chillGeometric(T, alpha):
    Ice_Cold_T = T*alpha
    return Ice_Cold_T

def chillLog(T, iterator):
    Ice_Cold_T = T/math.log(iterator+1)
    return Ice_Cold_T

def moveMethod(mm, i, j, pi, AlgProc):
    if mm == 'swap':
        #temp = AlgProc[pi]
        #AlgProc[pi] = AlgProc[i][j]
        #Algproc[i][j] = temp
        #return AlgProc
    elif mm == 'insert':
        #AlgProc[pi] = AlgProc[i][j]
        #return AlgProc
    elif mm == 'twist':
        #AlgProc[pi] = AlgProc[j][i]
        #return AlgProc
    elif mm == 'adjacent':
        #return AlgProc
    else:
        pass

def reduceMethod(rm, T, iterator):
    if rm == 'linear':
        chillLinear(T, x)
    elif rm == 'geometric'
        chillGeometric(T, alpha)
    elif rm == 'log':
        chillLog(T, iterator)
    else:
        pass

def SAA():
    AlgProc = Processes.copy()
    T = T0
    pi = 5
    while T > Tend:
        for k = 1 in range(1,L):
            i = random.randint(1,N)
            j = random.randint(1,N)
            pi_new = moveMethod(mm,i,j,pi, AlgProc)
            if Cmax(pi_new) > Cmax(pi):
                r = random.random()
                p = probability(pi, pi_new)
                if r >= p:
                    pi_new = pi
            pi = pi_new
            if Cmax(pi) < Cmax(pi_new):
                pi_new = pi
        T = reduceMethod(rm, T)
    return T

