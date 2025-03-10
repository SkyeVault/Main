import os
import re

# Function to format names (lowercase, hyphens, no special characters)
def format_name(name):
    name = name.lower()                          # Convert to lowercase
    name = name.replace("_", "-")                # Replace underscores with hyphens
    name = re.sub(r'[^a-z0-9.-]', '', name)      # Remove special characters except hyphens and dots (for file extensions)
    return name

# Get the current working directory
current_dir = os.getcwd()

# Process folders first
folders = [f for f in os.listdir(current_dir) if os.path.isdir(f)]
for folder in folders:
    formatted_name = format_name(folder)
    if folder != formatted_name:
        os.rename(folder, formatted_name)
        print(f"Renamed folder: '{folder}' → '{formatted_name}'")
    else:
        print(f"Folder already formatted: '{folder}'")

# Process files
files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]
for file in files:
    file_name, file_ext = os.path.splitext(file)  # Split filename and extension
    formatted_name = format_name(file_name) + file_ext  # Keep original extension
    if file != formatted_name:
        os.rename(file, formatted_name)
        print(f"Renamed file: '{file}' → '{formatted_name}'")
    else:
        print(f"File already formatted: '{file}'")

print("\nFolder and file renaming complete!")