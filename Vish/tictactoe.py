board = [["1","2","3"],["4","5","6"],["7","8","9"]]
def show(): print("\n".join([" | ".join(line) for line in board]))
def render():
  data = []
  for line in board:
    for choice in line: data.append(choice)
  return data
turn_count = 1
def check(token):
  choice = str(input("Please enter the place you would occupy? "))
  while True:
    if choice not in render() or choice in ["X", "O"]:
      choice = str(input("Please enter the place you would occupy?"))
    else: break
  for line in range(len(board)):
    for value in range(len(board[line])):
      if board[line][value] == choice:
        board[line][value] = token
  if turn_count >= 5:
    for line in board:
      if line[0] == line[1] and line[1] == line[2] and line[2] == token: return True
    for i in range(0,3):
      if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == token: return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == token: return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == token: return True
  return False
playeroneturn = True
show()
while True:
  if playeroneturn:
    playeroneturn = False
    if check("X"):
      print('Player one has won! ')
      break
  else:
    playeroneturn = True
    if check("O"):
      print('Player two has won! ')
      break
  turn_count+=1
  if turn_count == 9:
    print("Game is a draw")
    break
  show()