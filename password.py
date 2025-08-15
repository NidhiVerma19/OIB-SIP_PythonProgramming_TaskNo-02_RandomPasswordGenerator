import random
import string

try:
    import pyperclip
    clipboard_available = True
except ImportError:
    clipboard_available = False


def get_user_preferences():
    print("\n==== PASSWORD GENERATOR SETTINGS ====")
    try:
        length = int(input("Enter password length (at least 5): "))
        if length < 8:
            print("Length should be at least 5.")
            return get_user_preferences()
    except ValueError:
        print("Please enter a valid number.")
        return get_user_preferences()

    include_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_lower = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    if not any([include_upper, include_lower, include_digits, include_symbols]):
        print("You must select at least one character type!")
        return get_user_preferences()

    return length, include_upper, include_lower, include_digits, include_symbols


def generate_password(length, upper, lower, digits, symbols):
    character_pool = ''
    password_chars = []

    if upper:
        character_pool += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))

    if lower:
        character_pool += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))

    if digits:
        character_pool += string.digits
        password_chars.append(random.choice(string.digits))

    if symbols:
        character_pool += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    remaining_length = length - len(password_chars)
    password_chars += random.choices(character_pool, k=remaining_length)

    random.shuffle(password_chars)

    return ''.join(password_chars)


def main():
    print("===  Welcome to the Advanced Random Password Generator  ===")

    while True:
        length, upper, lower, digits, symbols = get_user_preferences()
        password = generate_password(length, upper, lower, digits, symbols)

        print(f"\nYour generated password is:\n{password}")

        if clipboard_available:
            pyperclip.copy(password)
            print("Password has been copied to clipboard!")

        repeat = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the password generator. Stay safe!")
            break


if __name__ == "_main_":
    main()