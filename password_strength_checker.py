import re

def password_chekher(password):
    # Minimum length requirement
    if len(password) < 8:
        return "password must be at least 8 characters long."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "password must contain at least one lowercase letter."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "assword must contain at least one uppercase letter."
    
    # Check for at least one digit
    if not re.search(r'\d', password):
        return "password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "password must contain at least one special character."
    
    return "password is strong."

# Example usage
password = input("Enter a password to validate: ")
print(validate_password(password))



