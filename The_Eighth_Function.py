from eight_functions import *
def eight():
    username = input('What is your username: ')
    password = input('What is your password: ')
    reenter = input('Retype your password: ')
    letter = input('Enter a letter: ')
    a = int(input('Enter a number: '))
    b = int(input('Enter a power: '))
    count = adder()
    order = multiplier()
    out = login(username, password, reenter)
    word = four(letter)
    ti = six(a, b)
    t = seven(count, order, out, word, ti)
    print(t)

eight()