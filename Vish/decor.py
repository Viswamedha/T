
def hello(name):
  return "Hello "+name
h = hello
hello = 0
#print(h("Vish"))


def hello(name):
  def message():
    return "Greetings "
  return message() + name
#print(hello("Vish"))


def greeting(name):
  return "Greetings " + name
	
def run(g):
  name = "Bob"
  return g(name)
  # greetings
  # return greetings(name)
#print(run(greeting))


def create(name):
  def message():
    return "Hello " + name
  return message
# files
# local - function 
# local - can be accessed by subfunctions
#a = create("Gary")
#print(a())

def f(name):
  return "Hello "+name

def create(func):
  def new(name):
    return func(name) + " ! "
  return new

v = create(f)
print(v("Vish"))



def f(name):
  return "Hello "+name

def create(func):
  def wrap(name):
    return (func(name))
  return wrap
 # function object 


# @decoratorname
@create
def main(name):
  print("I just wanna say", name)

main(f("Vish"))


def create(func):
  def wrap(name):
    return (func(name))
  return wrap

def haha(name):
    return name + "Hahaha"

a = create(haha)
a("asdasdasd")

@create
def y(name):
    return "sadasdasd"+name


# hwk - use the create function as a decorator and make a few of ur own functions using that! 
# decorators are also called template functions - what they do is simply change data being passed into a function a certain way before processing!
# in reality you never need to make ur own decorators - only how to use them
# the idea behind this is when u have a ton of functions and say, all of them require the data being passed in to be converted to strings
# so one possible way to simplify that is to create a function Generator like this:
'''
def myfunc(func): #creating the generator 
  def process(data): # this uses the data thats passed in
    return func(str(name)) # this is the actual conversion that takes place
  return process # returns the new function with the processing in place
# we call it using  @decoratorname
@myfunc
def newfunc(name):
  print(name+", hello")
# and then to use it
newfunc("Lol")
'''
print(y(haha("jeff")))