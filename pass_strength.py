import string

def check_password(password):
    score = 0

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    print("\nPassword Analysis:")
    print("Uppercase:", has_upper)
    print("Lowercase:", has_lower)
    print("Digits:", has_digit)
    print("Special characters:", has_special)

    if score <= 2:
        print("\nStrength: Weak ❌")
    elif score <= 4:
        print("\nStrength: Medium ⚠️")
    else:
        print("\nStrength: Strong ✅")


def main():
    password = input("Enter your password: ")
    check_password(password)


main()