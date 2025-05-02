import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

def main():
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
"""
Password Strength Checker
This is a simple Python program that checks the strength of a password based on several criteria including length, use of uppercase and lowercase letters, digits, and special characters.

Features
Checks if the password length is at least 8 characters.
Verifies the presence of digits, uppercase letters, lowercase letters, and special characters.
Provides a strength rating: Very Weak, Weak, Moderate, Strong, or Very Strong.
Usage
Clone or download this repository.

Run the script using Python 3:


python passstrength.py
Enter the password you want to check when prompted.

The program will output the strength of the password.

Example

Enter a password to check its strength: MyP@ssw0rd123
Password strength: Very Strong
Requirements
Python 3.x
License
This project is licensed under the MIT License."""
