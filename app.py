# Let's create rock, paper, scissors game
# The player can choose rock, paper, or scissors and should be warned if they make an invalid choice
# The computer should also choose randomly between rock, paper, and scissors
# The winner should be determined by the rules of the game
# The player should be able to play multiple times and the game should keep track of the score
# The player should be able to end the game at any time
# The player should be able to see their score at any time
# The player should be able to see the computer's choice at any time
# The player should be able to see the current round at any time
# The game should be run from the command line

import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.round = 0

    def play(self):
        while True:
            player_choice = input('Enter your choice (rock, paper, scissors): ')
            if player_choice not in self.choices:
                print('Invalid choice. Please try again.')
                continue
            computer_choice = random.choice(self.choices)
            print(f'Computer choice: {computer_choice}')
            self.round += 1
            if player_choice == computer_choice:
                print('It\'s a tie!')
            elif player_choice == 'rock' and computer_choice == 'scissors':
                print('You win!')
                self.player_score += 1
            elif player_choice == 'paper' and computer_choice == 'rock':
                print('You win!')
                self.player_score += 1
            elif player_choice == 'scissors' and computer_choice == 'paper':
                print('You win!')
                self.player_score += 1
            else:
                print('You lose!')
                self.computer_score += 1
            print(f'Player score: {self.player_score}')
            print(f'Computer score: {self.computer_score}')
            print(f'Round: {self.round}')
            play_again = input('Do you want to play again? (yes/no): ')
            if play_again == 'no':
                break

game = RockPaperScissors()
game.play()

