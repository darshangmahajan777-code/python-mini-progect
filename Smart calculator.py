# SMART CALCULATOR WITH HISTORY

# Addition
def add(a, b):
    return a + b


# Subtraction
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Store history
history = []


# Main program loop
while True:

    print("\n===== SMART CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Exit program
    if choice == "6":
        print("\nExiting...")
        print("Thank you! Visit again 😊")
        break

    # Show history
    elif choice == "5":

        print("\n===== HISTORY =====")

        if len(history) == 0:
            print("No calculations yet.")

        else:
            for item in history:
                print(item)

        continue

    # Check valid operation
    elif choice in ["1", "2", "3", "4"]:

        # Input numbers
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform operation
        if choice == "1":
            result = add(a, b)
            exp = f"{a} + {b} = {result}"

        elif choice == "2":
            result = sub(a, b)
            exp = f"{a} - {b} = {result}"

        elif choice == "3":
            result = mul(a, b)
            exp = f"{a} * {b} = {result}"

        elif choice == "4":
            result = div(a, b)
            exp = f"{a} / {b} = {result}"

        # Print result
        print("\nResult:", result)

        # Save history
        history.append(exp)

    else:
        print("Invalid choice! Please try again.")