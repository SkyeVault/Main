import os

# Define the base directory
base_dir = "skyevault-ops"

# Define the directory structure
directories = [
    f"{base_dir}/backend",
    f"{base_dir}/backend/security",
    f"{base_dir}/backend/scripts",
    f"{base_dir}/frontend/src",
    f"{base_dir}/frontend/public",
    f"{base_dir}/docs/api_docs",
    f"{base_dir}/scripts"
]

# Define the initial files to create
files = {
    f"{base_dir}/backend/main.py": "# Entry point for SkyeVault Ops backend\n",
    f"{base_dir}/backend/config.py": "# Configuration settings\n",
    f"{base_dir}/backend/requirements.txt": "# Python dependencies\n",
    f"{base_dir}/frontend/package.json": "{\n  \"name\": \"skyevault-frontend\"\n}\n",
    f"{base_dir}/docs/README.md": "# SkyeVault Ops Documentation\n",
    f"{base_dir}/docs/setup.md": "# Setup Guide\n",
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with initial content
for file, content in files.items():
    with open(file, "w") as f:
        f.write(content)

print("✅ SkyeVault Ops directory structure created successfully!")
