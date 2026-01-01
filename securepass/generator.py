import secrets
import string

def generate_password(length, symbols):
    chars = string.ascii_letters + string.digits

    if symbols:
        chars += "!@#$%^&*()_+-=[]{}"

    password = "".join(secrets.choice(chars) for _ in range(length))
    return password, len(chars)

