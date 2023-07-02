# Import the necessary libraries
import os
from datetime import datetime
import time

# Define the path to the new directory on the desktop
desktop = os.path.expanduser("~/Desktop")  # Gets the path to the user's desktop
directory = os.path.join(desktop, "Naujas Katalogas")  # Join the path to the desktop with the new directory name

# Create the new directory
os.makedirs(directory, exist_ok=True)  # Creates the directory. The exist_ok parameter allows the directory to be created even if it already exists

# Define the path to the new text file in the new directory
file_path = os.path.join(directory, "data.txt")

# Write the current date and time to the new file
with open(file_path, "w") as file:
    file.write(str(datetime.now()))  # Write the current date and time to the file

# Get the creation time and size of the file
creation_time = os.stat(file_path).st_ctime  # Get the creation time of the file
size = os.stat(file_path).st_size  # Get the size of the file in bytes

# Print the creation time (converted from seconds since epoch to a string) and size
print("Creation time:", time.ctime(creation_time))
print("Size:", size, "bytes")
