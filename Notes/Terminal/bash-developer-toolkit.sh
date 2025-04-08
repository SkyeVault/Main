#!/bin/bash

# Function to display menu
show_menu() {
    echo "---------------------------------"
    echo "   Developer Toolkit"
    echo "---------------------------------"
    echo "1) Set up a new project"
    echo "2) Run a local server"
    echo "3) Backup important files"
    echo "4) Update Git repository"
    echo "5) Exit"
    echo "---------------------------------"
    echo -n "Choose an option: "
}

# Function to set up a new project
setup_project() {
    echo -n "Enter project name: "
    read project_name
    mkdir "$project_name" && cd "$project_name"
    git init
    touch README.md
    echo "# $project_name" > README.md
    echo "Project $project_name has been set up!"
}

# Function to start a local server
run_server() {
    echo "Starting a local server on port 8000..."
    python3 -m http.server 8000
}

# Function to back up important files
backup_files() {
    echo -n "Enter the directory to back up: "
    read dir
    if [ -d "$dir" ]; then
        tar -czvf backup-$(date +%F).tar.gz "$dir"
        echo "Backup created: backup-$(date +%F).tar.gz"
    else
        echo "Directory not found!"
    fi
}

# Function to update Git repository
update_git() {
    echo -n "Enter the repository path: "
    read repo
    if [ -d "$repo/.git" ]; then
        cd "$repo"
        git add .
        echo -n "Enter commit message: "
        read commit_msg
        git commit -m "$commit_msg"
        git push origin main
        echo "Repository updated successfully!"
    else
        echo "Not a valid Git repository!"
    fi
}

# Main loop for user interaction
while true; do
    show_menu
    read choice
    case $choice in
        1) setup_project ;;
        2) run_server ;;
        3) backup_files ;;
        4) update_git ;;
        5) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid option, please try again!" ;;
    esac
done