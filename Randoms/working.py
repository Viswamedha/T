aaa == int(input('What is your number?: '))
def o():
    for int in aaa:  
        if aaa == 0:
            break
        elif aaa != 0:
            return aaa

bbb == int(input('What is your number?: '))
def t():
    for int in bbb:  
        if bbb == 0:
            break
        elif bbb != 0:
            return bbb

username == input('What is your username: ')
password == input('What is your password: ')
reenter == input('Retype your password: ')
def l():
    if password == reenter:
        f = open('login.txt','a+')
        f.writelines(username,password)
        f.close()
    else:
        continue

fst == input('Type a letter: ')
import nltk
nltk.download()
from nltk.corpus import words
word_list = words.words()
def w():
    # somehow

a == int(input('What is a?'))
b == int(input('What is b?'))
def m():
    a * b

def v():
    nu == [1, 2, 3, 4, 5, 6]
    return nu