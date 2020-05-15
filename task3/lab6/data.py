filepath = 'D:/Projekty/SPD/lab6/fsp/data001.txt'
with open(filepath) as fp:
    first_line = " ".join(fp.readline().split())

    # added parameters from file
    NMfirst_line = first_line.split()
    n = int(NMfirst_line[0])
    m = int(NMfirst_line[1])

    data = []
    for i in range (n):
       data.append([int(j) for j in fp.readline().split()])