#rock paper scissors game

import random

def game():
    user_choice = input("Choose rock, paper or scissors: ")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == computer_choice:
        print("It` is a tie")

    if win(user_choice, computer_choice):
        print("You won. You choosed " + user_choice + " and computer choosed " + computer_choice)
    else:
        print("You  lost. You choosed " + user_choice + " and computer choosed " + computer_choice)


def win(player, computer):
    if (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        return True
    return False

game()

