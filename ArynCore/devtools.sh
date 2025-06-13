#!/bin/bash

set -e

echo "[+] Updating system..."
sudo apt update && sudo apt upgrade -y

echo "[+] Installing essential packages..."
sudo apt install -y curl wget git build-essential ca-certificates gnupg lsb-release software-properties-common unzip htop neofetch

echo "[+] Installing ZSH and plugins..."
sudo apt install -y zsh
chsh -s $(which zsh)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
sed -i 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc

echo "[+] Installing VS Code..."
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install -y code
rm packages.microsoft.gpg

echo "[+] Installing Python and libraries..."
sudo apt install -y python3 python3-pip python3-venv pipx
pipx ensurepath
pipx install virtualenv
pip3 install numpy pandas requests flask openai beautifulsoup4 jupyterlab matplotlib

echo "[+] Installing Rust and cargo tools..."
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env
cargo install exa ripgrep fd-find bat

echo "[+] Installing Node.js and npm via nvm..."
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"
nvm install --lts
nvm use --lts

echo "[+] Installing global npm packages..."
npm install -g three tauri

echo "[+] Installing Docker and Docker Compose..."
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker

echo "[+] Installing extras..."
curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash
echo "neofetch" >> ~/.zshrc

echo "[+] Done. Reloading ZSH..."
exec zsh
