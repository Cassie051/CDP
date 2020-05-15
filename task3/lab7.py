import data
import sys

Processes = data.data
N = data.n
M = data.m

def Johnson(jProcesses):
    l = 0
    k = N
    minP = int(sys.maxsize)
    result = [0]*(k-1)
    minN = 0

    while (len(jProcesses)!= 0):
        for i in range(0, len(jProcesses)-1):
            for j in range(0, M):
                minP = min(jProcesses[i][j], minP)
                if(minP == jProcesses[i][j]):
                    minN = i
                    minM = j
        if (jProcesses[minN][0] < jProcesses[minN][1]):
            result.insert(l, minP)
            l += 1
            minP = int(sys.maxsize)
        else:
            result.insert(k, minP)
            k -= 1
            minP = int(sys.maxsize)
        jProcesses.remove(jProcesses[minN])

    return result

print(Processes[0][0])
print(Johnson(Processes))
