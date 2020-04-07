import data

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


print(sortD(WProcesses))