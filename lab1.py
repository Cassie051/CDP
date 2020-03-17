#otwarcie pliku i czytanie pierwszej linii
f = open('dane/data100.txt')
first_line = f.readline().split(" ")

#przypisanie ilośći zadań i parametrów
n = int(first_line[0])
k = int(first_line[1])

#utworzenie tablic dla parametrów
r = []
p = []
q = []
Rsort = []
Psort = []
Qsort = []
index = []

#podział parametrów
for x in f:
    next_lines = x.split(" ")
    r.append(int(next_lines[0]))
    p.append(int(next_lines[1]))
    q.append(int(next_lines[2]))

f.close()

#algorytm optymalizujący
def calculate(r,p,q):
    s = []
    C = []
    #s.clear()
    #C.clear()
    s.insert(0, r[0])
    C.insert(0, (s[0] + p[0]))
    Cmax = C[0] + q[0]
    for i in range(1, n):
        s.append(max([r[i], C[i-1]]))
        C.append(s[i]+p[i])
        Cmax = max([Cmax, (C[i]+q[i])])
    print (Cmax)

#skopiowanie tablicy do pomocniczej
Rsort = r.copy()

#algorytm wyznaczający indexy do sortowania
Rsort.sort()
def index_tester():
    for i in range(0,n):
        for j in range(0,n):
            if Rsort[i]==r[j]:
                index.insert(i,j)
                #print(index[i])
        j+=j
    i+=i


#algorytm ustalający kolejności w 'p' i 'q'
def index_sort():
    for i in range(0,n):
        Psort.append(p[(index[i])])
        Qsort.append(q[(index[i])])


calculate(r,p,q)
index_tester()
index_sort()
calculate(Rsort,Psort,Qsort)
