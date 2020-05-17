import data, lab6
import sys

Processes = data.data
N = data.n
M = data.m

def initBnB(BProcesses):
    pi = []
    for j in BProcesses:
        BnB(j, BProcesses, pi)

    def BnB(j, BProcesses, pi):
        UB = int(sys.maxsize)
        pi.append(j)
        BProcesses.remove(j)
        if(len(BProcesses) != 0):
            LB =  Bound(pi)
            if(LB <= UB):
                for j in BProcesses:
                    BnB(j, BProcesses, pi)
        else:
            Cmax =  lab6.Cmax(BProcesses)
            if(Cmax < UB):
                UB = Cmax
                result = pi         # zapamietujemy najlepsza permutacja

    def Bound(pi):
        