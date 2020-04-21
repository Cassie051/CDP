import data, sys
import itertools as it

PDProcesses = data.AllProcesses.copy()

N = data.n

# def NotRepCombinations():
#     check = []
#     comb = []
#     help = []
#     index = []
#     for x in it.permutations('1100', 4 ):
#             check.append(x)
#     for i in range(0, len(check)):
#         help = check[i]
#         for j in range(0, len(check)):
#             if help == check[j]:
#                 flag = 1
#                 index.append(j)
#         if (flag):
#             for k in index:
#                 check.remove(check[k])
#                 flag = 0
#     return check

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


def PDi(PDProcesses):
    Processes = PDProcesses.copy()
    MinF = int(sys.maxsize)
    result = -1

    F = [[] for i in range(0, N)]
    for i in range(0, N):
        for j in range(0, int(2**(N))):
            F[i].append(-1)

    # prep the first (initial) iteretion of the matrix
    for i in range(0, N):
        if(Processes[i].p - Processes[i].d) > 0:
            F[i][1|(1<<i)] = (Processes[i].p - Processes[i].d)*Processes[i].w
        else:
             F[i][1|(1<<i)] = 0

    for r in range(2, N):
        for subset in Mask(r, N):
            for nextP in range(1, N):
                if(((1<<nextP)&subset) == 0):
                    continue
                subsetWithoutNext = subset^(1<<nextP)
                for end in range(1, N):
                    if (end==nextP or ((1<<end)&subset)==0):
                        continue
                    help = 0
                    for k in range(0, N):
                        if (not ((1<<k)&subset)) == 0:
                            help += Processes[k].p

                    if (help - Processes[nextP].d) > 0:
                        newF = F[end][subsetWithoutNext] + (help - Processes[nextP].d) * Processes[nextP].w
                        if(MinF > newF):
                            F[nextP][subset] = newF
                    # if((help + Processes[nextP].p - Processes[nextP].d) > 0):
                    #     help = (help + Processes[nextP].p - Processes[nextP].d) * Processes[nextP].w
                    # newF = F[end][subsetWithoutNext] + help
                    # if(newF < MinF) and (newF >= 0):
                    #     MinF = newF
                    # F[nextP][subset] = MinF

    MinResult = int(sys.maxsize)
    for i in range(0, N):
        if(F[i][2**(N)-1] < MinResult):
            MinResult = F[i][2**(N)-1]
        print(F[i][2**(N)-2])

    return MinResult


print(PDi(PDProcesses))


