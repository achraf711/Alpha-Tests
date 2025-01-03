import random
import string

def generate_random_password(length):
    if length < 8:
        return "Password length should be at least 8 characters."

    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
length = int(input("Enter the desired password length: "))
print(f"Generated password: {generate_random_password(length)}")
