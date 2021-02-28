print("Welcome to Tic Tac Toe")
print("When asked enter which position you want your marker to be placed at")
print("The grid is numbered like: ")
print("|1|2|3|")
print("|4|5|6|")
print("|7|8|9|")
print("Player 1 is 'X' and Player 2 is 'O'")
a = [["1", "2", "3"], ["4", "5", "6"], [ "7", "8", "9"]]

for i in a:
  print(i)
win = "False"
while win != "True":
  num = int(input("Which number would Player 1 like to replace: "))
  num2 = int(input("Which number would Player 2 like to replace: "))
  if num != num2:
    if num == 1 or num == 2 or num == 3:
      num = num - 1
      if a[0][num] == "O":
        print("Space already taken")
        print("You have been disqualified")
        print("Player 2 wins")
        win = "True"
      else:
        a[0][num] = "X"
    elif num == 4 or num == 5 or num == 6:
      num = num - 4
      if a[1][num] == "O":
        print("Space already taken")
        print("You have been disqualified")
        print("Player 2 wins")
        win = "True"
      else:
        a[1][num] = "X"
    else:
      num = num - 7
      if a[2][num] == "O":
        print("Space already taken")
        print("You have been disqualified")
        print("Player 2 wins")
        win = "True"
      else:
        a[2][num] = "X"
    for i in a:
      print(i)
    if num2 == 1 or num2 == 2 or num2 == 3:
      num2 = num2 - 1
      if a[0][num2] == "X":
        print("Space already taken")
        print("You have been disqualified")
        print("Player 2 wins")
        win = "True"
      else:
        a[0][num2] = "O"
        for i in a:
          print(i)
    elif num2 == 4 or num2 == 5 or num2 == 6:
      num2 = num2 - 4
      if a[1][num2] == "X":
        print("Space already taken")
        print("You have been disqualified")
        print("Player 2 wins")
        win = "True"
      else:
        a[1][num2] = "O"
        for i in a:
          print(i)
    else:
      num2 = num2 - 7
      if a[2][num2] == "X":
        print("Space already taken")
        print("You have been disqualified")
        print("Player 2 wins")
        win = "True"
      else:
        a[2][num2] = "O"
        for i in a:
          print(i)
  if a[0][0] == "X" and a[0][1] == "X" and a[0][2] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[1][0] == "X" and a[1][1] == "X" and a[1][2] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[2][0] == "X" and a[2][1] == "X" and a[2][2] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[0][0] == "X" and a[1][0] == "X" and a[2][0] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[0][1] == "X" and a[1][1] == "X" and a[2][1] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[0][2] == "X" and a[1][2] == "X" and a[2][2] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[0][0] == "X" and a[1][1] == "X" and a[2][2] == "X":
    print("Player 1 wins")
    win = "True"
  elif a[0][2] == "X" and a[1][1] == "X" and a[2][0] == "X":
    print("Player 1 wins")
    win = "True"



  if a[0][0] == "O" and a[0][1] == "O" and a[0][2] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[1][0] == "O" and a[1][1] == "O" and a[1][2] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[2][0] == "O" and a[2][1] == "O" and a[2][2] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[0][0] == "O" and a[1][0] == "O" and a[2][0] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[0][1] == "O" and a[1][1] == "O" and a[2][1] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[0][2] == "O" and a[1][2] == "O" and a[2][2] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[0][0] == "O" and a[1][1] == "O" and a[2][2] == "O":
    print("Player 2 wins")
    win = "True"
  elif a[0][2] == "O" and a[1][1] == "O" and a[2][0] == "O":
    print("Player 2 wins")
    win = "True"