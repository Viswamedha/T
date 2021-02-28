
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

print(y(haha("jeff")))