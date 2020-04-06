import data


# optimal algorithm
def calculate(rows):
    s = []
    C = []
    s.insert(0, rows[0].r)
    C.insert(0, (s[0] + rows[0].p))
    Cmax = C[0] + rows[0].q
    for i in range(1, data.n):
        s.append(max([rows[i].r, C[i-1]]))
        C.append(s[i]+rows[i].p)
        Cmax = max([Cmax, (C[i]+rows[i].q)])
    return Cmax

# Sort def

def Rsort(rows):
    rows.sort(key=lambda x: (x.r))
    return (calculate(rows))

def RQsort(rows):
    rows.sort(key= lambda x: (x.r, x.q))
    return (calculate(rows))

