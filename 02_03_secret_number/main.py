import random
from re import X

from pygments import highlight

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess new number between 1 and {str(x)}."))
        if guess < random_number:
            print("to low. try again  ")
        elif guess > random_number:
            print("to high. try again  ")
    
    
    print(f"you did it!! The number was {random_number}")       


def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        print(guess)
        feedback = input("check the number. enter 'c', 'l, 'h' for correct, low and high")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1


print("you got it")

computer_guess(1000)