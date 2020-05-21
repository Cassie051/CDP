import data, lab6
import sys
import time

Processes = data.data
N = data.n
M = data.m

def Johnson(jProcesses):
    l = 0
    k = N - 1
    minP = int(sys.maxsize)
    result = [[0 for i in range(2)] for j in range(k+1)]
    minN = 0

    while (len(jProcesses)!= 0):
        for i in range(0, len(jProcesses)):
            for j in range(0, M):
                minP = min(jProcesses[i][j], minP)
                if(minP == jProcesses[i][j]):
                    minN = i
                    minM = j
        if (jProcesses[minN][0] < jProcesses[minN][1]):
            result[l] = jProcesses[minN]
            l += 1
            minP = int(sys.maxsize)
        else:
            result[k] = jProcesses[minN]
            k -= 1
            minP = int(sys.maxsize)
        jProcesses.remove(jProcesses[minN])
    return lab6.Cmax(result)

start = time.time()
print(Johnson(Processes))
end = time.time()
T = end - start
print("TIME: ",T*1000)