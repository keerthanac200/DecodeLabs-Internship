import random
import string


def generate_password(length):
    # Make sure the password is long enough
    if length < 4:
        print("Password length must be at least 4.")
        return None

    # Character groups
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = "@#$%&*!?"

    # Make sure the password contains:
    # At least one letter
    # At least one number
    # At least one special character

    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    # Remaining characters
    all_characters = letters + numbers + special_characters

    for i in range(length - 3):
        password.append(random.choice(all_characters))

    # Shuffle the password so the required characters
    # are not always at the beginning
    random.shuffle(password)

    return "".join(password)


print("=" * 45)
print("       RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("\nEnter password length: "))

        password = generate_password(length)

        if password is not None:
            print("\nGenerated Password:", password)
            print("Password Length:", len(password))

            choice = input(
                "\nDo you want to generate another password? (yes/no): "
            ).lower()

            if choice != "yes":
                print("\nThank you for using the Password Generator!")
                break

    except ValueError:
        print("Please enter a valid number.")