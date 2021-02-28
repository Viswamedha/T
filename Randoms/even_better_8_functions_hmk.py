# 8 functions - avoid using print statemnts and inputs inside function
# 1 adder - will keep asking user until they type 0, then add it togehtor
# 2 multiplies - same as above ^
# 3 create a login system - stores it permanently on a text file - separated by new lines - renter password twice
# 4/5 a function that gives the user a random 5 or 6 letter word but the first letter must match their chosen one - input for 1 letter (2 functions - a funciton in a fucntion)
# 6 a^b 
# 7 all the values from 1 - 6 must be stored on one line and printed out in order
# 8 will be on a separate file and call each of these functions in order
# 120 lines limit

def adder():
    number = 1
    count = 0
    while number != 0:
        number = int(input("Enter a number (0 will stop the program): "))
        count = count + number
    return count
def multiplier():
    number = 1
    count = 1
    while number != 0:
        count = count * number
        number = int(input("Enter a number (0 will stop the program): "))
    return count
def login(option,username,password,password2):
    if option:
        file = open("details.txt","r")
        data = file.read()
        file.close()
        data = data.split("\n")
        y = False
        for i in data:
            d = i.split(" ")
            if d[0]==username and d[1]==password:
                y = True
                break
        if y:
            return "Logged in successfully! "
        else:
            return "Invalid Credentials"
    else:
        if password==password2:
            file = open("details.txt","a")
            file.write(username+" "+password+"\n")
            file.close()
            return "Acc0unt created successfully!"
        else:
            return "Passwords do not match! "
def for_login():
    option = str(input("Do you have an account (yes/no)? "))
    if option=="yes":
        username = str(input("Uername: "))
        password = str(input("Password: "))
        x = login(True,username,password,"")
    elif option=="no":
        username = str(input("Uername: "))
        password = str(input("Password: "))
        password2 = str(input("Re-enter password: "))
        x = login(False,username,password,password2)
    else:
        return "Invalid option! "

    if x:
        return x
def word(letter):
    data = open("words.txt","r")
    words = data.read()
    data.close()
    words = words.split("\n")
    for i in words:
        print(i)
        if i[0] == letter and len(i) in [5,6]:
            return i
def power(number,exponent):
    count = 1
    for i in range(0,exponent):
        count = count*number
    return count


def print_all(adder_count,multiplier_count,login_message,word,power_count):
    print(str(adder_count)+" "+str(multiplier_count)+" "+str(login_message)+" "+str(word)+" "+str(power_count))