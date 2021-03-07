



# cake
# to buy all ingredients either day b4 or on that day, but it will take the whole day if u need to buy like 10 ingredients
# ingredients - day b4 bday

# u can never know how many parameters u need to pass into a function


# Consume rest behaviour
# Function
# Parameters
# Arguments - Consume rest arguments
# Keyword Arguments


def myfunc(*c):


  print(c)

#myfunc(5,6,7, 8)
# regular parameters, consume all parameter, keyword arguments, consume all keyword argument

def myfunc2(a, *b, c=100, **f):
  #print(b) 
  #print(str(b[2]))
  print(c)
  print(f)

# 4th number to be passed in converted to a string
myfunc2(3,5,c=6, g=7)





