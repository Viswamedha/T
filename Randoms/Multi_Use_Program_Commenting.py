print("Welcome!") 
print("Choose a number for your need: ")
print("1 for a calculator")
print("2 for a revision guide for python")
print("3 to play hangman")
print("4 to play a guess the number game") #Prints 5 statements
num = int(input("What number will you choose: ")) #Makes you enter a number and chooses what you want
if num == 1:
    print ("math homework.py")#If you enter the number 1 then you will see math homework.py

    problem = input("enter the math problem, or 'q' to quit: ") #either type a math problem or q
    while (problem != "q"): #If you enter q you leave math problem.py
        print("the answer to ",problem,"is:", eval(problem) ) #It solves the problem
        problem = input("enter another math problem, or 'q' to quit: ") #Lets you tyoe ub your problem or q

if num == 2:
    a = open("revision stuff 'multi use program'.txt", "r") #Opens it
    b = a.read() #Reads it
    a.close() #Closes it
    print(b) #Opens b- Reading

if num == 3:
    import random #Imports a random word
    file = open("words.txt","r") #Opens it
    words = file.readlines()
    file.close() #Closes it
    word = random.choice(words).strip("\n") #Chooses a random word
    wordletter = list(word) #Makes the word
    guessedletter = [] #Guess a letter
    lives = 12 #Gives you 12 guesses
    underscore = [] #Shows your score

    for i in wordletter:                 
        underscore.append("_")
    while lives > 0:
        if "_" not in underscore:
            break
        print("".join(underscore))
        guessletter = input("Guess a letter: ")
        if guessletter in guessedletter:
            print("You already tried that letter")
        else:
            guessedletter.append(guessletter)
            if guessletter in wordletter:
                print("You got a letter!")
                for i in range (len(wordletter)): 
                    if wordletter[i] == guessletter:
                        underscore[i]=guessletter
            else:
                lives= lives-1
                print("Wrong letter")
                print("Number of lives left: "+str(lives))
     
    if lives == 0:
        print("You have run out of lives.")
    else:
        print("You have got the word.")

if num == 4:
    import random #Imports a Random 
    print("You are playing guess the number ") #Prints It
    x = random.randint(0,150) #Imports a random number from 0 to 150
    guess = int(input("Guess the number: ")) #Makes you guess a number
    while guess!=x:
        if guess > x:
            print("Lower ") #If number is lower thna it will print lower
        elif guess < x:
            print("Higher ") #If the number is higher it will
        guess = int(input("Guess the number ")) #Asks you again
    print("You have guessed the number ") #If you get it it will print this


        
        
        
