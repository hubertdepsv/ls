HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
INITIAL_MARKER = ' '

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

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
    print(marker)
    for line in winning_lines:
        markers_in_line = [board[square] for square in line]
        # if 2 keys have a human marker, return the one without
        if markers_in_line.count(marker) == 2:
            for square in line:
                if board[square] == INITIAL_MARKER:
                    return square

    return None

print(find_at_risk_square({1: 'X', 2: 'X', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}))
print(find_at_risk_square({1: 'X', 2: ' ', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}))
print(find_at_risk_square({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: 'X', 6: ' ', 7: ' ', 8: 'X', 9: ' '}))
print(find_at_risk_square({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: 'X', 6: ' ', 7: ' ', 8: ' ', 9: 'X'}))
print(find_at_risk_square({1: 'X', 2: 'X', 3: 'O', 4: 'O', 5: 'X', 6: ' ', 7: '', 8: ' ', 9: ' '}))

print(find_at_risk_square({1: 'O', 2: 'O', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}, 'offensive'))
print(find_at_risk_square({1: 'O', 2: ' ', 3: ' ', 4: 'O', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}, 'offensive'))
print(find_at_risk_square({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: 'O', 6: ' ', 7: ' ', 8: 'O', 9: ' '}, 'offensive'))
print(find_at_risk_square({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: 'O', 6: ' ', 7: ' ', 8: ' ', 9: 'O'}, 'offensive'))
print(find_at_risk_square({1: 'O', 2: 'O', 3: 'X', 4: 'X', 5: 'O', 6: ' ', 7: ' ', 8: ' ', 9: ' '}, 'offensive'))
print(find_at_risk_square({1: 'X', 2: ' ', 3: ' ', 4: 'O', 5: 'X', 6: 'X', 7: 'O', 8: ' ', 9: 'O'}, 'offensive'))