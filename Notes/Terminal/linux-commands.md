# Linux Command Line Master Reference

## Overview

This document provides a comprehensive list of Linux commands, organized by category, with additional notes, rules, and usage examples. It also includes bonus sections on Git and shell usage best practices.

---

## Command Syntax

```
command [options] [arguments]
```

- `command`: The executable or script to run.
- `options`: Modify behavior of the command (e.g., `-l`, `--help`).
- `arguments`: Inputs to the command, such as files or directories.

---

## Fundamental Rules

1. Linux is case-sensitive.
2. Everything is treated as a file: directories, devices, and even processes.
3. Absolute paths start with `/`, relative paths do not.
4. Use `man <command>` to access manual pages.
5. Use `--` to signify the end of command options if needed.
6. `*` matches any number of characters in filenames.
7. Redirect output using `>`, append with `>>`, and pipe with `|`.
8. Use `tab` for auto-completion.
9. Use `CTRL+C` to cancel, `CTRL+Z` to pause, `fg`/`bg` to manage jobs.

---

## File & Directory Management

```bash
ls -lah               # List directory contents in detail
cd /path/to/dir       # Change directory
pwd                   # Show current directory
mkdir mydir           # Make new directory
rmdir mydir           # Remove empty directory
rm -rf dir            # Remove directory and contents
cp file1 file2        # Copy file
mv file1 file2        # Move or rename file
touch file            # Create empty file
find / -name "file"   # Find file from root
tree                  # Visual directory structure
```

## Viewing & Manipulating Files

```bash
cat file              # View file content
less file             # Scroll through file
head -n 20 file       # First 20 lines
tail -f file          # Follow updates to file
grep 'term' file      # Search term in file
awk '{print $1}' file # Print column 1
sed 's/foo/bar/' file # Replace text
sort file             # Sort lines
uniq file             # Remove duplicates
```

## User Management

```bash
whoami                # Show current user
id                    # Show user/group info
adduser newuser       # Create new user
deluser newuser       # Delete user
passwd newuser        # Change user password
groups                # Show groups for user
sudo su               # Become root
```

## File Permissions

```bash
chmod 755 script.sh   # Set executable permission
chown user:group file # Change owner
umask                 # Show default permissions
```

## Package Management (Debian/Ubuntu)

```bash
apt update            # Update repo index
apt upgrade           # Upgrade packages
apt install pkg       # Install package
apt remove pkg        # Remove package
dpkg -i pkg.deb       # Install .deb file manually
```

## Process Management

```bash
ps aux                # Show processes
top                   # Realtime system monitor
kill PID              # Kill process
killall name          # Kill by name
htop                  # Enhanced top (if installed)
nice, renice          # Priority of processes
```

## Networking

```bash
ping 8.8.8.8          # Test connectivity
ip a                  # Show IP address
netstat -tuln         # List listening ports
curl -I https://url   # HTTP header request
wget http://url       # Download file
ss -tuln              # Netstat alternative
traceroute 8.8.8.8    # Trace route
```

## Archives & Compression

```bash
tar -czvf archive.tar.gz folder/ # Compress
tar -xzvf archive.tar.gz         # Extract
zip -r archive.zip folder/       # Zip folder
unzip archive.zip                # Unzip file
gzip file                        # Compress
gunzip file.gz                   # Decompress
```

## System Monitoring

```bash
df -h                 # Disk usage
du -sh folder         # Folder size
free -h               # Memory usage
uptime                # System uptime
vmstat                # Virtual memory stats
dmesg | tail          # Kernel log
journalctl -xe        # Systemd logs
```

## Redirection & Pipes

```bash
command > file        # Overwrite output
command >> file       # Append output
command < inputfile   # Use input file
command1 | command2   # Pipe output to input
```

## Job Control

```bash
command &             # Run in background
jobs                  # List jobs
fg %1                 # Bring job to foreground
bg %1                 # Send to background
CTRL+Z                # Pause current job
```

---

## Git Essentials

```bash
git init                    # Initialize repo
git clone url               # Clone repo
git status                  # Show status
git add file                # Stage file
git commit -m "message"     # Commit changes
git push origin main        # Push to remote
git pull                    # Pull from remote
git branch                  # List branches
git checkout -b newbranch   # Create and switch branch
git merge branchname        # Merge branch
git log --oneline           # Compact commit history
git diff                    # Show changes
```

### Git Best Practices

- Commit often, with clear messages.
- Use branches for features/fixes.
- Rebase before merge if needed.
- Push to remote often to avoid data loss.

---

## Tips & Tricks

- Use `alias` to create command shortcuts in `.bashrc` or `.zshrc`.
- Use `history` and `!n` to rerun commands.
- Use `xargs` to execute on many inputs.
- Use `man`, `tldr`, or `--help` to learn commands.

---

## Conclusion

This markdown file serves as a core reference for Linux beginners and intermediate users. Keep it close while working on servers or scripting daily tasks.
