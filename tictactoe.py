import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

player = "X"
computer_ai = "O"
winner = None
game_running = True

#print game board
def print_game_board(board):
    for i in range(3):
        row = ""
        for j in range(3):
            row += board[i*3+j]
            if j < 2:
                row += "|"
        print(row)
        if i < 2:
            print("-+-+-")

# user input
def user_input(board):
    if player == computer_ai:
        computer_move(board)
    else:
        while True:
            user_inpt = int(input("Choose a Square (1-9): "))
            if user_inpt >= 1 and user_inpt <= 9 and board[user_inpt-1] == " ":
                board[user_inpt-1] = player
                break
            else:
                print("That spot is already occupied or invalid. Try again.")

# check for win
def check_winner(board):
    global winner
    winner = None

    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != " ":
            winner = board[i]
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != " ":
            winner = board[i]
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True

    return False

# check for tie in the game
def check_tie(board):
    global game_running
    if " " not in board and winner is None:
        print("There is a Tie between the players")
        game_running = False

# check winner of game
def game_winner():
    global game_running
    if check_winner(board):
        print(f"Congratulations Player {winner}, you won the game!")
        game_running = False

# switching player
def switch_player():
    global player
    if player == "X":
        player = computer_ai
    else:
        player = "X"

# computer move
def computer_move(board):
    while True:
        random_number = random.randint(1, 9)
        if board[random_number-1] == " ":
            board[random_number-1] = player
            print(f"Computer Move: {random_number}")
            break

while game_running:
    print_game_board(board)
    print(f"Player {player}'s turn")
    user_input(board)
    game_winner()
    check_tie(board)
    if game_running:
        switch_player()

print_game_board(board)
