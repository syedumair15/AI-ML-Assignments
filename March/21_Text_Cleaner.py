# 21_Text_Cleaner.py
import string

text = "Hello!!! This is TEXT."

text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))

print(text)
