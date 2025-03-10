import os
import re

# Function to format folder names (hyphens, lowercase)
def format_folder_name(name):
    name = name.lower()                          # Convert to lowercase
    name = name.replace("_", "-")                # Replace underscores with hyphens
    name = re.sub(r'[^a-z0-9-]', '', name)       # Remove special characters except hyphens
    return name

# Function to format file names (underscores, lowercase)
def format_file_name(name):
    name = name.lower()                          # Convert to lowercase
    name = name.replace("-", "_")                # Convert hyphens to underscores
    name = re.sub(r'[^a-z0-9_.]', '', name)      # Remove special characters except underscores and dots
    return name

# Get the current working directory
current_dir = os.getcwd()

# Dry run preview
print("Preview of Changes:")
print("=" * 40)

# Process folders first (hyphens)
folders = [f for f in os.listdir(current_dir) if os.path.isdir(f)]
for folder in folders:
    formatted_name = format_folder_name(folder)
    if folder != formatted_name:
        print(f"Folder: '{folder}' → '{formatted_name}'")

# Process files next (underscores)
files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]
for file in files:
    file_name, file_ext = os.path.splitext(file)  # Split filename and extension
    formatted_name = format_file_name(file_name) + file_ext  # Keep original extension
    if file != formatted_name:
        print(f"File: '{file}' → '{formatted_name}'")

# Ask for confirmation before renaming
confirm = input("\nProceed with renaming? (yes/no): ").strip().lower()

if confirm == "yes":
    print("\nRenaming Files and Folders...")
    
    # Rename folders
    for folder in folders:
        formatted_name = format_folder_name(folder)
        if folder != formatted_name:
            os.rename(folder, formatted_name)
            print(f"Renamed folder: '{folder}' → '{formatted_name}'")

    # Rename files
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        formatted_name = format_file_name(file_name) + file_ext
        if file != formatted_name:
            os.rename(file, formatted_name)
            print(f"Renamed file: '{file}' → '{formatted_name}'")

    print("\nRenaming complete.")
else:
    print("\nNo changes were made.")