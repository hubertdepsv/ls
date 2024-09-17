# Display the initial empty 3x3 board.
# Ask the user to mark a square.
# Computer marks a square.
# Display the updated board state.
# If it's a winning board, display the winner.
# If the board is full, display tie.
# If neither player won and the board is not full, go to #2
# Play again?
# If yes, go to #1
# Goodbye!

# 1: 
# 2: mark a square with the row number first and then the col number (from top left)
# 2: initialise an empty list of lists with 3 empty strings
# 3: update the list using the coordinates given


# Prompt the using to add a gross
# Get the row and col number from the input

# Update 
# To win somebody must have an equal distance between their 3 marks
# Winning combinations: 0-3-6, 1-4-7, 2-5-8, 0-4-8, 2-4-6
# Each player has a set with their marks
# Conditions to finish a game: set1 + set2 have 9 items or set1 or set2 contain a winning combination

import random, os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f"=> {message}")

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({', '.join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won(board):
    return bool(detect_winner(board))

def play_tic_tac_toe():
    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()