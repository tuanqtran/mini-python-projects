import random
import string

# Collect user preferences
# - length
# - should contain uppercase
# - should contain special
# - should contain digits

# Create all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid based off user preference

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Do you want to include uppercase letters? (y/n) ").strip().lower()
    include_special = input("Do you want to include special characters? (y/n) ").strip().lower()
    include_digits = input("Do you want to include digits? (y/n) ").strip().lower()

    if length < 4:
        print("Password length must be greater than 4 characters.")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""

    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "y":
        required_characters.append(random.choice(uppercase))
    if include_special == "y":
        required_characters.append(random.choice(special))
    if include_digits == "y":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)

    return str_password

generate_password()