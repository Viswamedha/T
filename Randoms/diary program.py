'''
horizon
zebra
cars
notre-dame
clear
'''


a = open("data.txt","r")
b = a.read()
a.close()
b = b.split("\n") #['horizon', 'zebra', 'cars', 'notre-dame', 'clear']


changed  = False
x = True
f=""

while x:
    changed = False
    for i in range(0,5):
        if i+1 == 5:
            break
        if b[i+1] < b[i]:
            f = b[i]
            b[i] = b[i+1]
            b[i+1] = f
            changed = True
    if changed == False:
        break
for i in b:
    print(i)




