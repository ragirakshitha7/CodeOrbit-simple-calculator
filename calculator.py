# Advanced Simple Calculator
# This program performs basic arithmetic operations.
# It takes user input, handles errors, and keeps running until the user exits.

import math


def get_number(message):
    """Ask the user for a number and handle invalid input."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate(num1, num2, operator):
    """Perform the selected arithmetic operation."""
    try:
        if operator == "+":
            return num1 + num2

        elif operator == "-":
            return num1 - num2

        elif operator == "*":
            return num1 * num2

        elif operator == "/":
            # Division by zero is not allowed
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 / num2

        elif operator == "%":
            # Modulus also cannot use zero as the second number
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 % num2

        elif operator == "**":
            return num1 ** num2

        else:
            raise ValueError("Unknown operation.")

    except ZeroDivisionError as error:
        return f"Error: {error}"

    except OverflowError:
        return "Error: Result is too large."


def show_menu():
    """Display available calculator operations."""
    print("\n--- ADVANCED PYTHON CALCULATOR ---")
    print("+   Addition")
    print("-   Subtraction")
    print("*   Multiplication")
    print("/   Division")
    print("%   Modulus")
    print("**  Power")
    print("sqrt  Square Root")
    print("exit  Close Calculator")


# Store calculation history in a list
history = []

while True:
    show_menu()

    # Get operation from user
    operation = input("\nChoose an operation: ").lower().strip()

    # Exit condition
    if operation == "exit":
        print("\nCalculator closed. Goodbye!")
        break

    # Square root needs only one number
    if operation == "sqrt":
        number = get_number("Enter a number: ")

        try:
            if number < 0:
                raise ValueError("Cannot find square root of a negative number.")

            result = math.sqrt(number)
            print(f"Result: √{number} = {result}")

            # Save result in history
            history.append(f"√{number} = {result}")

        except ValueError as error:
            print(f"Error: {error}")

        continue

    # Check whether the chosen operation is valid
    if operation not in ["+", "-", "*", "/", "%", "**"]:
        print("Invalid operation. Please choose from the menu.")
        continue

    # Take two numbers for normal operations
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")

    # Calculate and display the result
    result = calculate(first_number, second_number, operation)

    print(f"\nResult: {first_number} {operation} {second_number} = {result}")

    # Add successful calculations to history
    if not isinstance(result, str):
        history.append(f"{first_number} {operation} {second_number} = {result}")

    # Display history after each calculation
    if history:
        print("\nCalculation History:")
        for item in history:
            print("-", item)