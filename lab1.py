#otwarcie pliku i czytanie pierwszej linii
f = open('dane/data200.txt')
first_line = " ".join(f.readline().split())

#przypisanie ilośći zadań i parametrów
NKfirst_line = first_line.split()
n = int(NKfirst_line[0])
k = int(NKfirst_line[1])

#utworzenie tablic dla parametrów
rows = []

class Row:
  def __init__(self, r, p, q):
    self.r = r
    self.p = p
    self.q = q


#podział parametrów
for x in f:
    next_lines = x.split()
    rows.append(Row(int(next_lines[0]), int(next_lines[1]), int(next_lines[2])))
f.close()

Rrows = rows.copy()
RQrows = rows.copy()

#algorytm optymalizujący
def calculate(rows):
    s = []
    C = []
    s.insert(0, rows[0].r)
    C.insert(0, (s[0] + rows[0].p))
    Cmax = C[0] + rows[0].q
    for i in range(1, n):
        s.append(max([rows[i].r, C[i-1]]))
        C.append(s[i]+rows[i].p)
        Cmax = max([Cmax, (C[i]+rows[i].q)])
    print (Cmax)

# Sort def

def Rsort(rows):
    rows.sort(key=lambda x: (x.r))
    return (calculate(rows))

def RQsort(rows):
    rows.sort(key= lambda x: (x.r, x.q))
    return (calculate(rows))

calculate(rows)
Rsort(Rrows)
RQsort(RQrows)