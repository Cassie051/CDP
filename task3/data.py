filepath = 'D:/Projekty/CDP/task3/dane/data001.txt'
with open(filepath) as fp:
    first_line = " ".join(fp.readline().split())

    # added parameters from file
    NMfirst_line = first_line.split()
    n = int(NMfirst_line[0])
    m = int(NMfirst_line[1])

    data = []
    hel = []
    for i in range (n):
        hel.append([int(m) for m in fp.readline().split()])

    for i in range (n):
        new =[]
        for j in range(1, len(hel[0]), 2):
            new.append(hel[i][j])
        data.append(new)

#print (n)