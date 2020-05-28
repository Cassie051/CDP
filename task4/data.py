filepath = 'D:/Git/CDP/task4/dane/ta005.txt'

with open(filepath) as fp:
    first_line = " ".join(fp.readline().split())
    first_second = " ".join(fp.readline().split())

    # added parameters from file
    NMfirst_line = first_second.split()
    n = int(NMfirst_line[0])
    m = int(NMfirst_line[1])

    tmp = []
    hel = []
    for i in range (n):
        hel.append([int(m) for m in fp.readline().split()])

    for i in range (n):
        new =[]
        for j in range(1, len(hel[0]), 2):
            new.append(hel[i][j])
        tmp.append(new)

data = [[0 for i in range(n)] for j in range(m)]

for i in range(n):
    for j in range(m):
        data[j][i] = tmp[i][j]