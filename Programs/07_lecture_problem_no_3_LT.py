# Import the os module to interact with the operating system
import os
# Import the datetime class from the datetime module
from datetime import datetime

# Get the path to the user's desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Define the directory name
directory_name = "Naujas Katalogas"

# Create the directory on the desktop
new_directory_path = os.path.join(desktop_path, directory_name)
os.makedirs(new_directory_path, exist_ok=True)

# Define the file name
file_name = "DataIrLaikas.txt"

# Create the file with today's date and time inside the new directory
file_path = os.path.join(new_directory_path, file_name)
with open(file_path, 'w') as file:
    # Write the current date and time to the file
    file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Get the file's creation time and size in bytes
creation_time = os.stat(file_path).st_ctime
file_size = os.stat(file_path).st_size

# Convert the creation time to a readable format
creation_time_formatted = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

# Print the file's creation time and size
print(f"The file '{file_name}' was created on {creation_time_formatted} and has a size of {file_size} bytes.")
