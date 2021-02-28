data = str(input())
data = list(data)
m = []
while len(data) > 1:
    for i in range(len(data)):
        if i+1 == len(data): break
        if [data[i],data[i+1]] in [["R","R"],["G","G"],["B","B"]]:
            m.append(data[i])
        elif [data[i],data[i+1]] in [["R","G"],["G","R"]]:
            m.append("B")
        elif [data[i],data[i+1]] in [["R","B"],["B","R"]]:
            m.append("G")
        elif [data[i],data[i+1]] in [["B","G"],["G","B"]]:
            m.append("R")
    data = m
    m = []
print(data)
    
    
    






