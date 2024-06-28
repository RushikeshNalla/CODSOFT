
# Rock-Paper-Scissors Game.

import random

def get_user_choice():

  while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice in ['rock', 'paper', 'scissors']:
      return choice
    else:
      print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():

  choices = ['rock', 'paper', 'scissors']
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):

  if user_choice == computer_choice:
    return "Tie"
  elif user_choice == 'rock':
    if computer_choice == 'scissors':
      return "Win"
    else:
      return "Lose"
  elif user_choice == 'paper':
    if computer_choice == 'rock':
      return "Win"
    else:
      return "Lose"
  else:
    if computer_choice == 'paper':
      return "Win"
    else:
      return "Lose"

def play_again():

  while True:
    choice = input("Play again? (y/n): ").lower()
    if choice in ['y', 'n']:
      return choice == 'y'
    else:
      print("Invalid choice. Please enter y or n.")

def main():

  user_score = 0
  computer_score = 0

  print("Welcome to Rock-Paper-Scissors!")

  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"\nYou chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    if result == "Win":
      print("You win!")
      user_score += 1
    elif result == "Lose":
      print("You lose.")
      computer_score += 1
    else:
      print("It's a tie!")

    print(f"\nCurrent score: User - {user_score}, Computer - {computer_score}")

    if not play_again():
      print("Thank you for playing!")
      break

if __name__ == "__main__":
  main()