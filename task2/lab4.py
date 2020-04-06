import data

WProcesses = data.allProcesses.copy()

def get_exectime(Processes, process_id):
  return int(Processes[process_id][0])

def get_weight(Processes, process_id):
  return Processes[process_id][1]

def get_deadline(Processes, process_id):
  return Processes[process_id][2]

def min_value(n):
  min_value = get_deadline(0)
  x = 1
  for x in range(n):
    if min_value > get_deadline(x):
      min_value = get_deadline(x)
  index = 0
  for index in range(n):
    if min_value == get_deadline(x):
      return index

def exclude_index(Processes, index):
    del Processes[index][0:2]


def WiTi(WProcesses):
    time = 0
    sum_pwd = 0
    tardiness = 0
    N = data.n
    Processes = WProcesses.copy()
    for i in range(N):
        min_time_index = min_value(N)
        time = sum_pwd + get_exectime(Processes, min_time_index)
        if time <= get_deadline(Processes, min_time_index):
            sum_pwd += get_exectime(Processes, min_time_index)
            exclude_index(Processes, min_time_index)
        elif time > get_deadline(Processes, min_time_index):
            tardiness += get_weight * (sum_pwd + get_exectime(Processes, min_time_index) - get_deadline(Processes, min_time_index))
    return tardiness

WiTi(WProcesses)