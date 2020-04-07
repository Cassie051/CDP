import data, sys
import itertools as it

WProcesses = data.AllProcesses.copy()


def WiTi(WProcesses):
	Processes = WProcesses.copy()
	S = []
	C = []
	T = []
	F = 0
	N = data.n
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

def BruteForce(Processes):
	N = data.n
	result = []
	MINresult = 0
	najlepszyWynik = int(sys.max)
	# PermProcess = it.permutations(Processes, N)
	# for i in range(0, N):
	# 	result.append(PermProcess.__next__())
	# 	MINresult = min(MINresult, result[i])
	# return MINresult
	PermProcess = list(it.permutations(Processes, N))
	for i in range(0, N):
		obecnyWynik = WiTi(PermProcess[i])
		if(obecnyWynik <= najlepszyWynik):
			najlepszyWynik = obecnyWynik
			najlepszaPermutacja = PermProcess[i]
	return najlepszaPermutacja



print(BruteForce(WProcesses))