import json #Imports the module
class user: #Class 
    def __init__(self): 
        self.details = {} #An empty dictionary used for later

    def store(self):
        file = open("data.json", "w") #Opeminh the json file
        json.dump(self.details, file, indent=4) #Storing the empty "details" in the file
        file.close() #Closes the file

    def update(self):
        file = open("data.json") #Opens the file
        self.details = json.load(file)

    def signup(self):
        self.update()
        valid = False #States that valid is false, can be used later to break while loops, useful
        while valid == False: 
            username = str(input("Username: ")) #Inputs
            password = str(input("Password: "))
            confirm = str(input("Confirm Password: "))
            if username and password and confirm and password == confirm: #Checks if the username and password isn't blank and makes sure that the re-entered password is coorect
                self.details[username] = password #Stores it in the dictionary
                valid = True #Breaks the while loop
        self.store()
    
    def login(self):
        self.update()
        username = str(input("Username: ") #inputs
        password = str(input("Password: "))
        if username in self.details:
            if self.details[username] == password: #Checks the details against the ones stored in the dictionary
                print("Valid! You are now logged in! ") #Done!
                return #Ends the program
        print("Invalid! ")
    
    def listall(self):
        self.update()
        for key in self.details:
            print(key + "   " + self.details[key]) #Prints the details at the end

u = user()
u.listall()
