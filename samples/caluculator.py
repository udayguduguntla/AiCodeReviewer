# Simple CLI Calculator App
# Created by: Your Name
# Note: This app performs basic arithmetic using Python functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Oops! Can't divide by zero."
    return x / y

def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("That's not a number, try again...")

def calculator():
    print("===================================")
    print("     Welcome to Python Calculator  ")
    print("===================================")

    while True:
        print("\nChoose an operation:")
        print(" 1 ➤ Addition (+)")
        print(" 2 ➤ Subtraction (-)")
        print(" 3 ➤ Multiplication (*)")
        print(" 4 ➤ Division (/)")
        print(" 5 ➤ Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye! 👋")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} × {num2} = {result}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} ÷ {num2} = {result}")

        else:
            print("Invalid choice! Please select a number between 1 to 5.")

if __name__ == "__main__":
    calculator()
