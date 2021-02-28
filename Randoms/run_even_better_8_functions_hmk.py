import even_better_8_functions_hmk as z
def run():
    a = z.adder()
    b = z.multiplier()
    c = z.for_login()
    d = z.word(input("Enter a letter: "))
    e = z.power(int(input("Enter the number: ")),int(input("Enter an exponent: ")))
    z.print_all(a,b,c,d,e)
run()