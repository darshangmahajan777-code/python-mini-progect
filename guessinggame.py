import random

# Generate random number between 1 and 100
number = random.randint(1, 100)

# Count attempts
attempts = 0

print("🎯 NUMBER GUESSING GAME")
print("Guess a number between 1 and 100")

while True:

    # User input
    guess = int(input("Enter your guess: "))

    # Count attempts
    attempts += 1

    # Check guess
    if guess > number:
        print("❌ Your guess is too high")
        print("👉 Guess a smaller value\n")

    elif guess < number:
        print("❌ Your guess is too low")
        print("👉 Guess a higher value\n")

    else:
        print("\n🎉 Congratulations!")
        print("✅ You guessed the correct number")
        print("📊 Total attempts:", attempts)
        break