



# make a class <- takes in name, age, gender, height (cm)
# mutliply the age by height, divide by 200 and round it
# if they are male, add 5 points, if they are female add 4 points, and print it out 
# and then subtract the points by their age




def multiplier():
    bbb = int(input('What is your number?: '))
    count = 0
    while bbb != 0:
        count = count * bbb
        bbb = int(input('What is your number?: '))
    return count



def adder():
    aaa = int(input('What is your number?: '))
    count = 0
    while aaa != 0:
        count = count + aaa
        aaa = int(input('What is your number?: '))
    return count

#f = adder()
#print(f)
# taken 1 input
# made a counter
# while loop checking if input isnt equal to 0
# added to counter
# take another input 


# Lekha, you need to finish the functions and fix the 8th function asw
# Rithvik, Suhas
# class
# 3 functions
# 1 take in 4 numbers - lengths of a shape
# check if its a square and print "I am a square"
# 2 take in 2 words, print the longer one
# 3 take in 3 numbers, a, b, c    a^(b^c)  print the result out


class Main:
    def __init__(self, v1, v2, v3, v4, v5, v6, v7, v8, v9): self.v1,self.v2,self.v3,self.v4,self.v5,self.v6,self.v7,self.v8,self.v9, = v1,v2,v3,v4,v5,v6,v7,v8,v9
    def one(self): 
        if self.v1 == self.v2 == self.v3 == self.v4: print("I am a square! ")
    def two(self):
        if len(self.v5) > len(self.v6): print(self.v5)
        else: print(self.v6)
    def three(self): print(str(self.v7**(self.v8**self.v9)))
a = Main(2,2,2,2,"Hello","Blue",2,3,2)
a.one()
a.two()
a.three()






