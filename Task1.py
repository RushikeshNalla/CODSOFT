
# Design a simple calculator with basic arithmetic operations.

def get_numbers():

  while True:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      return num1, num2
    except ValueError:
      print("Invalid input. Please enter numbers only.")

def choose_operation():

  while True:
    operation = input("""
Choose operation:
  + for addition
  - for subtraction
  * for multiplication
  / for division
Enter your choice: """)
    if operation in ['+', '-', '*', '/']:
      return operation
    else:
      print("Invalid operation. Please choose +, -, *, or /.")

def perform_calculation(num1, num2, operator):

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  else:

    if num2 == 0:
      return "Error: Division by zero"
    return num1 / num2

def main():

  print("Welcome to the Simple Calculator!")
  while True:
    num1, num2 = get_numbers()
    operator = choose_operation()
    result = perform_calculation(num1, num2, operator)
    print(f"Result: {result}")

    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
      break

  print("Thank you for using the Simple Calculator!")

if __name__ == "__main__":
  main()


