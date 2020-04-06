# open and read file
f = open('dane/data10.txt')
first_line = " ".join(f.readline().split())

# added parameters from file
NK = first_line.split()
n = int(NK[0])
k = int(NK[1])
i = 0


allProcesses = []

# add elements to list
for i in range(n):
  singleProcess = list(map(int, f.readline().split()))
  allProcesses.append(singleProcess)

# close file
f.close()