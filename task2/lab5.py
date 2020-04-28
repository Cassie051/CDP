import data, sys, time
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

def PDinit():
    bits = (2**(N))-1
    F = []
    F.append(0)
    for j in range(1, 2**(N)):
        F.append(-1)
    return PDr(F, bits)

def PDr(F, bits):
    result = int(sys.maxsize)
    for i in range(0, N):
        if not(bits&(1<<i) == 0):
            if (bits == 0):
                return 0
            previous_time = 0
            new_bits = bits&(~(1<<i))
            if (F[new_bits] == -1):
                F[new_bits] = PDr(F, new_bits)

            for j in range(0, N):
                if not(bits&(1<<j) == 0):
                    previous_time += PDProcesses[j].p
            # current_penalty = PDProcesses[i].w * max(0, previous_time-PDProcesses[i].d)
            # result = min(result, current_penalty + F[new_bits])
            result = min(result, max(previous_time - PDProcesses[i].d, 0) * PDProcesses[i].w + F[new_bits])
    return result

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


start = time.time()
print("\nPDi calculate:", PDi(PDProcesses))
end = time.time()
print(end-start)

start = time.time()
print("\nPDr calculate:", PDinit())
end = time.time()
print(end-start)

