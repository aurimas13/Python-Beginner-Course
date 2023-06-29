# Import necessary module for writing to a file
import os

# Ask the user to enter the desired name of the file
filename = input("Enter the desired name of the file: ")

# Make sure the filename is valid
filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_'))

# Add .txt extension to the filename if it doesn't have one
if not filename.endswith(".txt"):
    filename += ".txt"

# Ask the user to enter the desired number of lines
num_lines = int(input("Enter the desired number of lines: "))

# Initialize a counter
counter = 0

# Open the file in write mode
with open(filename, 'w') as f:
    # Start a while loop
    while counter < num_lines:
        # Ask the user to enter a line of text
        text = input("Enter a line of text or press ENTER to finish: ")

        # If the user presses ENTER (input is empty), break the loop
        if text == '':
            break

        # Write the entered text into the file
        f.write(text + '\n')

        # Increment the counter
        counter += 1

# Let the user know the file has been created
print(f"File '{filename}' has been created in {os.getcwd()} with {counter} lines.")
