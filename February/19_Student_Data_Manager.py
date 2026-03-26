# 19_Student_Data_Manager.py
students = {}

for i in range(5):
    name = input("Name: ")
    marks = float(input("Marks: "))
    students[name] = marks

def grade(m):
    if m >= 90: return "A+"
    elif m >= 80: return "A"
    elif m >= 70: return "B"
    else: return "C"

avg = sum(students.values()) / len(students)
topper = max(students, key=students.get)

for name, marks in students.items():
    print(name, marks, grade(marks))

print("Average:", avg)
print("Topper:", topper)
