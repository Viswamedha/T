# - Input statements and variables
answer = int(input('What is 5 times 4? '))
# - Boolean Operators (and, or, not)
(34 + 82) or (54 + 62) == 152 
# - If loops with elif and else, For loops and While loops
if answer == 20:
    print('You were correct!')
elif answer - 1 == 20 or answer + 1 == 20:
    print('You were close!')
else:
    print('Go do some maths')
# - Strings and print statements
example = 'Supercalifragilisticexpialidocious'
print(example[::-1])
price = str(input('How expensive should seashells be? '))
print('She sells seashells by the seashore for {}'.format(price))
print('She sells seashells by the seashore for ' + price)
# - Integers and Floating Points, Comparators? (=, !=, <, >)
5 != 5.0
4.9999 <= 5
# - Dictionaries, Lists, Tuples
thetuple = (1, 2, 3, 4, 5)
print(type(thetuple))
# - Arithmetic (multiplication, divison, addition, subtraction, powers)
rightanswer = 5 * 4 
ooh = 3 % 2 
oohnoo = 4 + 3 ** 8
# - Basic conversion of data, for example an integer to a string
print(' The right answer is ' + str(rightanswer))
# - Functions and Classes (only the basics)
class BirthdayCake:
    def cake(self, birthday):
        birthday = str(input('What is your birthday(DD/MM/YYYY)? '))
        if birthday == '07/02/2021':
            print('Have a digital Birthday Cake!')
        else:
            print('Too bad, maybe tomorrow.')
# - Files and modes
chickenfillets = open('CHICKENFILLETS.txt', 'w+')
chickenfillets.write('CHICKEN FILLETS \n CHICKEN FILLETS \n CHICKEN FILLETS')
chickenfillets.read()
chickenfillets.close()