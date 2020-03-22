import data, lab1

Srows = data.rows

def RsortMIN(rows):
    rows.sort(key=lambda x: (x.r))
    return rows[0]

def QsortMAX(rows):
    rows.sort(key=lambda x: (x.q))
    return rows[len(rows)-1]
        

# Schrage algorithm
def schrage(rows):
    i = 1
    tlist = []
    G = []
    N = rows
    for j in range(0, len(N)):
        tlist.append(rows[j].r)
    t = min(tlist)
    tcheck = t
    while (not (len(G)!=0 or len(N)!=0)):
        while (not (len(N)!=0 and tcheck <= t)):
            j = RsortMIN(N)
            G.append(j)
            if j in N:
                N.remove(j)
        if (len(G)!=0):
            j = QsortMAX(G)
            if j in G:
                G.remove(j)
                rows.insert(i, j)
                t = int(j.p)
                i = i+1
            else:
                t = tcheck
    return rows

            



    


