int(var) # str / float to int
str(var) # int / float to str
list(var) # str to list
"".join(var) # list to str

True
False

'''
>
<
>=
<=
==
!=

+
-
*
/
'''

var = 0
var = ""
var = []
var = ["",0]

for (incremental)
for i in var/list :
for i in range(0,len(var/list)):


while (conditional)
while var > 0:
    
read - r
(over)write - w
append - a

var = open("filename.txt", "mode - r/w/a")
#r
a = var.read()     "askfaskfdsfsdfksdfhsdkfsdkfsdkfsdf"
b = var.readlines()     ["askfaskfdsf","sdfksdfhsdkf","sdkfsdkfsdf"]
#w
var.write(contents)
#a
var.write(contents)
var.close()

a="The brown fox jumps over the lazy dog. "
b = a.split(" ")
print(b)   ["The","brown","fox","jumps","over","the","lazy","dog."]

a = "".join(b)
print(a)


b = [["pencilcase",2],["lunchbox",4]]

for i in b:
    for j in i:
        print(j)
    

#  0,1,2,3,4,5,6
a=["a","b","c","d","e","f","g"]
for i in range(0, 7):
    if i == 5:
        pass
    else:
        print(a[i])

class old(object):
    
    def func():
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        c = int(input("Number 3: "))

        s=[]

        s.append(a)
        s.append(b)
        s.append(c)

        for x in range(3):
            print(s[x])

    def func2():
        print("4+5=9")


class new:
    def func2():
        print("1+2=4")
  
import new2


def a(items):
    return items


f = new2.old()
f.func()

# code
# functions
# classes - object / instance
# module