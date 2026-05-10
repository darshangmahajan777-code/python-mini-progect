# ATM SIMULATOR

balance = 400000

print("🏦 WELCOME TO ATM")

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Check Balance
    if choice == "1":
        print(f"\n💰 Your Balance is ₹{balance}")

    # Deposit Money
    elif choice == "2":

        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            balance = balance + amount
            print(f"✅ ₹{amount} deposited successfully")
            print(f"💰 New Balance = ₹{balance}")

        else:
            print("❌ Enter valid amount")

    # Withdraw Money
    elif choice == "3":

        amount = float(input("Enter amount to withdraw: "))

        if amount > balance:
            print("❌ Insufficient Balance")

        elif amount <= 0:
            print("❌ Enter valid amount")

        else:
            balance = balance - amount
            print(f"✅ ₹{amount} withdrawn successfully")
            print(f"💰 Remaining Balance = ₹{balance}")

    # Exit
    elif choice == "4":
        print("\n🙏 Thank You For Using ATM")
        break

    # Invalid Choice
    else:
        print("❌ Invalid Choice")