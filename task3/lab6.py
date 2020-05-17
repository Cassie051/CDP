import data

<<<<<<< Updated upstream
=======
def Cmax(CProcesses):
    Cstart = 0
    Cend = 0
    endList = [[0 for i in range(M)]  for j in range(N)]
    startList = [[0 for i in range(M)]  for j in range(N)]
    for i in range(0, len(CProcesses)-1):
        for j in range(0, M):
            if(i == 0):
                Cstart = Cend
                Cend = Cstart + CProcesses[i][j]
            else:
                if(j == 0):
                    Cstart = endList[i-1][j]
                else:
                    Cstart = max(endList[i-1][j], Cend)
                Cend = Cstart + CProcesses[i][j]
>>>>>>> Stashed changes

Data = data.data.copy()
N = data.n
M = data.m

<<<<<<< Updated upstream

#def optimal():



def FlowShop():
    for i in range(len(Data)):
        element = 1
        for j in Data:
            Data[Data.index(j)] = j[0::1]
            Data[Data.index(j[0::1])].append(element)
            element = element + 1 
    print(Data)

FlowShop()
        
=======
# not works yet
# def BruteForce(BProcesses):
# 	minimal_value = []
# 	minimal_value.append(sys.maxsize)
# 	machine = 0
# 	Elem = N_elements(data.n)
# 	while machine < data.m:
# 		for p in Permutation(Elem):
# 			single_combi = []
# 			single_combi = p.copy()
# 			rearanged = Rearange(single_combi,Processes,machine)
# 			current_value = Cmax(rearanged)
# 			if current_value < minimal_value[machine] :
# 				minimal_value[machine] = current_value
# 	return minimal_value[machine]

# def Permutation(lst):
# 	if len(lst) == 0:
# 		yield []
# 	elif  len(lst) == 1:
# 		yield (lst)
# 	else:
# 		for i in range(len(lst)):
# 			x = lst[i]
# 			xs = lst[:i] + lst[i+1:]
# 			for p in Permutation(xs):
# 				yield ([x]+p)

# def N_elements(N):
# 	index = []
# 	for i in range(0,N):
# 		index.append(i)
# 	return (index)


# def Rearange(single_combi, Procesess, machine):
# 	rearanged_list = []
# 	for x in range (N):
# 		rearanged_list.insert(single_combi[x], Procesess[x][machine])
# 	return rearanged_list

# print(BruteForce(Processes))
>>>>>>> Stashed changes
