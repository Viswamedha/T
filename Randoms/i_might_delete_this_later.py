# imports JSON module so it is valid in the code
import json
# creates class called 'user' for login system
class user:
    # defines first function, which creates a dictionary
    def __init__(self):
        self.details = {}
    # defines function called 'store', whoch opens a JSON file and adds the dictionary from earlier into it
    def store(self):
        file = open("data.json", "w")
        json.dump(self.details, file, indent=4)
        file.close()
    # defines function called 'update', which opens aforementioned JSON file and assigns the dictionary to the loading of the file
    def update(self):
        file = open("data.json")
        self.details = json.load(file)
    # defines function called 'signup', which calls the 'update' and 'store' functions respectively, and creates a while loop that is get triggered, and asks for username, password and password confirmation
    def signup(self):
        self.update()
        # username, password, reenter password
        # if username 
        # if boolean   empty string = False   full string = True
        valid = False
        while valid == False:   # while not False   
            username = str(input("Username: "))
            password = str(input("Password: "))
            confirm = str(input("Confirm Password: "))
            # checks if there are inputs to all input statements and if the password and the password confirmation are identical, then assigns the password(value) to the username(key) in the dictionary
            if username and password and confirm and password == confirm:
                self.details[username] = password
                # overwrites 'valid' to be true, so the while loop will stop
                valid = True
        self.store()
    # defines 'login' function, which calls the 'update' function again and asks for username and password again
    def login(self):
        self.update()
        username = str(input("Username: "))
        password = str(input("Password: "))
        # if the username and password are in the dictionary, it 'logs in' the user, if not, the user gets a message saying 'Invalid!'
        if username in self.details:
            if self.details[username] == password:
                print("Valid! You are now logged in! ")
                return
        print("Invalid! ")
    # defines 'listall' function which calls the 'update' function once more and prints the username and password
    def listall(self):
        self.update()
        for key in self.details:
            print(key + "   " + self.details[key])

# assigns the variavle 'u' to the 'user'
u = user()
# calls the 'listall' function
u.listall()