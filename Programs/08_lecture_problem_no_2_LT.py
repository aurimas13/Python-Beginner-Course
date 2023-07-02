# import necessary libraries
from datetime import datetime

# Full text of "The Zen of Python"
zen_of_python = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# Create a new text file and write the Zen of Python to it
with open("Tekstas.txt", "w") as file:
    file.write(zen_of_python)

# Read the file and print the contents
with open("Tekstas.txt", "r") as file:
    print(file.read())

# Append the current date and time to the last line of the file
with open("Tekstas.txt", "a") as file:
    file.write("\n" + str(datetime.today()))

# Read the file again, add line numbers, and write back to the file
with open("Tekstas.txt", "r") as file:
    lines = file.readlines()

with open("Tekstas.txt", "w") as file:
    for i, line in enumerate(lines, 1):
        file.write(f"{i}: {line}")

# Replace the line "Beautiful is better than ugly." with "Gražu yra geriau nei bjauru."
with open("Tekstas.txt", "r") as file:
    lines = file.readlines()

with open("Tekstas.txt", "w") as file:
    for line in lines:
        if "Beautiful is better than ugly." in line:
            line = line.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
        file.write(line)

# Print the entire text of the file in reverse
with open("Tekstas.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

# Count the number of words, numbers, uppercase letters, and lowercase letters in the file
with open("Tekstas.txt", "r") as file:
    text = file.read()

num_words = len(text.split())
num_numbers = sum(char.isdigit() for char in text)
num_upper = sum(char.isupper() for char in text)
num_lower = sum(char.islower() for char in text)

print(f"Words: {num_words}, Numbers: {num_numbers}, Uppercase letters: {num_upper}, Lowercase letters: {num_lower}")

# Copy the entire text of the file to a new file, converting to uppercase
with open("Tekstas.txt", "r") as file:
    text = file.read()

with open("Tekstas_UPPER.txt", "w") as file:
    file.write(text.upper())
