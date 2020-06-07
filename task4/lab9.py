import data, sys
import copy
import time

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

def CNeh(CProcesses):
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

    return endList

def Neh(NProcesses):
    k = 0
    W = []
    pi = [[] for j in range(M)]
    pitmp = [[] for j in range(M)]
    tabj = []
    for i in range(N):
        tmp = 0
        for j in NProcesses:
            tmp += j[i]
            tabj.insert(len(tabj), j[i])
        W.append([tmp, tabj.copy()])
        del tabj[0:]
    W.sort(key = lambda x: x[0])
    while len(W) != 0 :
        j = W[len(W)-1][1]
        for i in range(len(j)):
            pi[i].append(j[i])
        pitmp = copy.deepcopy(pi)
        for l in range(0, k):
            if k>0:
                for i in range(len(j)):
                    pitmp[i][k-l], pitmp[i][k-l-1] = pitmp[i][k-l-1], pitmp[i][k-l]
            if Cmax(pitmp) < Cmax(pi):
                pi = copy.deepcopy(pitmp)
        del W[len(W)-1]
        k += 1
    return Cmax(pi)

def Select(Wj, pi, case):
    if(case == 1):
        # najdluzsza operacja na sciezce krytycznej
        return "nothing"
    elif(case == 2):
        # najwieksza suma operacji wchodzacych na sciezke krytyczna
        List = CNeh(pi)
        for i in range(len(List)-1, 0):
            for j in range(len(List[0])-1, 0):
                tmp = List[i][j]
    elif(case == 3):
        # najwieksza liczba operacji wchodzacych na sciezke krytyczna
        return "nothing"
    elif(case == 4):
        # najwieksze zmniejszenie Cmax
        tpi = copy.deepcopy(pi)
        elier = -2
        ref = Cmax(pi)
        tmptask = [0 for i in range(len(pi))]
        for j in range(len(pi[0])):
            for i in range(len(pi)):
                tmptask[i] = pi[i][j]
                del pi[i][j]
            if tmptask == Wj:
                pi = copy.deepcopy(tpi)
            else:
                tmp = Cmax(pi)
                if elier == -2:
                    elier = tmp
                    task = copy.deepcopy(tmptask)
                elif ref-elier < ref-tmp:
                    task = copy.deepcopy(tmptask)
                pi = copy.deepcopy(tpi)
        return task

def NehPlus(NProcesses):
    k = 0
    W = []
    pi = [[] for j in range(M)]
    pitmp = [[] for j in range(M)]
    tabj = []
    flag = -1
    for i in range(N):
        tmp = 0
        for j in NProcesses:
            tmp += j[i]
            tabj.insert(len(tabj), j[i])
        W.append([tmp, tabj.copy()])
        del tabj[0:]
    W.sort(key = lambda x: x[0])
    while len(W) != 0 :
        j = W[len(W)-1][1]
        for i in range(len(j)):
            pi[i].append(j[i])
        pitmp = copy.deepcopy(pi)
        for l in range(0, k):
            if k>0:
                for i in range(len(j)):
                    pitmp[i][k-l], pitmp[i][k-l-1] = pitmp[i][k-l-1], pitmp[i][k-l]
            if Cmax(pitmp) < Cmax(pi):
                pi = copy.deepcopy(pitmp)
        del W[len(W)-1]
        flag += 1

        if(flag > 1):
            x = Select(j, copy.deepcopy(pi), 4)
            pitmp = copy.deepcopy(pi)
            for l in range(0, k):
                if k>0:
                    for i in range(len(x)):
                        pitmp[i][k-l], pitmp[i][k-l-1] = pitmp[i][k-l-1], pitmp[i][k-l]
                if Cmax(pitmp) < Cmax(pi):
                    pi = copy.deepcopy(pitmp)
        k += 1
    # print(pi)
    return Cmax(pi)


start = time.time()
print(Neh(Processes))
end = time.time()
T = end - start
print(T)

start = time.time()
print(NehPlus(Processes))
end = time.time()
T = end - start
print(T)