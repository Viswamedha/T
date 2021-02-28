from firstfile import *
import json
# 3 files
# only those with valid credentials can use the calculator
# first file - class - calculator - 9 basic operations, needs to be usable till the user no longer wants to - keyword
# second file - 2 classes - one is for signup and stores in json file second class is for login, login gives access to calculator
# third file - json file to store all of this

class Signup():
    def __init__(self, username, password, confirm):
        self.username = username
        self.password = password
        self.confirm = confirm
    def creating(self, username, password):
        self.username = input('What will your username be? ')
        self.password = input('What will your password be? ')
        self.confirm = input('Type your password again: ')
        if self.username and self.password and self.confirm == self.password:
            pass
        else:
            print(' Your confirmation password does not match your password.')

b = Signup()
b.Signup()
a = Calculator()
class Login():
    def __init__(self, username, password, entereduser, enteredpass):
        self.username = username
        self.password = password
        self,enteredpass = enteredpass
        self.entereduser = entereduser
    def signingin(self, username, password, entereduser, enteredpass):
        self.entereduser = input('What is your username? ')
        self.enteredpass = input('What is your password? ')
        if self.entereduser == self.username and self.enteredpass == self.password:
            print('You have logged in. You can now access the Calculator.')
            a.Calculator()
        else:
            print('You have entered the incorrect username and password.')

c = Login()
c.Login()

ohno = open('thirdfile.json', 'w')
json.dump(firstfile, secondfile)
ohno.close()