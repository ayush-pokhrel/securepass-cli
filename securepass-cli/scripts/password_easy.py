import random
import string

letters=string.ascii_letters
digits=string.digits
symbols="!@#$%^&*()"

all_chars=letters+digits+symbols

length=int(input("enter password length: "))

password=""

for _ in range(length):
    password+=random.choice(all_chars)

print("generated password: ",password)
