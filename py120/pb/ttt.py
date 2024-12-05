import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    CENTER_SQUARE = 5

    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

class Player:
    def __init__(self, marker):
        self.marker = marker

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )
    GAMES_LIMIT = 3

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.human_score = 0
        self.computer_score = 0
        self.first_player = self.human

    def play(self):
        self.display_welcome_message()
        self.board.display()

        while True:
            self.play_game()

            if self.human_score + self.computer_score == TTTGame.GAMES_LIMIT:
                break
            
            if not self._play_again():
                break

        self.display_goodbye_message()
    
    def play_game(self):
        current_player = self.first_player
        self.board = Board()
        self.board.display_with_clear()
        print(f"The score is now:\n"
              f"Human: {self.human_score}\n"
              f"Computer: {self.computer_score}")

        while True:
            self.player_moves(current_player)
            if self.is_game_over():
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)

        self.board.display_with_clear()
        self.display_results()

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human

    def player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def _play_again(self):
        play_again = input("Do you want to play again? (y or n): ").lower().strip()
        if play_again.startswith('n'):
                return False
        return True

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            self.human_score += 1
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            self.computer_score += 1
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    @staticmethod
    def _join_or(keys):
        if len(keys) < 3:
            return " or ".join(keys)
        return f"{', '.join(keys[:-1])} or {keys[-1]}"

    def human_moves(self):
        choice = None
        valid_choices = self.board.unused_squares()
        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = self._join_or(choices_list)
            prompt = f"Choose a square among {choices_str}: "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def detect_immediate_win_in_row_for_player(self, player, row):
        opponent = self.computer if player == self.human else self.human
        if self.board.count_markers_for(player, row) == 2 and self.board.count_markers_for(opponent, row) == 0:
            return True
        
        return False
    
    def find_square_to_mark(self, row):
        for key in row:
            if self.board.squares[key].is_unused():
                return key
            
        return None

    def computer_moves(self):
        row = None
        for winning_row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.detect_immediate_win_in_row_for_player(self.computer, winning_row):
                row = winning_row
                break
            if self.detect_immediate_win_in_row_for_player(self.human, winning_row):
                row = winning_row
        
        choice = None
        if row:
            choice = self.find_square_to_mark(row)
        elif self.board.squares[Board.CENTER_SQUARE].is_unused():
            choice = Board.CENTER_SQUARE
        else:
            valid_choices = self.board.unused_squares()
            choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

game = TTTGame()
game.play()
