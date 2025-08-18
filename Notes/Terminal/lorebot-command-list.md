# Home Workstation Command Guide (lorebot)

This document condenses all shell activity from `~/.bash_history` and `~/.zsh_history` on `lorebot`. It includes system setup, machine learning pipelines, LLM deployment, Dockerized environments, and GUI/remote tool chains. Commands are cleaned, deduplicated, and grouped logically for clarity.

---

## Table of Contents

1. [System Setup](#system-setup)
2. [Dev Tools & Editors](#dev-tools--editors)
3. [Shell Customization (Zsh)](#shell-customization-zsh)
4. [Python, Virtualenv, and Pip](#python-virtualenv-and-pip)
5. [Git & GitHub Workflow](#git--github-workflow)
6. [Ollama (LLM)](#ollama-llm)
7. [Docker Environment](#docker-environment)
8. [SadTalker Pipeline](#sadtalker-pipeline)
9. [Networking & DNS](#networking--dns)
10. [GPU/Drivers & CUDA](#gpudrivers--cuda)
11. [Parsec, Sunshine & Remote Desktop](#parsec-sunshine--remote-desktop)
12. [Verge3D & OrcaSlicer](#verge3d--orcaslicer)
13. [Aliases & Quality of Life](#aliases--quality-of-life)

---

## System Setup

```bash
sudo apt update && sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt autoremove -y
sudo do-release-upgrade
sudo apt install -y \
    git curl wget unzip build-essential software-properties-common \
    apt-transport-https ca-certificates gnupg lsb-release tree
```

## Dev Tools & Editors

```bash
sudo apt install -y code tilix nano micro mousepad
sudo apt install gimp ffmpeg
```

## Shell Customization (Zsh)

```bash
sudo apt install -y zsh
chsh -s $(which zsh)
# Plugins
ZSH_CUSTOM=${ZSH_CUSTOM:-~/.oh-my-zsh/custom}
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```

## Python, Virtualenv, and Pip

```bash
sudo apt install -y python3.11 python3.11-venv python3.11-dev
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

## Git & GitHub Workflow

```bash
git config --global user.email "arynwood@protonmail.com"
git clone <repo>
git pull --rebase origin main
git add -A
git commit -m "<msg>"
git push origin main
git log --oneline --graph --decorate --all
```

## Ollama (LLM)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama list
ollama pull <model>
ollama serve
OLLAMA_HOST=0.0.0.0:11434 ollama serve
sudo systemctl enable --now ollama
```

### Common Pulled Models

```bash
tinyllama:1.1b-chat
gemma:2b-instruct-q4_0
codellama:7b-instruct-q4_0
mistral:7b-instruct-q4_0
llama3:8b-instruct-q4_0
gpt-oss:20b
qwen2.5:7b-instruct
```

## Docker Environment

```bash
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
sudo systemctl enable --now docker
```

### Docker Commands

```bash
docker compose up -d
docker compose build <profile>
docker compose --profile auto up -d
docker logs -f <container>
docker exec -it <container> bash
```

## SadTalker Pipeline

```bash
cd ~/tools/sad-talker
python3 inference.py \
  --driven_audio <audio.wav> \
  --source_image <image.png> \
  --enhancer gfpgan \
  --result_dir <output_dir> \
  --still --preprocess full

# GPU-optimized Torch (CUDA 11.8 or 12.1)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Checkpoints Download (via `hf_hub_download`)

```python
from huggingface_hub import hf_hub_download
files = ["epoch_20.pth", "pose_model.pth.tar", ...]
for f in files:
    hf_hub_download("TencentARC/SadTalker", filename=f, local_dir=".")
```

## Networking & DNS

```bash
ping google.com -c 4
ip addr show
sudo systemctl restart NetworkManager
sudo systemctl restart systemd-resolved
sudo rm -f /etc/resolv.conf
sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

## GPU/Drivers & CUDA

```bash
nvidia-smi
sudo ubuntu-drivers autoinstall
sudo apt install -y nvidia-container-toolkit
sudo systemctl restart docker
```

## Parsec, Sunshine & Remote Desktop

```bash
# Sunshine
sudo apt install ./sunshine*.deb
sunshine &
ss -tuln | grep 47990
journalctl -u sunshine -e

# Parsec
chmod +x parsec.AppImage
./parsec.AppImage --register-host
```

## Verge3D & OrcaSlicer

```bash
# Verge3D
tar -xf verge3d-blender-*.tar.gz -C ~/tools/verge3d
~/tools/verge3d/verge3d-blender-*/verge3d --app-manager

# OrcaSlicer
chmod +x OrcaSlicer*.AppImage
./OrcaSlicer*.AppImage
```

## Aliases & Quality of Life

```bash
alias server='ssh sayhiholly@162.248.7.248'
alias ll='ls -lah'
alias gs='git status'
```

---
