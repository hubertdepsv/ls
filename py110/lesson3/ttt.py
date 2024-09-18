import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_NUMBER = 5

WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]

def prompt(message):
    print(f"==> {message}")

def display_board(board, score):
    os.system('clear')
    prompt(print_score(score))
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
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

def join_or(lst, delimiter=', ', word='or'):
    str_lst = [str(num) for num in lst]
    if len(str_lst) == 0:
        return ""

    if len(str_lst) == 1:
        return str_lst[0]

    return f"{delimiter.join(str_lst[:-1])} {word} {str_lst[-1]}"

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square: {join_or(valid_choices)}")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        if (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won(board):
    return bool(detect_winner(board))

def find_at_risk_square(board, option='defensive'):
    if option == 'defensive':
        marker = HUMAN_MARKER
    else:
        marker = COMPUTER_MARKER
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for line in winning_lines:
        markers_in_line = [board[square] for square in line]
        # if 2 keys have a human marker, return the one without
        if markers_in_line.count(marker) == 2:
            for square in line:
                if board[square] == INITIAL_MARKER:
                    return square

    return None

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = find_at_risk_square(board, 'offensive')

    if not square:
        square = find_at_risk_square(board, 'defensive')

    if not square:
        square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def print_score(score):
    return f"""Current scores are:
                Player: {score['Player']},
                Computer: {score['Computer']}"""

def play_tic_tac_toe():
    score = {
        'Player': 0,
        'Computer': 0,
    }
    while True:
        board = initialize_board()

        while True:
            display_board(board, score)

            player_chooses_square(board)

            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        if someone_won(board):
            winner = detect_winner(board)
            score[winner] += 1
            prompt(f"{winner} won!")
        else:
            prompt("It's a tie!")

        if GAMES_NUMBER in score.values():
            winner = [
                key for key, value in score.items() if value == GAMES_NUMBER
            ][0]
            prompt(f"This match was won by {winner}! Thanks for playing!")
            # When a match is won the programme will stop
            break

        prompt("Play again? (y or n)")
        answer = input().lower()[0]

        if answer != 'y':
            break

        prompt('Thanks for playing Tic Tac Toe!')

# Call the main game function
play_tic_tac_toe()