#rock paper scissors game

import random

def game():
    user_choice = input("Choose [r]ock, [p]aper or [s]cissors ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        print("It` is a tie")

    if win(user_choice, computer_choice):
        print("You won your choose was " + user_choice + " and computer choose was" + computer_choice)
    else:
        print("You loose your choose was " + user_choice + " and computer choose was " + computer_choice)


def win(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True
    return False

game()

