import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Invalid length. Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
