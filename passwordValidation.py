import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

    
    if re.match(pattern, password):
        return "Valid Password"
    else:
        return "Invalid Password"


user_password = input("Enter your password: ")
result = validate_password(user_password)
print(result)
