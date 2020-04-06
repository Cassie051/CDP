from queue import PriorityQueue
import data, lab1


def RsortMIN(rows):
    rows.sort(key=lambda x: (x.r))
    return rows[0]

def QsortMAX(rows):
    rows.sort(key=lambda x: (x.q))
    return rows[len(rows)-1]


# Schrage algorithm
def schrage(rows):
    i = 1
    G = []
    N = rows.copy()
    pi = []
    t = RsortMIN(N).r
    while (len(G)!=0 or len(N)!=0):
        while (len(N)!=0 and RsortMIN(N).r <= t):
            j = RsortMIN(N)
            G.append(j)
            N.remove(j)
        if (len(G)!=0):
            j = QsortMAX(G)
            G.remove(j)
            pi.insert(i, j)
            t += int(j.p)
            i = i+1
        else:
            t = RsortMIN(N).r
    return pi



# Schrage algorithm on queue
def schrageOnQueue(rows):
    i = 1
    G = PriorityQueue()
    N = PriorityQueue()
    temp = rows.copy()
    for k in range(0, len(temp)):
        N.put((temp[k].r, temp[k]))
    pi = []
    t = RsortMIN(temp).r
    tcheck = 0
    while (not G.empty()) or (not N.empty()):
        while (not N.empty()) and (tcheck == 0):
            j = N.get()[1]
            if (int(j.r) <= t):
                G.put((-j.q, j))
            else:
                N.put((j.r, j))
                tcheck = 1
        if (not G.empty()):
            j = G.get()[1]
            pi.insert(i, j)
            t += int(j.p)
            i = i+1
            tcheck = 0
        else:
            j = N.get()[1]
            t = int(j.r)
            N.put((j.r, j))
            tcheck = 0
    return pi






