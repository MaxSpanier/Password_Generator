import string
import secrets

def genrate_password_weak(length):
    alphabet = string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def genrate_password_strong(length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def genrate_password_extreme(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

print(genrate_password_weak(20))
print(genrate_password_strong(20))
print(genrate_password_extreme(20))

