# CODSOFT

**Task 1**
Simple Calculator with Basic Arithmetic Operations.

Overview:
This program is a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. It prompts the user to input two numbers and choose an operation, then performs the calculation and displays the result.

**Code Explanation:**

1. get_numbers Function:
- Prompts the user to input two numbers.
- Validates the input to ensure only numbers are entered.
- Returns the two numbers.

2. choose_operation Function:
- Prompts the user to choose an arithmetic operation (addition, subtraction, multiplication, or division).
- Validates the input to ensure a valid operation is chosen.
- Returns the chosen operation.

3. perform_calculation Function:
- Takes two numbers and an operator as arguments.
- Performs the chosen arithmetic operation.
- Handles division by zero error.
- Returns the result of the calculation.

4. main Function:
- Welcomes the user to the calculator.
- Repeatedly performs calculations until the user decides to quit.
- Calls the above functions to get numbers, choose an operation, and perform the calculation.
- Displays the result.
- Asks the user if they want to perform another calculation.
- Thanks the user when they decide to quit.

**Example Usage:**
- Input two numbers: 10 and 5.
- Choose an operation: + (addition).
- Output: Result: 15.


**Task 2**
Rock-Paper-Scissors Game

**Overview:**
This program is a Rock-Paper-Scissors game where the user plays against the computer. The game prompts the user to choose rock, paper, or scissors, then randomly generates the computer's choice and determines the winner based on the rules of the game.

**Code Explanation:**

1. get_user_choice Function:
- Prompts the user to choose rock, paper, or scissors.
- Validates the input to ensure a valid choice is made.
- Returns the user's choice.

2. get_computer_choice Function:
- Randomly generates the computer's choice (rock, paper, or scissors).
- Returns the computer's choice.

3. determine_winner Function:
- Takes the user's and computer's choices as arguments.
- Determines the winner based on the rules:
  * Rock beats scissors.
  * Scissors beat paper.
  * Paper beats rock.
- Returns the result: "Win", "Lose", or "Tie".

4. play_again Function:
- Asks the user if they want to play another round.
- Validates the input to ensure a valid choice (y or n) is made.
- Returns True if the user wants to play again, False otherwise.

5. main Function:
- Welcomes the user to the game.
- Initializes user and computer scores.
- Repeatedly plays the game until the user decides to quit.
- Calls the above functions to get the user's and computer's choices and determine the winner.
- Displays the choices and the result of each round.
- Updates and displays the scores.
- Asks the user if they want to play again.
- Thanks the user when they decide to quit.

**Example Usage:**
- User choice: rock.
- Computer choice: scissors.
- Output: You win! (Rock beats scissors).

**Task 3**
To do list application

**How it works:**

- Menu Display: The display_menu function prints the available options.
- View List: The view_list function shows the current to-do items.
- Add Item: The add_item function prompts the user to input an item to add to the list.
- Remove Item: The remove_item function shows the list with indices and allows the user to remove an item by its number.
- Main Loop: The main function runs an infinite loop to keep the application running until the user chooses to exit.







