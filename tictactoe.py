#user_name = input("what is your name?")
#password = input("input your password")
#a = len(password)
#b = (a * '*')

#print(f'Hi {user_name}, your password {b} is {a} letter long')
def display_board(board):
    for row in board:
      print(row[0], "|", row[1], "|", row[2])

def player_input(player, board):
    while True:
        row = int(input(f"Player {player}, row (1 to 3): ")) - 1
        col = int(input(f"Player {player}, column (1 to 3): ")) - 1

        if row < 0 or row >2 or col <0 or col > 2:
            print("Numbers must be between 1 and 3.")
        elif board[row][col] != " ":
            print("That square is already taken. Try again.")
        else:
           return row, col

 
#board = [[" ", " ", " "],
        # [" ", " ", " "],
         #[" ", " ", " "]]
#row, col = player_input("X", board)
#board[row][col] = "X"
#display_board(board)


def check_win(board, player):
    winning_line = [player, player, player]

    for row in board:
        if row == winning_line:
           return True

    for i in range(3):
        column = [board[0][i], board[1][i], board[2][i]]
        if column == winning_line:
            return True

    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]
    if diagonal_1 == winning_line or diagonal_2 == winning_line:
        return True

    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    player = "X"

    while True:
        display_board(board)
        row, col = player_input(player, board)
        board[row][col] = player

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


play()