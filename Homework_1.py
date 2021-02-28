# 3 inputs
# 1 someones profile - title firstname lastname  - split it any way u want (input will always contain spaces between title, name and lastname)
# 2 date of birth 14/12/03 - will always contain 2 slashes
# 3 school name - unknown
# 15vnalabotu@schoolname.bham.sch.uk

#variable[ : ]

#a="The brown fox jumps over the lazy dog. "
#b = a.split(" ")
#print(b)   ["The","brown","fox","jumps","over","the","lazy","dog."]

# Mr Viswamedha Nalabotu
# 14/12/03
# camphillboys


profile = str(input("Enter title, first name and last name: "))
dob = str(input("Enter DOB in format dd/mm/yy "))
name = str(input("Enter school name: "))
data = profile.split(" ")
fname = data[1]
lname = data[2]
data2 = dob.split("/")
month = int(data2[1])
year = int(data2[2])
if month > 9:
    y = year + 11
else:
    y = year + 12
email = str(y) + fname[:1] + lname + "@" + name + ".bham.sch.uk" 
print(email)
