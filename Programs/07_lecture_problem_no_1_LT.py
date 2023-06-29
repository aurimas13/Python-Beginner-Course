# Import the datetime class from the datetime module
from datetime import datetime

# Define the full text of "Zen of Python"
zen_of_python = """Beautiful is better than ugly.
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
Although never is often better than *right* now."""

# Write the text to a file named "Tekstas.txt"
with open("Tekstas.txt", "w") as file:
    file.write(zen_of_python)

# Read the text from the file and print it
with open("Tekstas.txt", "r") as file:
    print(file.read())

# Append the current date and time to the last line of the file
with open("Tekstas.txt", "a") as file:
    file.write('\n' + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

# Read the text from the file, number each line and replace "Beautiful is better than ugly." 
with open("Tekstas.txt", "r") as file:
    lines = file.readlines()

with open("Tekstas.txt", "w") as file:
    for index, line in enumerate(lines, start=1):
        if "Beautiful is better than ugly." in line:
            line = "Gražu yra geriau nei bjauru.\n"
        file.write(f"{index} {line}")

# Read the text from the file and print it in reverse
with open("Tekstas.txt", "r") as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line, end="")

# Count words, numbers, uppercase letters and lowercase letters in the file
word_count = 0
number_count = 0
uppercase_count = 0
lowercase_count = 0
with open("Tekstas.txt", "r") as file:
    for line in file:
        for char in line:
            if char.isalpha():
                if char.isupper():
                    uppercase_count += 1
                else:
                    lowercase_count += 1
            elif char.isdigit():
                number_count += 1
        word_count += len(line.split())

print(f"\nWords: {word_count}, Numbers: {number_count}, Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")

# Copy the contents of the file to a new file in uppercase
with open("Tekstas.txt", "r") as original_file:
    with open("Tekstas_uppercase.txt", "w") as new_file:
        new_file.write(original_file.read().upper())
