# Ask the user to input the number of lines they want to enter
num_lines = int(input("Enter the number of lines you want to input: "))

# Ask the user for the name of the file they want to create
filename = input("Enter the name of the file you want to create: ")

# Open the file for writing
with open(filename, 'w') as file:
    # Initialize the counter for the number of lines
    count = 0

    # Use a while loop to take input from the user
    while count < num_lines:
        # Ask the user to enter a line of text
        text = input("Enter a line of text (or just press ENTER to quit): ")

        # Check if the user pressed just ENTER (empty input)
        # If so, break the loop
        if text == '':
            break

        # Write the text to the file, followed by a newline character
        file.write(text + '\n')

        # Increment the counter
        count += 1

# Inform the user that the file has been created
print(f"The file '{filename}' has been created with your input.")
