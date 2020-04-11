import data, sys
import itertools as it

WProcesses = data.AllProcesses.copy()

N = data.n

def WiTi(WProcesses):
	Processes = WProcesses.copy()
	S = []
	C = []
	T = []
	F = 0
	Clast = 0
	for j in range(0, N):
		S.append(Clast)
		C.append(S[j] + Processes[j].p)
		T.append( max((C[j] - Processes[j].d), 0))
		Clast = C[j]
	for j in range(0, N):
		F += Processes[j].w * T[j]
	return F

def sortD(Processes):
	Processes.sort(key=lambda x: (x.d))
	return (WiTi(Processes))

def BruteForce(WProcesses):
	Processes = WProcesses.copy()
	minimal_value = sys.maxsize

	for p in Permutation(N_elements(N)):
		single_combi = []
		single_combi = p.copy()
		rearanged = Rearange(single_combi,Processes)
		current_value = WiTi(rearanged)
		if current_value < minimal_value :
			minimal_value = current_value

	return minimal_value

# zmiana kolejności danych, użytych później w WiTi
def Rearange(single_combi, Procesess):
	rearanged_list = []
	for x in range (N):
		rearanged_list.insert(single_combi[x], data.Process(Procesess[x].p, Procesess[x].w, Procesess[x].d))
	return rearanged_list

def N_elements(N):
	index = []
	for i in range(0,N):
		index.append(i)
	return (index)

def Permutation(lst):
	if len(lst) == 0:
		yield []
	elif  len(lst) == 1:
		yield (lst)
	else:
		for i in range(len(lst)):
			x = lst[i]
			xs = lst[:i] + lst[i+1:]
			for p in Permutation(xs):
				yield ([x]+p)


print (BruteForce(WProcesses))
