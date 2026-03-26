# 28_Storytelling_with_Graphs.py
import matplotlib.pyplot as plt

subjects = ["Math","Science","English","Computer","Social"]
marks = [85,78,88,92,74]

scores = [45,55,67,72,80,85,90,95,60,70]

plt.bar(subjects, marks)
plt.show()

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.show()

plt.hist(scores)
plt.show()
