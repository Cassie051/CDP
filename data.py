# open and red file
f = open('dane/data10.txt')
first_line = " ".join(f.readline().split())

# added parameters from file
NKfirst_line = first_line.split()
n = int(NKfirst_line[0])
k = int(NKfirst_line[1])

# making calss Row
rows = []

class Row:
  def __init__(self, r, p, q):
    self.r = r
    self.p = p
    self.q = q


# added data to row
for x in f:
    next_lines = x.split()
    rows.append(Row(int(next_lines[0]), int(next_lines[1]), int(next_lines[2])))
f.close()