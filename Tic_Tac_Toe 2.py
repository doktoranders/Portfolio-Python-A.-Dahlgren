class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        
    def print_board(self):
        print('\n')
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i + 3]))
            
    def update_board(self, position, player_type):
        try:
            if self.board[position - 1] == ' ':
                self.board[position - 1] = player_type
                return True
            else:
                print('Position already selected. Select another position.')
                return False
        except IndexError:
            print('Invalid position! Select another position.')
            
    def check_winner(self, player_type):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if all(self.board[i] == player_type for i in win):
                return True
        return False
    
    def check_draw(self):
        return ' ' not in self.board

class Player:
    def __init__(self, player_type):
        self.type = player_type
        self.name = self.get_name(player_type)
        
    def get_name(self, player_type):
        name = input(f'Player selecting {player_type}, enter your name: ')
        return name

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1
        
    def play(self):
        self.board.print_board()
        while True:
            try:
                message = f'{self.current_player.name}, enter the position (1 - 9): '
                position = int(input(message))
                if self.board.update_board(position, self.current_player.type):
                    self.board.print_board()
                    if self.board.check_winner(self.current_player.type):
                        print(self.current_player.name, 'wins!')
                        break
                    elif self.board.check_draw():
                        print('Game is a draw!')
                        break
                    else:
                        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            except ValueError:
                print('Invalid input! Enter a number between 1 and 9.')

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
