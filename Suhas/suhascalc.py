class calc:

    def calculator(self):
        print("This is a calculator")
        print("Enter a '+' if you want to add numbers")
        print("Enter a '-' if you want to subtract")
        print("Enter a '*' if you want to multiply")
        print("Enter a '/' if you want to divide")
        print("Enter '**' if you want to square")
        print("Enter '***' if you want to cube")
        print("Enter '!' if you want to multiply by 10")
        print("Enter '£' if you want to divide by 10") # 5! - 5*4*3*2
        print("Enter '$' if you want to divide by 100")
        print("Type 'potato' to exit calculator")
        a = input("What operation do you choose: ")
        if a == "potato":
            print("OK")
            print("Goodbye! Thank you for using the calculator")  
        else:
            while a != "potato":
                if a == "+":
                    b = int(input("Please enter your first number: "))
                    c = int(input("Please enter your second number: "))
                    d = b + c
                    print(d)
                    a = input("What operation do you choose: ")
                elif a == "-":
                    b = int(input("Please enter your first number: "))
                    c = int(input("Please enter your second number: "))
                    d = b - c
                    print(d)
                    a = input("What operation do you choose: ")
                elif a == "*":
                    b = int(input("Please enter your first number: "))
                    c = int(input("Please enter your second number: "))
                    d = b * c
                    print(d)
                    a = input("What operation do you choose: ")
                elif a == "/":
                    b = int(input("Please enter your first number: "))
                    c = int(input("Please enter your second number: "))
                    d = b / c
                    print(d)
                    a = input("What operation do you choose: ")
                elif a == "**":
                    b = int(input("Please enter your number: "))
                    d = b * b
                    print(d)
                    a = input("What operation do you choose: ")
                elif a == "***":
                    b = int(input("Please enter your number: "))
                    d = b * b * b
                    print(d)
                    a = input("What operation do you choose: ")
                elif a == "!":
                    b = int(input("Please enter your number: "))
                    d = b * 10
                    print(d)
                    a = input("Which operation do you choose: ")
                elif a == "£":
                    b = int(input("Please enter your number: "))
                    b = b / 10
                    print(b)
                    a = input("Which operation do you choose: ")
                elif a == "$":
                    b = int(input("Please enter your number: "))
                    b = b / 100
                    print(b)
                    a = input("Which operation do you choose: ")

                  

a = calc()
a.calculator()

