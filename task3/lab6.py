import data


Data = data.data.copy()
N = data.n
M = data.m


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
        
