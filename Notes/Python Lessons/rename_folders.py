import os
import re

# Function to convert folder names to lowercase with hyphens
def format_folder_name(name):
    name = name.lower()               # Convert to lowercase
    name = name.replace("_", "-")     # Replace underscores with hyphens
    name = re.sub(r'[^a-z0-9-]', '', name)  # Remove special characters except hyphens
    return name

# Get list of folders in the current directory
current_dir = os.getcwd()
folders = [f for f in os.listdir(current_dir) if os.path.isdir(f)]

# Rename folders
for folder in folders:
    formatted_name = format_folder_name(folder)
    if folder != formatted_name:  # Rename only if different
        os.rename(folder, formatted_name)
        print(f"Renamed: '{folder}' → '{formatted_name}'")
    else:
        print(f"No change: '{folder}'")

print("\n Folder renaming complete!")