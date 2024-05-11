import random

class Game:
    def __init__(self):
        self.computer_pick = self.get_computer_pick()
        self.user_pick = self.get_user_pick()
        self.result = self.get_result() 

    def get_computer_pick(self):
        random_number = random.randint(1, 3)
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        return options[random_number]

    def get_user_pick(self):
        while True:
            user_pick = input('Enter rock/paper/scissors: ').lower()
            if user_pick in ('rock', 'paper', 'scissors'):
                  break
            else:
                print('Wrong input!')
        return user_pick

    def get_result(self):
        if self.computer_pick == self.user_pick:
            return 'draw'
        winning_moves = {'paper': 'rock', 'rock': 'scissors', 'scissors': 'paper'}
        if winning_moves[self.user_pick] == self.computer_pick:
            return 'win'
        return 'lose'

    def print_result(self):
        print(f"Computer's pick: {self.computer_pick}")
        print(f'Your pick: {self.user_pick}')
        print(f'You {self.result}')

while True:
   game = Game()
   game.print_result()

   play_again = input('Do you want to play again? (y/n): ')
   if play_again != 'y':
      break
