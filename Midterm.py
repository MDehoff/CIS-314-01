import re
import random
import string

password_file = "Password_file.txt"  # variable storing a text file where weak passwords will be written

def password_strength(password):
    strength = 0  # initialize the password strength
    feedback = []  # empty list to store feedback

    if len(password) >= 8:  # check if password is 8 characters long
        strength += 1  # if true increase strength by 1
    else:
        feedback.append("Password should be at least 8 characters long.")  # if not return this

    if re.search(r'[a-z]', password):  # uses regular expressions to check if password includes a lowercase letter
        strength += 1
    else:
        feedback.append("Password needs at least one lowercase letter.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password needs at least one uppercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password needs at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password needs at least one special character.")

    if not re.search(r'(password|123|admin|forget)', password, re.IGNORECASE):  # ignorecase recognizes patterns no matter the capitalization
        strength += 1
    else:
        feedback.append("Avoid using common passwords like password, 123, admin, and forget")

    if strength >= 6:  # Determine overall strength of password
        return "Strong Password!", feedback

    elif strength >= 4:  # Determine if it's moderate
        return "Moderate password, could use some strengthening.", feedback
    else:  # Determine if it's weak
        return "Weak password, needs improvement.", feedback


def save_feedback(feedback):
    # append feedback to password file
    with open(password_file, "a") as f:  # open with the append mode
        f.write("Password Feedback: " + "".join(feedback) + "\n")  # Join feedback with a comma


def generate_recommendations(feedback):
    recommended_password = ""
    
    if "Password should be at least 8 characters long." in feedback:
        recommended_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        recommended_password += random.choice(string.ascii_uppercase)
        recommended_password += random.choice(string.ascii_lowercase)
        recommended_password += random.choice(string.digits)
        while len(recommended_password) < 12:  # Ensuring at least 12 characters
            recommended_password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    if "Password needs at least one lowercase letter." in feedback:
        recommended_password += random.choice(string.ascii_lowercase)
    
    if "Password needs at least one uppercase letter." in feedback:
        recommended_password += random.choice(string.ascii_uppercase)
    
    if "Password needs at least one digit." in feedback:
        recommended_password += random.choice(string.digits)
    
    if "Password needs at least one special character." in feedback:
        recommended_password += random.choice(string.punctuation)
    
    if "Avoid using common passwords like password, 123, admin, and forget" in feedback:
        # Avoid generating these common passwords in recommendations
        recommended_password = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) * 2
        recommended_password = recommended_password + random.choice(string.punctuation)

    return recommended_password


if __name__ == "__main__":  # Driver code
    password = input("Create a password:")  # Have the user enter a password
    result, suggestions = password_strength(password)  # call the password function and run password through
    print(result)

    if suggestions:  # print suggestions for strengthening password
        print("Suggestions to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")  # Print each suggestion
    
    # if password is weak, provide recommendations and save to password file
    if result.startswith("Weak"):
        print(f"Saving feedback to {password_file}")
        save_feedback(suggestions)  # call save function to store suggestions 
        recommended_password = generate_recommendations(suggestions)
        print(f"Recommended Strong Password: {recommended_password}")
