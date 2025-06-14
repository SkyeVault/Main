#!/bin/bash
set -e

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing base packages..."
sudo apt install -y \
    curl wget git unzip \
    python3 python3-pip python3-venv \
    build-essential libssl-dev libgtk-3-dev \
    pkg-config libwebkit2gtk-4.0-dev libappindicator3-dev \
    libayatana-appindicator3-dev librsvg2-dev

echo " Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker $USER

echo " Installing Node.js..."
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

echo " Installing Rust..."
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env

echo " Installing nkn-client JS..."
mkdir -p ~/mcp && cd ~/mcp
npm init -y
npm install nkn-client

echo " Creating Python venv..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo " Installing Tauri CLI..."
cargo install tauri-cli

echo " Pulling n8n docker container..."
docker pull n8nio/n8n

echo " Setup complete! Log out and back in to apply Docker permissions."
