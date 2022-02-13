import random

from pyrsistent import T

def play():
    user = input("What is your choice. 'r' for rock, 'p' for paper or 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'] )

    if user == computer:
        return 'tie'
    
    # r > s, s > p, p > r

    if is_win(user, computer):
        return 'You won'
    else:
        return 'Computer won'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
    (player == 's' and opponent == 'p') or \
    (player == 'rp' and opponent == 'r'):
        return True

print(play())