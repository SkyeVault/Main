# Customizing the Developer Toolkit Bash Script

## Introduction
This guide will walk you through customizing the **Developer Toolkit Bash Script** to match your workflow. You can modify functions, change menu options, and add automation tasks based on your personal development needs.

---

## 1. Understanding the Script Structure
The script consists of three main parts:
1. **The Menu** - Displays options for the user.
2. **Functions** - Executes different tasks based on user input.
3. **Loop** - Keeps the menu running until the user exits.

```bash
while true; do
    show_menu
    read choice
    case $choice in
        1) setup_project ;;  # Calls the function
        2) run_server ;;
        3) backup_files ;;
        4) update_git ;;
        5) system_maintenance ;;
        6) morning_setup ;;
        7) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid option, please try again!" ;;
    esac
done
```

### **How to Customize**
- Modify the **menu options** to match your workflow.
- Edit or add **functions** to automate tasks you frequently perform.
- Personalize messages and outputs for a better user experience.

---

## 2. Customizing Menu Options
To change the menu, locate this section and update the options:

```bash
show_menu() {
    echo "---------------------------------"
    echo "   My Custom Developer Toolkit"
    echo "---------------------------------"
    echo "1) Create a new Rust project"
    echo "2) Start a Docker container"
    echo "3) Sync files with AWS S3"
    echo "4) Update Git repository"
    echo "5) System Maintenance"
    echo "6) Morning Setup"
    echo "7) Exit"
    echo "---------------------------------"
    echo -n "Choose an option: "
}
```

---

## 3. Adding or Modifying Functions
Each menu option is linked to a function. You can add your own functions to automate tasks.

### **Example: Automating a Rust Project Setup**

```bash
setup_rust_project() {
    echo -n "Enter Rust project name: "
    read project_name
    cargo new "$project_name"
    cd "$project_name"
    echo "Rust project $project_name has been created!"
}
```

Replace the `setup_project` function call in the menu with:
```bash
1) setup_rust_project ;;
```

### **Example: Starting a Docker Container**
```bash
run_docker_container() {
    echo -n "Enter Docker image name: "
    read image_name
    docker run -d "$image_name"
    echo "$image_name is now running."
}
```

Replace the menu function call:
```bash
2) run_docker_container ;;
```

### **Example: Morning Setup**
```bash
morning_setup() {
    echo "Opening GitHub, VS Code, and browser..."
    open -a "Google Chrome" "https://github.com"
    open -a "Visual Studio Code"
    open -a "Finder" ~/ 
    echo "Your development environment is ready!"
}
```

### **Example: System Maintenance**
```bash
system_maintenance() {
    echo "Pulling latest changes from GitHub..."
    git pull origin main
    
    echo "Downloading and installing system updates..."
    sudo softwareupdate -ia
    
    echo "Checking firewall status and ensuring security..."
    sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
    sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
    
    echo "System is up to date and secure!"
}
```

Replace the menu function call:
```bash
5) system_maintenance ;;
```

---

## 4. Running the Customized Script
### **1. Make the Script Executable**
```bash
chmod +x my_toolkit.sh
```

### **2. Run the Script**
```bash
./my_toolkit.sh
```

---

## Conclusion
By customizing this script, you can:
- Automate your most-used tasks.
- Reduce repetitive typing.
- Make development workflows faster and more efficient.

Modify the script to fit your **personal needs** and create a command-line tool that works **just for you**!
