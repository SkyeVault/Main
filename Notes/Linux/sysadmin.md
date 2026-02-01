# Sysadmin Command Sheet (Linux) — copy/paste friendly

> Notes:
> - Commands assume a typical Debian/Ubuntu system unless noted.
> - Use `sudo -i` (or prefix with `sudo`) when needed.
> - Replace placeholders like `<USER>`, `<IFACE>`, `<SERVICE>`, `<PORT>`, `<HOST>`.

---

## 0) Safety + context (do this first)
```bash
# Who am I / where am I / what kernel
whoami
id
hostnamectl
uname -a
date; timedatectl

# Quick system snapshot
uptime
w
last -n 10


⸻

1) Help / discovery

# Manuals and quick help
man <cmd>
tldr <cmd>              # install: apt install tldr (or snap/pip)
<cmd> --help

# Find binaries / commands
which <cmd>
command -v <cmd>
type <cmd>

# Search packages (Debian/Ubuntu)
apt-cache search <term>
apt show <pkg>
dpkg -L <pkg>           # files installed by package
dpkg -S /path/to/file   # which package owns this file


⸻

2) Files / directories

# Navigation + listing
pwd
ls -lah
tree -a -L 2            # install: apt install tree

# Disk usage (fast & common)
df -hT
du -h --max-depth=1 /var | sort -h

# Find large files
find /var -type f -size +500M -print0 | xargs -0 ls -lh

# Find files by name/time
find /etc -iname "*nginx*" 2>/dev/null
find /var/log -type f -mtime -7 -name "*.log" -print

# Permissions / ownership
stat <file>
namei -l /path/to/file
chmod 640 <file>
chown root:root <file>

# Compare / diff
diff -u old.conf new.conf
cmp -l file1 file2


⸻

3) Text processing (logs, configs)

# Quick view
cat <file>
less -S <file>
head -n 50 <file>
tail -n 100 <file>
tail -f <file>

# Search text
grep -R --line-number "pattern" /etc/<dir> 2>/dev/null
rg "pattern" /etc            # ripgrep: apt install ripgrep

# Useful parsing
awk '{print $1,$NF}' <file>
cut -d: -f1 /etc/passwd
sed -n '1,120p' <file>
sort -u <file>


⸻

4) Users, groups, sudo

# Users & groups
getent passwd <USER>
getent group <GROUP>
groups <USER>

# Add / modify user
useradd -m -s /bin/bash <USER>
passwd <USER>
usermod -aG sudo <USER>          # Debian/Ubuntu admin group

# Lock/unlock
passwd -l <USER>
passwd -u <USER>

# Sudo checks
sudo -l
visudo


⸻

5) Processes / performance

# Top-level monitoring
top
htop                    # apt install htop
ps aux --sort=-%mem | head
ps aux --sort=-%cpu | head

# Process details
pgrep -a <name>
pidof <name>
pstree -ap
lsof -p <PID> | head
cat /proc/<PID>/limits

# CPU / memory / IO
free -h
vmstat 1 5
iostat -xz 1 3          # apt install sysstat
iotop -o                # apt install iotop

# Kill / signal
kill -TERM <PID>
kill -KILL <PID>
pkill -f "pattern"


⸻

6) systemd services & boot

# Service control
systemctl status <SERVICE> --no-pager
systemctl start <SERVICE>
systemctl stop <SERVICE>
systemctl restart <SERVICE>
systemctl reload <SERVICE>
systemctl enable <SERVICE>
systemctl disable <SERVICE>

# Units, failed, boot
systemctl list-units --type=service --state=running
systemctl --failed
systemd-analyze blame | head -n 30
systemd-analyze critical-chain

# Timers (cron replacement)
systemctl list-timers --all


⸻

7) Journald logs

# System logs
journalctl -b --no-pager
journalctl -u <SERVICE> --since "1 hour ago" --no-pager
journalctl -u <SERVICE> -f

# Kernel logs
journalctl -k -b --no-pager

# See auth-related events (Ubuntu often uses journald too)
journalctl _SYSTEMD_UNIT=ssh.service --since yesterday --no-pager


⸻

8) Networking: interfaces, routes, DNS

# Interfaces & IPs
ip -br a
ip a show <IFACE>
ip link show
ethtool <IFACE>             # apt install ethtool

# Routes
ip r
ip -6 r
ss -tulpn                   # listening sockets
ss -tulpn | grep -E ':(80|443|22)\b'

# DNS resolution
resolvectl status           # systemd-resolved systems
cat /etc/resolv.conf

# Query DNS
dig +short A example.com
dig +short AAAA example.com
dig +trace example.com
nslookup example.com
host -a example.com

# Connectivity checks
ping -c 3 1.1.1.1
ping -c 3 example.com
curl -I https://example.com
curl -sv https://example.com 2>&1 | tail -n 30


⸻

9) Firewall (UFW / nftables / iptables)

# UFW (common on Ubuntu)
ufw status verbose
ufw app list
ufw allow 22/tcp
ufw deny 23/tcp
ufw delete allow 22/tcp

# nftables (modern)
nft list ruleset | less

# iptables (legacy systems)
iptables -S
ip6tables -S


⸻

10) SSH (server & client checks)

# SSH server status
systemctl status ssh --no-pager
ss -tulpn | grep sshd
grep -R --line-number "Port\|PermitRootLogin\|PasswordAuthentication" /etc/ssh/sshd_config /etc/ssh/sshd_config.d 2>/dev/null

# Test from another machine
ssh -vvv -p <PORT> <USER>@<HOST>

# Show host key fingerprints
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub


⸻

11) Packages / updates (Debian/Ubuntu)

# Update + upgrade
apt update
apt upgrade -y
apt full-upgrade -y

# Cleanup
apt autoremove -y
apt clean

# Package status
dpkg -l | less
apt policy <pkg>


⸻

12) Storage: partitions, mounts, LVM

# Block devices & filesystems
lsblk -f
blkid
mount | column -t
findmnt -rno SOURCE,TARGET,FSTYPE,OPTIONS

# Partition table
fdisk -l
parted -l

# LVM (if used)
pvs; vgs; lvs
lvdisplay
vgdisplay


⸻

13) Permissions, ACLs, capabilities

# ACLs
getfacl <path>
setfacl -m u:<USER>:rwx <path>

# Linux capabilities
getcap -r / 2>/dev/null | head
setcap cap_net_bind_service=+ep /path/to/binary


⸻

14) Security quick checks

# Recent logins
last -a | head -n 30
lastb -a | head -n 30          # failed logins (if enabled)

# Listening ports + owning processes
ss -tulpn

# SUID/SGID files (audit)
find / -perm /6000 -type f 2>/dev/null | head -n 50

# File integrity idea (basic)
debsums -s                      # apt install debsums


⸻

15) Web / TLS (Nginx/Apache basics)

# Nginx
nginx -t
nginx -T | sed -n '1,200p'
ls -lah /etc/nginx/sites-available /etc/nginx/sites-enabled

# Apache
apache2ctl -t
apache2ctl -S

# Check cert presented by a host (SNI)
echo | openssl s_client -connect <HOST>:443 -servername <HOST> 2>/dev/null | openssl x509 -noout -subject -issuer -dates -ext subjectAltName


⸻

16) DNS servers (BIND example)

# Service & config sanity
named-checkconf
named-checkzone example.com /etc/bind/zones/db.example.com

# Query your authoritative server directly
dig @127.0.0.1 example.com SOA +noall +answer
dig @<NS_IP> example.com A +noall +answer
dig @<NS_IP> example.com AAAA +noall +answer


⸻

17) Cron & scheduling

# User cron
crontab -l
crontab -e

# System cron
ls -lah /etc/cron.*
cat /etc/crontab

# systemd timers
systemctl list-timers --all


⸻

18) Backups & archives

# Tar (preserve perms, show progress)
tar -czvf backup.tgz /etc/nginx /etc/ssh

# Rsync (safe defaults; dry run first)
rsync -avhn --delete /source/ /dest/
rsync -avh --delete /source/ /dest/

# Checksums
sha256sum <file>
sha256sum -c checksums.sha256


⸻

19) Troubleshooting patterns (copy/paste)

# "Why is my service down?"
systemctl status <SERVICE> --no-pager
journalctl -u <SERVICE> --since "2 hours ago" --no-pager | tail -n 200
ss -tulpn | grep <PORT> || true

# "Why can't I reach it from outside?"
ip -br a
ip r
ufw status verbose
ss -tulpn | grep <PORT> || true
curl -sS -o /dev/null -w "http=%{http_code}\n" http://127.0.0.1:<PORT>/ || true

# "What changed recently?"
journalctl --since "1 day ago" --no-pager | tail -n 200
ls -lt /etc | head


⸻

20) Handy one-liners

# Top 20 largest directories under /
du -xhd1 / 2>/dev/null | sort -h | tail -n 20

# Top 20 largest files under /var
find /var -type f -printf '%s\t%p\n' 2>/dev/null | sort -n | tail -n 20 | awk '{printf "%.1fMB\t%s\n",$1/1024/1024,$2}'

# Show ports with process names (pretty)
ss -tulpn | awk 'NR==1 || /LISTEN/ {print}'

# Follow nginx errors (adjust path per distro)
tail -f /var/log/nginx/error.log


⸻

21) References (common paths)

/etc/ssh/sshd_config
/etc/ssh/sshd_config.d/
/etc/nginx/nginx.conf
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
/var/log/
/var/log/syslog (Ubuntu)
/var/log/auth.log (Ubuntu)
/etc/systemd/system/
/etc/fstab

