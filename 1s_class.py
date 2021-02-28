'''
a = 0
b = "hello"
c = [4,5,6,7,"hello","i am alive"]
# c[index]
# tuples use ()
d = {}

# key - value system
# "keyname": "value"

d = {"keyname": "value", "keyname2": "value2"}

# adding - defining directly into the dictionary
# dictionaryname[keyname] = "value"
d["keyname3"] = "value3"

# overwriting data - exactly the same as adding
d["keyname2"] = "strawberries"

# deleting item from dictionary
del d["keyname"]

# fetching
# fetching from a list simply is a for i in listname:
# for i in dictname: 
#   print(i)  -> all the keys in the dictionary
for i in d:
    print(i)

# for values 
# we need to speficy dictname[keyname]
for i in d:
    print(d[i])
'''

# 1 class
# all inputs and function inside class, login and signup
# stores everything in a dictionary - while 
# final function that prints the contents of the dictionary