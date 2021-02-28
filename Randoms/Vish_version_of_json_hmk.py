import json
class user:
    def __init__(self):
        self.details = {} #exists

    def store(self):
        file = open("data.json", "w")  #open file
        json.dump(self.details, file, indent=4)  #putting the new details into the file
        file.close()  #close file

    def update(self):
        file = open("data.json")  #open file
        self.details = json.load(file)  #reads the file

    def signup(self):
        self.update()  #calls the update function
        # username, password, reenter password
        # if username 
        # if boolean   empty string = False   full string = True
        valid = False  #stating its value
        while valid == False:   # while not False   
            username = str(input("Username: "))  #username input
            password = str(input("Password: "))  #password input
            confirm = str(input("Confirm Password: "))  #checks the password
            if username and password and confirm and password == confirm: #if something exists in all the inputs and the 2 password input r the same
                self.details[username] = password  #storing it in the dict
                valid = True  
        self.store()  #calling another func
    
    def login(self):
        self.update()  #calls the func
        username = str(input("Username: "))  #asks for username
        password = str(input("Password: "))  #asks for password
        if username in self.details:  #if the username exists
            if self.details[username] == password:  #checks password
                print("Valid! You are now logged in! ")  #if it passes both conditions prints valid
                return  #ends the func
        print("Invalid! ")  #if it doesnt get past the first condition prints invalid
    
    def listall(self):
        self.update()  #func
        for key in self.details:  #doing it once for each key & value
            print(key + "   " + self.details[key])  #prints everything in th json

u = user()  #calling the class
u.listall()  #calling the func
