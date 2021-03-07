


def generator(function):
  def modify(name):
    return function(name+" is stupid")
  return modify


@generator
def new(name):
  print(name)

@generator
def new2(name):
  print(name)
  
@generator
def new3(name):
  print(name)

@generator
def new4(name):
  print(name)

new("Suhas")

# generator
''' 
def generator_func(name):
  name = str(name)
  def new(name):
    print(type(name))
  new()
'''






