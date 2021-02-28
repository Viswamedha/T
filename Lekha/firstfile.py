# 3 files
# only those with valid credentials can use the calculator
# first file - class - calculator - 9 basic operations, needs to be usable till the user no longer wants to - keyword
# second file - 2 classes - one is for signup and stores in json file second class is for login, login gives access to calculator
# third file - json file to store all of this

# operations (+, -, /, //, *, **, %, <, >)
# keyword = stop

class Calculator:
    def __init__(self, first, second, added, takenaway, times, divided, idk, powers, perce, th, an):
        self.first = first
        self.second = second
        self.added = added
        self.takenaway = takenaway
        self.times = times
        self.divided = divided
        self.idk = idk
        self.powers = powers
        self.perce = perce
        self.th = th
        self.an = an
    def addition(self, first, second, added):
        self.added = self.first + self.second
        print(str(added))
    def subtraction(self, first, second, takenaway):
        self.takenaway = self.first - self.second
        print(str(takenaway))
    def multiplication(self, first, second, times):
        self.times = self.first * self.second
        print(str(times))
    def division(self, first, second, divided):
        self.divided = self.first / self.second
        print((str(divided)))

    def extra(self, first, second, idk):
        self.idk = self.first // self.second
        print(str(idk))
    def expo(self, first, second, powers):
        self.powers = self.first ** self.second
        print(str(powers))
    def mod(self, first, second, perce):
        self.perce = self.first % self.second
    def great(self, first, second, th):
        self.th = self.first > self.second
        print(str(th))
    def less(self, first, second, an):
        self.an = self.first < self.second
        print(str(an))
    def test(self):
      self.division()
a = Calculator()

first = int(input('What is your first number? '))
second = int(input('What is your second number? '))
print('Here are all 9 operations: addition, subtraction, multiplication, division, floor division, exponents, modulo, greater than and less than.')
operator = input('What operation would you like to use? ')
if operator == 'addition':
    a.addition()
    continue
elif operator == 'subtraction':
    a.subtraction()
    continue
elif operator == 'multiplication':
    a.multiplication()
    continue
elif operator == 'divison':
    a.division()
    continue
elif operator == 'floor division':
    a.extra()
    continue
elif operator == 'exponents':
    a.expo()
    continue
elif operator == 'modulo':
    a.mod()
    continue
elif operator == 'greater than':
    a.great()
    continue
elif operator == 'less than':
    a.less()
    continue
elif operator == 'stop':
    break
else:
    print('That is not a valid operation.')
    continue