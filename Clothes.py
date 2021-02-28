
shirt = str(input("What is the colour of your shirt? "))
trouser = str(input("What is the colour of your trouser? "))
shoes = str(input("What are the colour of your shoes? "))
blazer = str(input("What is the colour of your blazer? "))

def outfit(shirt, trouser, shoes, blazer):
  if shirt == shoes or shirt == trouser or shirt == blazer:
    Answer = "True"
  elif blazer == shoes or blazer == trouser:
    Answer = "True"
  elif shoes == trouser:
    Answer = "True"
  else:
    Answer = "False"
  return Answer

Answer = outfit(shirt, trouser, shoes, blazer)

print(str(Answer))