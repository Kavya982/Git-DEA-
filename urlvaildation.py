import re

def validate_url(url):
    
    pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9#?&%=._-]*)*$'
    
    
    if re.match(pattern, url):
        return "Valid URL"
    else:
        return "Invalid URL"


user_url = input("Enter a URL to validate: ")
result = validate_url(user_url)
print(result)
