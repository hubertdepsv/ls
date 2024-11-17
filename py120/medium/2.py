import random

class GuessingGame:
    def __init__(self):
        self.number = random.choice(range(1, 101))
        self.guesses = 7

    def play(self):
        while True:
            print(f"\nYou have {self.guesses} guesses remaining.")
            user_choice = int(input('Enter a number between 1 and 100: '))

            if user_choice > self.number:
                print("Your guess is too high.")
            elif user_choice < self.number:
                print("Your guess is too low.")
            elif user_choice == self.number:
                print("That's the number!\n")
                print("You won!")
                return

            if self.guesses <= 1:
                print("\nYou have no more guesses. You lost!")
                return

            self.guesses -= 1

game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!