# 12_Smart_Input.py
name = input("Enter name: ")
age = int(input("Enter age: "))
hobby = input("Enter hobby: ")

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print("Hello", name)
print("Category:", category)
print("Hobby:", hobby)
