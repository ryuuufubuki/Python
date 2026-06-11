import random 

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

length = input("Enter Password Length:")
length = int(length)

password = ""

for i in range(length):
    password += random.choice(characters)

print(password)     