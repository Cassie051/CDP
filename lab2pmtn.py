from queue import PriorityQueue
import data, lab1

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

