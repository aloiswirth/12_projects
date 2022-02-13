import random
import math

class player 
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super.__init__(letter)
    
    def get_move(game):
        valid_square = False
        val = None
        while not valid_sqare:
            square = input(self.letrer * '\'turn. Inpit move (0-9): ')
            # check if it is a correct value by trying to convert to 
            # an integer. If this fails say that it is invalid.
            # if the spot is not valid, also return a message
            try:
                int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if this is successful say yay!
            except:
                print('invalid square. try again: ')
            
        return val


