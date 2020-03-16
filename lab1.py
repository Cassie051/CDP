f = open('dane/data10.txt')
first_line = f.readline().split(" ")

n = int(first_line[0])
k = int(first_line[1])

r = []
p = []
q = []

for x in f:
    next_lines = x.split(" ")
    r.append(int(next_lines[0]))
    p.append(int(next_lines[1]))
    q.append(int(next_lines[2]))

f.close()

def calculate():
    s = []
    C = []
    s.insert(0, r[0])
    C.insert(0, (s[0] + p[0]))
    Cmax = C[0] + q[0]
    for i in range(1, n):
        s.append(max([r[i], C[i-1]]))
        C.append(s[i]+p[i])
        Cmax = max([Cmax, (C[i]+q[i])])
    return Cmax

def sorting():
        data.append(r)
        data.append(p)
        data.append(q)

print(calculate())
