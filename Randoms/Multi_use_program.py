print("Welcome!")
print("Choose a number for your need: ")
print("1 for a calculator")
print("2 for a revision guide for python")
print("3 to play hangman")
print("4 to play a guess the number game")
num = int(input("What number will you choose: "))
if num == 1:
    print ("math homework.py")

    problem = input("enter the math problem, or 'q' to quit: ")
    while (problem != "q"):
        print("the answer to ",problem,"is:", eval(problem) )
        problem = input("enter another math problem, or 'q' to quit: ")

if num == 2:
    a = open("revision stuff 'multi use program'.txt", "r")
    b = a.read()
    a.close()
    print(b)

if num == 3:
    import random
    file = open("words.txt","r")
    words = file.readlines()
    file.close()
    word = random.choice(words).strip("\n")
    wordletter = list(word)
    guessedletter = []
    lives = 12
    underscore = []


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
    import random
    print("You are playing guess the number ")
    x = random.randint(0,150)
    guess = int(input("Guess the number: "))
    while guess!=x:
        if guess > x:
            print("Lower ")
        elif guess < x:
            print("Higher ")
        guess = int(input("Guess the number "))
    print("You have guessed the number ")


        
        
        
