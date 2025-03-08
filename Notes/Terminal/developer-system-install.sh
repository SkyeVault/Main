#!/bin/bash

# Initialize System - Developer Toolkit Setup Script
# Automates setup for a new machine or VM with all necessary tools

# Function: Update System & Enable Security
update_system() {
    echo "Updating system packages..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sudo softwareupdate -ia  # macOS
    else
        sudo apt update && sudo apt upgrade -y  # Linux
    fi

    echo "Enabling firewall..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
    else
        sudo ufw enable
    fi
}

# Function: Install Command-Line Tools
install_cli_tools() {
    echo "Installing essential CLI utilities..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install wget curl git tree htop
    else
        sudo apt install -y wget curl git tree htop
    fi
}

# Function: Set Up Git & SSH
setup_git_ssh() {
    echo "Generating SSH key for GitHub..."
    ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa
}

# Function: Install Programming Languages
install_languages() {
    echo "Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

    echo "Installing Python & Pip..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    else
        sudo apt install -y python3 python3-pip
    fi
}

# Function: Install AWS CLI & Security Tools
install_aws_tools() {
    echo "Installing AWS CLI..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install awscli
    else
        sudo apt install -y awscli
    fi

    echo "Configuring AWS CLI..."
    aws configure
}

# Function: Install & Configure VS Code
install_vscode() {
    echo "Installing Visual Studio Code..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install --cask visual-studio-code
    else
        sudo snap install code --classic
    fi

    echo "Installing VS Code Extensions..."
    code --install-extension ms-python.python
    code --install-extension rust-lang.rust-analyzer
}

# Function: Optimize Terminal & Zsh
setup_terminal() {
    echo "Installing Oh My Zsh & Plugins..."
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install zsh-autosuggestions zsh-syntax-highlighting
    else
        sudo apt install -y zsh-autosuggestions zsh-syntax-highlighting
    fi

    echo "Applying Zsh Configurations..."
    echo "source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc
    echo "source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
    source ~/.zshrc
}

# Function: Run All Setup Steps
initialize_system() {
    update_system
    install_cli_tools
    setup_git_ssh
    install_languages
    install_aws_tools
    install_vscode
    setup_terminal
    echo "System setup complete! Restart your terminal for all changes to take effect."
}

# Execute the script
initialize_system
