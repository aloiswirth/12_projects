from lib2to3.pytree import LeafPattern


class TicTacToe:
    def __init__(self):
        # set up a single list of to represent the 3x3 board
        self.board = [' ' for _ in range(9)] 
        # initialize the current winner
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # o | 1 | 2 etc (tells what number belongs to what box)
        number_board = [[str(i) for i in range( j* 3, (j +1)*3 )] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def number_empty_squares(self):
        # return len(self.available_moves()) or
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if valid move then make the move (assign letter to square)
        # then return True. if invalid return False
        if self.board[square] == '':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
        return False



def play(game, x_player, o_player, print_game = True ):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    # Iteration while the came still has open squares.
    # Currently no winner 
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to sqare {square}')
                game.print_board()
                print('')

             #after the move we need to alternate the letters
             letter = 'O' if letter == 'X' else 'X'