from queue import PriorityQueue
import data, lab1, sys

Srows = data.rows

def RsortMIN(rows):
    rows.sort(key=lambda x: (x.r))
    return rows[0]

def QsortMAX(rows):
    rows.sort(key=lambda x: (x.q))
    return rows[len(rows)-1]
        
# SchragePmtn algorithm
def schragePmtn(rows):
    Cmax = 0
    Ng = []
    N = rows.copy()
    t = 0
    l = data.Row(0, 0, 0)
    while (len(Ng)!=0) or (len(N)!=0):
        while (len(N)!=0) and (RsortMIN(N).r <= t):
            j = RsortMIN(N)
            Ng.append(j)
            N.remove(j)
            if j.q > l.q:
                l.p = t - j.r
                t = j.r
                if l.p > 0:
                    Ng.append(l)
        if len(Ng)==0:
            t = RsortMIN(N).r
        else:
            j = QsortMAX(Ng)
            Ng.remove(j)
            l = j
            t += j.p
            Cmax = max(Cmax, (t + j.q))
    return Cmax

print("Normal SchragePmtn calculate:", schragePmtn(Srows))


# SchragePmtn algorithm on queue
def schragePmtnOnQueue(rows):
    Cmax = 0
    Ng = PriorityQueue()
    N = PriorityQueue()
    temp = rows.copy()
    for k in range(0, len(temp)):
        N.put((temp[k].r, temp[k]))
    t = 0
    l = data.Row(0, 0, int(sys.maxsize))
    tcheck = 0
    while (not Ng.empty()) or (not N.empty()):
        while (not N.empty()) and (tcheck == 0):
            j = N.get()[1]
            if (int(j.r) <= t):
                Ng.put((-j.q, j))
            else:
                N.put((j.r, j))
                tcheck = 1
            if j.q > l.q:
                l.p = t - j.r
                t = j.r
                if l.p > 0:
                    Ng.put((-l.q, l))
                tcheck = 0
        if Ng.empty():
            j = N.get()[1]
            t = int(j.r)
            N.put((j.r, j))
            tcheck = 0
        else:
            j = Ng.get()[1]
            l = j
            t += int(j.p)
            Cmax = max(Cmax, (t + j.q))
            tcheck = 0
    return Cmax

print("Queue SchragePmtn calculate:", schragePmtnOnQueue(Srows))

