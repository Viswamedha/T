class Info:
    def __init__(self, name, surname, dob, colour):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.colour = colour
    def fullname(self):
        print(self.name + self.surname)
    def age(self):
        year = int(self.dob[6:])
        birthyear = 2021 - year
        print(str(birthyear))
    def many(self):
        year = int(self.dob[6:])
        birthyear = 2021 - year
        woah = self.colour * int(birthyear)
        print(str(woah))
'''
name = str(input('What is your first name?: '))
surname = str(input('What is your surname?: '))
dob = str(input('What is your date of birth (DD/MM/YYYY)?: '))
colour = str(input('What is your favourite colour?: '))
a = Info(name, surname, dob, colour)
a.fullname()
a.age()
a.many()
'''

# make a class
# 4 numbers
# 4 separate functions to add all the combinations of the numbers (3 at a time)
# a,b,c,d    a+b+c  a+b+d  b+c+d  c+a+d


# 1 class
# all inputs and function inside class, login and signup
# stores everything in a dictionary
# final function that prints the contents of the dictionary


# make a detailed summary of everything u have learn in python as detailed as possible with some examples






# word - definition
# key - value

data = {
    "Name": "Suhas",
    "Age": 12,
    "Height": 15,
    "Weight": 200
}
data["Name"]
# mylist[indexvalue]
# mydict[keyname]
# for i in listname:
# i would be each element of the list
# for i in dictname:
# del mylist[0]
# del mydict[keyname]
# mylist.append(item)
# mydict[newkey] = newvalue
# changing name to Vish

# overwrite - keyname needs to be specified

