ask = 1
snum = 0
def one(ask,snum):
    num = 1
    while num != 0:
        num = int(input("Please enter a number: "))
        sum1 = num + snum
        snum = sum1
    return snum
a = one(ask,snum)
print("The sum of your numbers are " + str(a))


ask = 1
snum = 1
def two(ask,snum):
    num = 0
    while num != 1:
        num = int(input("Please enter a number: "))
        sum1 = num * snum
        snum = sum1
    return snum
z = two(ask,snum)
print("The product of your numbers are " + str(z))




    
def three(ask):
    if ask == "no":
        username = input("Please enter the username you want to use: ")
        password = input("Please enter a password: ")
        pass2 = input("Re-enter the password: ")
        newaccount = username + " " + pass2
        if password == pass2:
            l = open("details.txt","a")
            l.write(newaccount)
            l.close()
        return
    else:
        l = open("details.txt","r")
        m = l.readlines()
        l.close()
        username = input("What is your username: ")
        password = input("What is your password: ")
        account = username + " " + password
        return password, pass2, account, m


ask = input("Do you have an account: ")
n = three(ask)
password = n[0]
pass2 = n[1]
account = n[2]
m = n[3]
if password == pass2:
    print("Account created")
else:
    print("Passwords do not match")
    print("Account creation failed")
if account in m:
    print("Logged in")
else:
    print("Credentials not recognised")
if ask != "yes" or ask != "no":
    print("invalid input")

value = int(input("What is your starting number: "))
power = int(input("To the power of: "))
def six(value, power):
    count = 2
    ogval = value
    indice = power
    while count <= power :
        ogval = ogval * value
        count = count + 1
    return ogval

c = six(value,power)
print(str(c))

import random
letter = input("Please enter a letter: ")
number = 0
def fourfive(letter,number):
    while number == 0:
        f = open("words2.txt","r")
        words = f.readlines()
        f.close()
        word = random.choice(words)
        for i in word:
            word = i.strip("\n")
            word.append(f)
        fletter = word[0]
        if fletter == letter:
            number = 1
            return word
            break
        else:
            number = 0

b = fourfive(letter,number)
print(b)


def seven(a,z,c):
    full = str(a) + " " + str(z) + " " + str(c)
    return full
d = seven(a,z,c)
print(d)
