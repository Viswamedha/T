#Hangman
'''
import random # Creates a random number
file = open("eklavya.txt","r") # Opens the file eklavya.txt and uses read mode (can view all text in the file)
words = file.readlines() # the variable 'words' is assigned to file.readlines(), which means each line of text in the file is shown on another line
file.close() # Closes the file
word = random.choice(words).strip("\n") # Picking a random word and removes the \n from the word
wordletter = list(word) # The variable 'word' is turned into a list, which is now the variable 'wordletter'
guessedletter = [] # The variable 'guessedletter' is an empty list because no letters have been guessed yet
lives = 12 # the variable 'lives' have been set to twelve, so the player only have 12 chances to make an error
underscore = [] # the variable 'underscore' is in an empty list because the number of letters in the word is 0, for now


for i in wordletter: # For every letter in 'wordletter'
    underscore.append("_") # ...add an underscore to the list 'underscore'
while lives > 0: # As long as your lives are more than 0
    if "_" not in underscore: # if there are no underscores in 'underscore'
        break # end the while loop
    print("".join(underscore)) # shows how many underscores there are
    guessletter = input("Guess a letter: ") # invites player to input a letter, and stores in in variable 'guessletter'
    if guessletter in guessedletter: # if the player's letter has already been guessed...
        print("You already tried that letter") # ...show the statement 'You already tried that letter'
    else: # or if that has not happened
        guessedletter.append(guessletter) # add the chosen letter to the list of guessed letters
        if guessletter in wordletter: # if the player's letter is in the word
            print("You got a letter!") # say 'You got a letter!'
            for i in range (len(wordletter)): # if the word letter is ??? long
                if wordletter[i] == guessletter: # if the letter in the word is the same as the guessed letter
                    underscore[i]=guessletter # add an underscore to 'underscore' because a letter was guessed
        else: # or if this has not happened
            lives= lives-1 # take away a life
            print("Wrong letter") # show 'Wrong letter'
            print("Number of lives left: "+str(lives)) # show the number of lives left
 
if lives == 0: # if the player has no lives left
    print("You have run out of lives.") # show 'You have run out of lives.'
else: # if the player still has some lives left
    print("You have got the word.") # say 'You have got the word.'
    print("The word was " + str(word)) # show the word

'''

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