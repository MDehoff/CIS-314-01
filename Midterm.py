import re

def password_strength_evaluator(password):
    # Initialize strength score
    score = 0

    # Check the length of the password
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Evaluate the strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to evaluate its strength: ")
    strength = password_strength_evaluator(password)
    print(f"Password strength: {strength}")
