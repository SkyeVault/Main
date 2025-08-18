# Linux Command-Line Reference (Bash & Zsh)

This guide consolidates commands from extensive usage history across Bash and Zsh shells on the `aryncore` server. Commands are grouped by category, deduplicated, cleaned, and enriched with context. Common errors and recommended aliases are also included.

---

## Table of Contents

1. [System Monitoring & Information](#system-monitoring--information)
2. [System Updates & Packages](#system-updates--packages)
3. [User & Access Management](#user--access-management)
4. [Networking](#networking)
5. [Remote Access & GUI](#remote-access--gui)
6. [Docker & Containers](#docker--containers)
7. [Development Environment](#development-environment)
8. [Ollama (LLM Management)](#ollama-llm-management)
9. [File & Disk Operations](#file--disk-operations)
10. [Web Server & NGINX](#web-server--nginx)
11. [Monitoring & Observability](#monitoring--observability)
12. [Mail Server (Postfix)](#mail-server-postfix)
13. [DNS Server (BIND)](#dns-server-bind)
14. [GUI Virtualization (Headless)](#gui-virtualization-headless)
15. [Aliases & Helpers](#aliases--helpers)

---

## System Monitoring & Information

```bash
htop                # Interactive system monitor
ps aux              # Process listing
ps -p <PID> -o pid,ppid,cmd,etime
lsof -p <PID>       # Open files by process
lsof -i:<port>      # Network use by port
free -m             # Memory usage in MB
df -hT              # Disk usage and FS type
lsblk               # Block device tree
dmesg | grep -i denied | tail -n 20
uptime              # System load info
neofetch            # System summary
sensors             # Detect hardware sensors
```

## System Updates & Packages

```bash
sudo apt update && sudo apt upgrade -y    # Full upgrade
apt list --upgradable                     # Pending packages
sudo apt install -y <pkg>                 # Install package
sudo apt remove <pkg>                     # Remove package
sudo apt install -f                       # Fix broken installs
sudo dpkg --configure -a                 # Reconfigure packages
```

## User & Access Management

```bash
sudo passwd                 # Change root password
whoami                     # Show current user
sudo whoami                # Show elevated user
sudo usermod -aG docker $USER
sudo chown -R user:group <dir>
```

## Networking

```bash
ip a                       # Interface info
ping -c 3 google.com       # Test connectivity
curl ifconfig.me           # External IP
ss -tuln                   # Listening ports
ufw status                 # Firewall status
sudo ufw allow <service>   # Allow service
```

## Remote Access & GUI

```bash
sudo apt install xrdp -y
sudo systemctl enable xrdp && sudo systemctl start xrdp
echo xfce4-session > ~/.xsession
chmod +x ~/.xsession
sudo reboot
startxfce4 &
```

## Docker & Containers

```bash
sudo apt install -y docker.io docker-compose
sudo systemctl enable --now docker
docker ps -a              # All containers
docker images             # Show images
docker volume ls          # Volumes
sudo usermod -aG docker $USER
newgrp docker             # Reload group
```

### Common Docker Tasks

```bash
docker compose up -d
sudo docker-compose restart
docker-compose logs <service>
docker exec -it <container> sh
```

## Development Environment

```bash
# ZSH + Oh My Zsh
sudo apt install -y zsh
chsh -s $(which zsh)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Python
sudo apt install python3 python3-pip -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ollama (LLM Management)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama list                         # Show models
ollama pull <model>                 # Download
ollama rm <model>                   # Remove
ollama run <model>                  # Run
ollama serve                        # Serve API
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

## File & Disk Operations

```bash
ls -lah                # Detailed listing
mkdir -p /path         # Create dir
rm -rf /path           # Recursive remove
fdupes -r ~            # Find duplicates
find /tmp -newer <file> -ls
```

## Web Server & NGINX

```bash
sudo apt install nginx certbot python3-certbot-nginx -y
sudo nano /etc/nginx/sites-available/<site>
sudo ln -s /etc/nginx/sites-available/<site> /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d yourdomain.com
```

## Monitoring & Observability

```bash
# Node Exporter
useradd --no-create-home --shell /bin/false node_exporter
wget https://github.com/prometheus/node_exporter/releases/latest/download/node_exporter-1.8.0.linux-amd64.tar.gz
# Prometheus
curl -LO https://github.com/prometheus/prometheus/releases/download/v2.52.0/prometheus-2.52.0.linux-amd64.tar.gz
# Grafana
sudo apt install -y grafana
sudo systemctl enable --now grafana-server
```

## Mail Server (Postfix)

```bash
sudo apt install postfix mailutils -y
sudo nano /etc/postfix/main.cf
sudo systemctl restart postfix
mail
```

## DNS Server (BIND)

```bash
sudo apt install bind9 bind9utils bind9-doc -y
sudo nano /etc/bind/named.conf.local
sudo systemctl enable --now bind9
sudo named-checkconf
sudo named-checkzone <domain> /etc/bind/zones/db.<domain>
dig @localhost <domain>
```

## GUI Virtualization (Headless)

```bash
sudo apt install -y xvfb firefox x11vnc
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
firefox --no-remote --profile /tmp/testprofile &
x11vnc -display :99 -nopw -listen localhost &
```

## Aliases & Helpers

Add to `~/.zshrc` or `~/.bashrc`

```bash
alias ll='ls -lah'
alias gs='git status'
alias up='sudo apt update && sudo apt upgrade -y'
alias dps='docker ps -a'
alias serveollama='OLLAMA_HOST=0.0.0.0:11434 ollama serve'
```

---

## Error Fixes & Diagnostics

### Error: `Unable to locate package libwebkit2gtk-4.0-dev`

**Fix:** Add universe repo:

```bash
sudo add-apt-repository universe && sudo apt update
```

### Lock Errors (`dpkg/apt`)

```bash
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock
sudo dpkg --configure -a
```

---

> Keep this file under version control and use it as a reference for bootstrapping any new server or container.
