# GitHub Navigation Guide

This guide covers the basics of moving files, creating folders, and 
understanding the difference between branches and folders in Git.

## 📂 Creating and Moving Files & Folders in GitHub

### **1️⃣ Creating a New Folder Locally**
To create a new folder inside your GitHub repository:
```bash
mkdir New-Folder
git add .
git commit -m "Added new folder and moved files"
git push origin main
touch New-Folder/README.md

# Move Notes folder to the repository
mv ~/Documents/Notes ./Notes

# Ensure Notes has a README for visibility in GitHub
echo "# Notes" > Notes/README.md
echo "This folder contains various guides, documentation, and personal notes." >> Notes/README.md

# Create GitHub Navigation Guide
echo "# GitHub Navigation Guide" > Notes/github-navigation.md
echo "\nThis guide covers the basics of moving files, creating folders, and understanding the difference between branches and folders in Git." >> Notes/github-navigation.md

# Expand the guide to document everything we've done in GitHub so far
echo "\n## GitHub Workflow: Everything We've Done" >> Notes/github-navigation.md
echo "\n### Setting Up the Repository" >> Notes/github-navigation.md
echo "- Created a new repository and named it **Main**" >> Notes/github-navigation.md
echo "- Deleted unnecessary repositories to keep things clean" >> Notes/github-navigation.md
echo "- Renamed branches where needed and standardized everything under **main**" >> Notes/github-navigation.md
echo "\n### Organizing the Repository Structure" >> Notes/github-navigation.md
echo "- Moved and renamed folders to create a professional layout" >> Notes/github-navigation.md
echo "- Deleted unnecessary folders and consolidated similar projects" >> Notes/github-navigation.md
echo "- Created a structured README for each folder" >> Notes/github-navigation.md
echo "\n### Git Basics We Used" >> Notes/github-navigation.md
echo "- Cloning a repo: \`git clone <repo_url>\`" >> Notes/github-navigation.md
echo "- Checking out branches: \`git checkout <branch_name>\`" >> Notes/github-navigation.md
echo "- Creating new folders: \`mkdir FolderName\`" >> Notes/github-navigation.md
echo "- Moving files: \`mv file.txt NewFolder/\`" >> Notes/github-navigation.md
echo "- Deleting folders: \`git rm -r FolderName\`" >> Notes/github-navigation.md
echo "- Committing and pushing changes: \`git commit -m 'message' && git push origin main\`" >> Notes/github-navigation.md

# Commit and push changes
git add Notes
git commit -m "Expanded GitHub Navigation Guide to document everything we've done"
git push origin main


