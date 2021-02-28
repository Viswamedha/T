
class calculator:

  def __init__(self):
    pass


  

  def add(self, count, data):
    print(data)
    for i in data:
      count += i  # data = data + i
    return count
    
  def calculate(self):
    choice = input('inp: ')
    while choice != "sh":
      if choice == "+":
        num1 = int(input("enter number: "))
        while not num1:
          num1 = int(input("enter number: "))
        num2 = int(input("enter number 2: "))
        data = []
        while num2 != 0:
          data.append(num2)
          num2 = int(input("enter number 2: "))
        a = self.add(num1, data)
        print(a)
      choice = input('inp: ')

f = calculator()
f.calculate()

