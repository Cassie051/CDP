import data, sys
import itertools as it

PDProcesses = data.AllProcesses.copy()

N = data.n

# Mask set
def Mask(m, n):
    subsets = []
    NotRepCombinations(0, 0, m, n, subsets)
    return subsets

def NotRepCombinations(seter, at, m, n, subsets):
    if (n - at < m):
        return
    if (m == 0):
        subsets.append(seter)
    else:
        for i in range(at, n):
            seter |= 1 << i
            NotRepCombinations(seter, i + 1, m - 1, n, subsets)
            seter &= ~(1 << i)


# WiTi DP Iteration
def PDi(PDProcesses):
    Processes = PDProcesses.copy()
    result = -1

    F = [[] for i in range(0, N)]
    for i in range(0, N):
        for j in range(0, int(2**(N))):
            F[i].append(-1)

    # prep the first (initial) iteretion of the matrix
    for i in range(0, N):
        if(Processes[i].p - Processes[i].d) > 0:
            F[i][1<<i] = (Processes[i].p - Processes[i].d)*Processes[i].w
        else:
             F[i][(1<<i)] = 0
        # print(F[i][4])

    for r in range(2, N+1):
        for subset in Mask(r, N):
            for nextP in range(0, N):
                if(((1<<nextP)&subset) == 0):
                    continue
                subsetWithoutNext = subset^(1<<nextP)
                MinF = int(sys.maxsize)
                for end in range(0, N):
                    if (end==nextP or ((1<<end)&subset)==0):
                        continue
                    sumP = 0
                    for k in range(0, N):
                        if not (((1<<k)&subset) == 0):
                            sumP += Processes[k].p

                    if (sumP  - Processes[nextP].d) > 0:
                        newF = F[end][subsetWithoutNext] + (sumP - Processes[nextP].d) * Processes[nextP].w
                    else:
                        newF = F[end][subsetWithoutNext]
                    if(MinF > newF):
                        MinF = newF
                F[nextP][subset] = MinF

    MinResult = int(sys.maxsize)
    for i in range(0, N):
        if(F[i][2**(N)-1] < MinResult):
            MinResult = F[i][2**(N)-1]
    return MinResult


print(PDi(PDProcesses))


