name = input("What is your name (full): ")
date = input("What is your date of birth in a dd/mm/yyyy format:")
def details(name,details):
    dates = date.split("/")
    dates2 = dates[2]
    year = int(2020) - int(dates2)
    print("You are " + str(year) + " years old")
    name = name.split(" ")
    fname = name[0]
    lname = name[1]
    fletter = fname[0]
    email = dates2 + fletter + lname + "@gmail.com"
    print("A suggested email for you is " + str(email) )
#a=details(name,date)


color = input("Please enter a color, I will check if it is valid: ")
def colour(color):
    z = open("colours.txt","r")
    y = z.readlines()
    z.close()
    if color in y:
        print("Valid colour")
    else:
        print("Invalid colour")
a = colour(color)
