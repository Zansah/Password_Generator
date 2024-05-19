import random 
import string

def generate(length, password=''):
    if length == 0:
        return password
    else:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        random_char = random.choice(chars)
        return generate(length - 1, password + random_char)
    
password = generate(8)
print(f"Generated Password {[password]}")