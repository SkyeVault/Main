
---

# Linux Orientation Notes

## Module 1: Introduction to Linux

### Kernel vs Operating System

* **Kernel**: Core system controlling hardware interactions.
* **Operating System**: Includes kernel + tools/utilities (e.g. bash, systemd, X server).
* Use `uname -r` to check kernel version.

### History and Philosophy

* **UNIX Origins** → BSD → Linux (Torvalds, 1991)
* Emphasis on **modularity**, **open source**, and **portability**.

### Linux Distributions

* **Debian-based** (Ubuntu, Kali)
* **RPM-based** (Fedora, CentOS, RHEL)
* Use `lsb_release -a` or `cat /etc/os-release` to check distro info.

### Linux Standard Base (LSB)

* Standardizes core libraries, directory structures.
* `lsb_release` command often used to comply.

---

## Module 1 Tools

### `sudo` – Run commands as superuser

```bash
sudo <command>
```

* Example: `sudo apt update`
* Gives temporary root permissions.
* Defined in `/etc/sudoers`.

### Terminal Help Commands

| Tool     | Usage Example    | Notes               |
| -------- | ---------------- | ------------------- |
| `man`    | `man ls`         | Manual pages        |
| `info`   | `info coreutils` | Hypertext format    |
| `--help` | `ls --help`      | Inline help         |
| `help`   | `help cd`        | Shell builtins only |

---

### Graphical Environments

* **X11** is the base graphical layer.
* **GNOME**: clean, modern (Ubuntu default).
* **KDE**: customizable, powerful (used by Plasma).
* Try both with `startx` if not auto-launched.

### Labs

* **Multiple Workspaces**: `Ctrl + Alt + Left/Right`
* **Terminal Tabs**: Usually `Ctrl + Shift + T`

---

## Module 2: Starting to Work in Linux

### `echo` and `cat`

```bash
echo "text" > file.txt   # Write text to file
cat file.txt             # View file content
```

### Text Editors

#### `vi` / `vim`

* Modes: Normal (`Esc`), Insert (`i`), Command (`:`)
* Save/Quit: `:w`, `:q`, `:wq`
* Delete: `dd`, `x`

#### `emacs`

* Commands: `Ctrl-x Ctrl-s` (save), `Ctrl-x Ctrl-c` (exit)
* Powerful for scripting and file editing

---

### Shells and Initialization

* **Bash** (`/bin/bash`) is default shell.
* Init files:

  * `/etc/profile`
  * `~/.bashrc`
  * `~/.bash_profile`

### Aliases

```bash
alias ll='ls -l --color=auto'
```

### Environment Variables

```bash
echo $PATH
export EDITOR=vim
```

### Prompt Customization

```bash
PS1='\u@\h:\w\$ '
```

* \u = user, \h = host, \w = current dir

---

### Special Characters & Redirection

| Symbol | Meaning                                |                                |                             |
| ------ | -------------------------------------- | ------------------------------ | --------------------------- |
| `>`    | Redirect stdout to file (overwrite)    |                                |                             |
| `>>`   | Append stdout to file                  |                                |                             |
| `<`    | Redirect file to stdin                 |                                |                             |
| \`     | \`                                     | Pipe output to another command |                             |
| `&&`   | Run next command if previous succeeded |                                |                             |
| \`     |                                        | \`                             | Run next if previous failed |

```bash
ls | grep txt
```

### Command Substitution

```bash
echo "Today is $(date)"
```

---

### Filesystems & Partitions

#### Filesystem Layout

* `/`: root
* `/etc`: config
* `/home`: user dirs
* `/var`: logs, variable data
* `/tmp`: temp files
* `/usr`: user programs

#### Partitioning Tools

* `fdisk`, `parted`, `lsblk`, `df -h`, `mount`

---

### Hard vs Symbolic Links

```bash
ln file.txt hardlink.txt    # Hard link
ln -s file.txt symlink.txt  # Symbolic link
```

---

## Module 3: System Components

### Boot Process

* BIOS/UEFI → GRUB → Kernel → `init`/`systemd`

#### `/boot`

* Contains kernel, initrd, GRUB configs

#### GRUB

* `/boot/grub/grub.cfg`
* To update: `update-grub` or `grub2-mkconfig`

---

### System Initialization

* `systemd`: Main init system

```bash
systemctl status
systemctl list-units
```

### Memory and Swap

```bash
free -h
swapon --show
```

### OOM Killer

* Out of Memory handler
* Triggered by low memory; logs in `dmesg`

---

### Networking

#### Tools

```bash
ip addr        # Interface info
ip route       # Routing table
```

* `ip` is the modern replacement for `ifconfig`

#### Predictable Interface Names

* Example: `enp0s3`, `wlp2s0`

#### Static IP Config (Debian)

Edit `/etc/network/interfaces` or use `nmcli`

---

## Module 4: Command Details

### Basic Utilities

* `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv`, `touch`
* Use `type` to check if command is builtin or binary:

```bash
type cd
```

### File Transfer

* `scp`, `rsync`, `wget`, `curl`

```bash
scp file user@host:/path
```

---

### System Monitoring

* `top`, `htop`, `free`, `uptime`, `vmstat`, `iostat`
* Graphical: `ksysguard`

```bash
sudo apt install ksysguard
```

---

### Kernel Modules

* `lsmod`, `modprobe`, `rmmod`

```bash
modprobe i2c-dev
```

---

### Device Management

* `udevadm info`, `/dev`, `/sys/class`

---

### System Services

```bash
systemctl start <service>
systemctl stop <service>
systemctl enable <service>
```

---

## Module 5: System Admin & User Management

### Package Managers

| Distro    | Tool           | Example               |
| --------- | -------------- | --------------------- |
| Debian    | `apt`          | `sudo apt install`    |
| Red Hat   | `dnf`          | `sudo dnf install`    |
| OpenSUSE  | `zypper`       | `sudo zypper install` |
| Universal | `rpm` / `dpkg` | Manual package mgmt   |

---

### User Management

```bash
useradd <name>
passwd <name>
usermod -aG sudo <name>
```

### User Environment

* User files: `/etc/passwd`, `/etc/shadow`, `/etc/group`
* Home directory: `/home/<username>`

---

### Permissions

```bash
chmod 755 file
chown user:group file
```

---

### Log Files

* Location: `/var/log`
* Tools: `journalctl`, `tail`, `less`

---

### sudo vs su

* `sudo`: execute single command as root
* `su`: switch to root shell session

---

## Bonus: Git & Open Source

* Version control: `git init`, `git clone`, `git commit`, `git push`
* Explore open source by contributing to GitHub projects

---
