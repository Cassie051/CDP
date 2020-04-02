import data, lab1, lab2, lab2pmtn, sys


def Bfind(I, Cmax):
    rows = I.copy()
    s = []
    C = []
    b = len(rows)
    s.insert(0, rows[0].r)
    C.insert(0, (s[0] + rows[0].p))
    for i in range(1, len(rows)):
        s.append(max([rows[i].r, C[i-1]]))
        C.append(s[i]+rows[i].p)
    for i in range(len(rows)-1, 1, -1):
        if (Cmax == (C[i] + rows[i].q)):
            return i
    return b

def Afind(I, Cmax, b):
    rows = I.copy()
    for a in range(0, b):
        psum = 0
        k = a
        for k in range(0, b):
            psum += rows[k].p
        if (Cmax == (rows[a].r + psum + rows[b].q)):
            return a
    return a

def Cfind(I, Cmax, b, a):
    rows = I.copy()
    c = 0
    for i in range(b, a, -1):
        if (rows[i].q < rows[b].q):
            return i
    return c

# Carlier algorithm
def carlier(rows):
    I = lab2.schrage(rows)
    U = lab1.calculate(lab2.schrage(I))
    pi = 0
    p = 0
    r = 0
    q = 0
    UB = int(sys.maxsize)
    if U < UB:
        UB = U
        pi = UB
    Cmax = lab1.calculate(I)
    b = Bfind(I, Cmax)
    a = Afind(I, Cmax, b)
    c = Cfind(I, Cmax, b, a)
    if c == 0:
        return pi
    for k in range(c+1, b):
        r = min(r, I[k].r)
        q = min(q, I[k].q)
        p += I[k].p
    crestore = I[c].r
    I[c].r = max(I[c].r, r + p)
    LB = lab2pmtn.schragePmtn(I)
    if LB < UB:
        carlier(I)
    I[c].r = crestore
    qrestore = I[c].q
    I[c].q = max(I[c].q, q+p)
    LB = lab2pmtn.schragePmtn(I)
    if LB < UB:
        carlier(I)
    I[c].q = qrestore
    return UB

