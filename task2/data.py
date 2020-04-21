# open and read file
f = open('D:/Git/CDP/task2/dane/data11.txt')
first_line = " ".join(f.readline().split())

# added parameters from file
NKfirst_line = first_line.split()
n = int(NKfirst_line[0])
k = int(NKfirst_line[1])

# making calss Process
AllProcesses = []

class Process:
	def __init__(self, p, w, d):
		self.p = p
		self.w = w
		self.d = d

# add elements to list
for x in f:
		next_lines = x.split()
		AllProcesses.append(Process(int(next_lines[0]), int(next_lines[1]), int(next_lines[2])))
f.close()

# close file
f.close()