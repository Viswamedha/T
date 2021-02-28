import json
class signup:

    def sign(self):
        credentials = {}
        username = input("What would you like your username to be: ")
        password = input("What would you like your password to be: ")
        confirmation = input("Please re-enter your password: ")
        goat = "blob"
        while goat != "bob":
            if username and password == confirmation:
                credentials[username] = username
                credentials[password] = password
                file = open("credentials.json", "w")
                json.dump(credentials, file, indent = 1)
                file.close()
                goat = "bob"
            else:
                username = input("What would you like your username to be: ")
                password = input("What would you like your password to be: ")
                confirmation = input("Please re-enter your password: ")
    def login(self):
        lusername = input("What is your username: ")
        lpassword = input("What is your password: ")
        a = open("credentials.json", "r")
        b = json.load(a)
        a.close()
        if lusername in b and lpassword in b:
          print("Logged in")
          import calc.py
          y = calc()
          y.calculator 
        else:
          print("Wrong details")
        

z = signup()
z.sign()
z.login()