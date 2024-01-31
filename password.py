import random
import string

def generate_secure_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    #listy ze znakami

    password_characters = []
    password_characters.append(random.choice(lowercase_letters))
    password_characters.append(random.choice(uppercase_letters))
    password_characters.append(random.choice(digits))
    password_characters.append(random.choice(special_characters))

    while len(password_characters) < 8:
        password_characters.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        
    random.shuffle(password_characters)
    password = ''.join(password_characters)

    return password

#wywolanie funkcji
secure_password = generate_secure_password()
print("Wygenerowane bezpieczne hasło:", secure_password)
