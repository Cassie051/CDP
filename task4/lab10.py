import data
import random
import sys
import math


Processes = data.tmp.copy()
N = data.n
M = data.m

T0 = 100 #100 10000
L = int(math.sqrt(N)) #N N*N
x = T0/1000 #T0/10000 T0/100000
alpha = 0.97 #0,95 0,90
Tend = 1 #0.01 #0.001 0.0001
rm = 'l' #'l'  g' 'i'
mm = 'i' #'i' 't' 'a'

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
    return float(Ice_Cold_T)

def chillGeometric(T, alpha):
    Ice_Cold_T = T*alpha
    return float(Ice_Cold_T)

def chillLog(T, iterator):
    Ice_Cold_T = T/math.log(iterator+1)
    return float(Ice_Cold_T)

def moveMethod(mm, i, j, pi):
    if mm == 's':
        for x in range (M):
            pi[i][x], pi[j][x] = pi[j][x], pi[i][x]
             #prosta zamiana 
        return pi

    elif mm == 'i':
        for x in range(M):
            temp = pi[i][x]
            for y in range(N):
                if y < j and y < i: #elementy są przed wyciąganym i jego miejscem
                    pass
                elif y < j and y > i: #elemetny pomiędzy elementem wyciągniętym i jego miejscem
                    pi[y][x] = pi [y-1][x]
                elif y > j and y < i: #elementy pomiędzy miejscem i elementem wyciągniętym
                    pi[y][x] = pi [y+1][x]
                elif y > j and y > i: #elementy po miejscach interaktywych
                    pass
                else:
                    pass
        return pi

    elif mm == 't':
        if i > j:
            a = j
            b = i
        else:
            a = i
            b = j #przypisuje na przyszłość indeksy do wygodniejszego używania

        for x in range(M):
            while a < b:
                pi[a][x], pi[b][x] = pi[b][x], pi[a][x] #podmienia elementy
                a = i + 1   #przemieszcza indeksy
                b = b - 1
        return pi

    elif mm == 'a':
        first = pi[i][0]
        for x in range (1,M):
            if x == M-1 :
                pi[i][x] = first #zapamiętuje pierwszy element
            else:    
                pi[i][x] = pi[i][x-1] #cofa każdy z elementów
        return pi

    else:
        pass

def reduceMethod(rm, T, iterator):
    if rm == 'l':
         chill_Lin = chillLinear(T, x)
         return chill_Lin
    elif rm == 'g':
        chill_Geo = chillGeometric(T, alpha)
        return chill_Geo
    elif rm == 'i':
        chill_Log = chillLog(T, iterator)
        return chill_Log
    else:
        pass

def SAA():
    pi = Processes.copy()
    pi_best = pi 
    T = T0
    iterator = 0
    while T > Tend:
        for k in range(1,L):
            i = random.randint(1,N-1)
            j = random.randint(1,N-1)
            pi_new = moveMethod(mm,i,j,pi)
            if Cmax(pi_new) > Cmax(pi):
                r = random.random()
                p = probability(pi, pi_new)
                if r >= p:
                    pi_new = pi
            pi = pi_new
            if Cmax(pi) < Cmax(pi_best):
                pi_best = pi
        iterator += 1
        #print (iterator)
        T = reduceMethod(rm, T, iterator)
    return pi_best

print (Cmax(SAA()))