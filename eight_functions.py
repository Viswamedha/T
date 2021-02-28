# 8 functions - avoid using print statements and inputs inside function
# 1 adder - will keep asking user until they type 0, then add it togehtor
# 2 multiplies - same as above ^
# 3 create a login system - stores it permanently on a text file - separated by new lines - reenter password twice
# 4/5 a function that gives the user a random 5 or 6 letter word but the first letter must match their chosen one - input for 1 letter (2 functions - a funciton in a function)
# 6 a^b 
# 7 all the values from 1 - 6 must be stored on one line and printed out in order
# 8 will be on a separate file and call each of these functions in order
# 120 lines limit
def adder():
    aaa = int(input('What is your number?: '))
    count = 0
    while aaa != 0:  
        count = count + aaa
        aaa = int(input('What is your number?: '))
    return count

def multiplier():
    bbb = int(input('What is your number?: '))
    order = 0
    while bbb != 0:
        order = order * bbb
        bbb = int(input('What is your number?: '))
    return order

def login(username, password, reenter):
    if password == reenter:
        f = open('login.txt','a+')
        f.write(username+" "+password)
        f.close()
        return "done"
    return "Passwords dont match"

def four(letter):
    f = open('wordlist.txt','r')
    g = f.read()
    words = g.split('/n')
    f.close()
    for word in words:
        if word[0] == letter and (len(word) == 5 or len(word) == 6):
            return word
    return "Word not found"

def six(a, b):
    ti = 1
    for i in range(0, b):
        ti = ti * a
        return ti

def seven(count, order, username, password, word):
    nu = str(count) + " " + str(order) + " " + str(username) + " " + str(password) + " " + str(word) + " " 
    return nu