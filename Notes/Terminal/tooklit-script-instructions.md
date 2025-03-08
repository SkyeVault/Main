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
        5) echo "Goodbye!"; exit 0 ;;
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
    echo "5) Exit"
    echo "---------------------------------"
    echo -n "Choose an option: "
}
```

### **Example Changes**
- Change "Set up a new project" to **"Create a new Rust project."**
- Replace "Run a local server" with **"Start a Docker container."**
- Add **"Sync files with AWS S3."**

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

---

## 4. Saving User Preferences
You can store user preferences in a **config file** to avoid re-entering common inputs.

### **Example: Storing AWS Credentials**
Modify the AWS sync function to use stored credentials:
```bash
sync_aws_s3() {
    source ~/.aws_config
    aws s3 sync ~/projects s3://$AWS_BUCKET_NAME/
    echo "Files synced to S3 bucket: $AWS_BUCKET_NAME"
}
```

Create a `~/.aws_config` file:
```bash
export AWS_BUCKET_NAME="my-default-bucket"
```
Then load it in the script:
```bash
source ~/.aws_config
```

---

## 5. Automating Daily Tasks
### **Example: Running a Morning Setup Script**
If you frequently open the same tools, automate the process:
```bash
morning_setup() {
    echo "Starting your daily setup..."
    code ~/projects  # Open VS Code in the projects folder
    docker start my-dev-container  # Start a development container
    firefox https://chat.openai.com/  # Open a browser tab
    echo "All set!"
}
```
Add this to the menu:
```bash
3) morning_setup ;;
```

---

## 6. Running the Customized Script
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