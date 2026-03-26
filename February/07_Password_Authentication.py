# 07_Password_Authentication.py
# Assignment: Password Authentication System
# Description: Strong password validation and login system
# Author: Syed Umair Ali
import re

def is_strong(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

password = input("Create password: ")

while not is_strong(password):
    print("Weak password. Try again.")
    password = input("Create password: ")

print("Password created successfully")

attempts = 3
while attempts > 0:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)
