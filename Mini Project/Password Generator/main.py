import random

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+")

print("Generated password:", password)