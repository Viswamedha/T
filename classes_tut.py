
# variables / code
# function
# class - grouping
# module / python file

# make another class
# takes in 4 parameters - first name, last name, date of birth, favourite colour
# 1 function print out first and last name on one line
# 2 function print out their current age based on date of birth (DD/MM/YYYY) - we only care about years
# 3 prints out their favourite colour the number of tiems their age is, so if my age was 17, print it out 17 times


class Duo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def p(help):
        print(help.a)
        print(help.b)

a = Duo("Vish","Dies")
a.p()
input()

# separate collection of variables and instances
# every function inside the class must reference to the class - self
# classname.attributename -> attribute is a variable that belongs to the class itself
class Test:
    def __init__(self, a):  # self = <Test object>
        self.a = a  # Test.a = value of a

    def p(self):
        print(self.a)

b = Test("Hi") # create an instance / copy of the class where the variable a is "Hi"
b.p()

# make your own class - take in 2 parameters and then print out both in a separate funtion
input()

# def __init__():


# import python_file


#profile
class Main:

    def __init__(self, name):
        self.name = name
    
    def p(self):
        print(self.name)


# objects / instance - a temporary copy of a class which is seperate to the original class



a = Main("Vish")
a.p()


# class - take in 2 parameters and print them out! 



