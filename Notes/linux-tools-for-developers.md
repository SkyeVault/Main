Can you fix this markdown guide that ChatGPT made for me? Remove emojis and make it more detailed and informative for a study guide
# 🐧 Linux Tools for Developers – Study Guide

> **Course:** Linux Tools for Developers (Linux Foundation)  
> **Format:** Command syntax, examples, pro tips, pitfalls, and study tips  
> **Goal:** Build practical command-line fluency and developer tool mastery

---

## 📌 Table of Contents
1. [File & Directory Management](#1-file--directory-management)
2. [Finding & Filtering Files](#2-finding--filtering-files)
3. [Text Viewing & Manipulation](#3-text-viewing--manipulation)
4. [Essential Utilities](#4-essential-utilities)
5. [Bash Scripting Basics](#5-bash-scripting-basics)
6. [Files & Filesystems](#6-files--filesystems)
7. [Permissions & Ownership](#7-permissions--ownership)
8. [Compiling & Debugging](#8-compiling--debugging)
9. [Packaging Software](#9-packaging-software)
10. [Study Tips & Memory Tricks](#10-study-tips--memory-tricks)

---

## 1. File & Directory Management

**Commands:**
```bash
ls -lAh --color       # list files (long, human-readable, hidden)
touch file.txt        # create empty file / update timestamp
mkdir -p dir/subdir   # make directories recursively
rm -rf dir/           # remove directory & contents
mv old.txt new.txt    # rename / move
cp -r src/ dest/      # copy recursively
```

**Pro Tips:**
- Always `ls` before running `rm -rf` to avoid disasters.
- Use `-i` on `mv`/`cp` to prompt before overwriting.

---

## 2. Finding & Filtering Files

```bash
find /path -name "*.log"       # find by name
find . -type f -size +10M      # files >10 MB
locate config.json             # search via database
grep -r "pattern" /etc         # recursive text search
grep -Ei "error|fail" logfile  # case-insensitive OR pattern
```

**Pro Tips:**
- Update `locate` DB: `sudo updatedb`
- Combine `find` + `exec`:  
  `find . -name "*.tmp" -exec rm {} \;`

---

## 3. Text Viewing & Manipulation

**Viewing:**
```bash
cat file.txt
less file.txt
head -n 20 file.txt
tail -f /var/log/syslog
```

**Processing:**
```bash
sort file.txt | uniq -c          # count unique lines
cut -d',' -f1,3 data.csv         # extract fields 1 and 3
awk '{print $1, $3}' file.txt    # print columns
sed 's/error/issue/g' file.txt   # replace text
paste file1 file2                # merge side-by-side
join file1 file2                  # join by common field
split -l 1000 bigfile chunk_      # split into 1000-line files
```

**Regex with `grep`:**
```bash
grep -E "foo|bar" file.txt
grep -P "colou?r" file.txt       # perl regex (color/colour)
```

**Pro Tips:**
- Use `zcat`, `zgrep` for compressed files.
- `awk` is great for quick CSV math:  
  `awk -F',' '{sum+=$3} END {print sum}' file.csv`

---

## 4. Essential Utilities

```bash
wc -l file.txt               # count lines
tee output.txt               # split output to file + stdout
strings binary.bin           # extract readable text
```

**Pro Tips:**
- `tee -a` appends instead of overwriting.
- `wc` works well in pipelines: `cat file | wc -w`

---

## 5. Bash Scripting Basics

**Structure:**
```bash
#!/bin/bash
# My Script

echo "Hello $USER"
for f in *.txt; do
  echo "Processing $f"
done
```

**Key Elements:**
- Variables: `name="Lorelei"`
- Conditionals:
```bash
if [ -f "$file" ]; then
  echo "Exists"
fi
```
- Loops:
```bash
for i in {1..5}; do echo $i; done
```
- Functions:
```bash
myfunc() { echo "Hello $1"; }
myfunc World
```

**Pro Tips:**
- Always run `chmod +x script.sh` before execution.
- Use `set -e` to stop on error.
- Use `"$var"` (quotes) to avoid word-splitting issues.

---

## 6. Files & Filesystems

**Types:**
- Regular, directory, symlink, block device, char device, socket, FIFO.

**Commands:**
```bash
file name.txt
mount /dev/sdb1 /mnt
umount /mnt
df -h
du -sh *
```

**Pro Tips:**
- Loopback FS creation:
```bash
dd if=/dev/zero of=disk.img bs=1M count=100
mkfs.ext4 disk.img
mount -o loop disk.img /mnt
```

---

## 7. Permissions & Ownership

```bash
ls -l
chmod 755 script.sh
chown user:group file.txt
umask 022
```

**Special Bits:**
- **setuid** – run with owner’s permissions
- **setgid** – run with group’s permissions
- **sticky bit** – restrict deletion in shared dirs (`chmod +t`)

**Pro Tips:**
- Octal: `r=4`, `w=2`, `x=1`
- `chmod 640 file` = owner rw, group r, others none

---

## 8. Compiling & Debugging

**GCC:**
```bash
gcc -Wall -g main.c -o app
gcc main.c -I/include/path -L/lib/path -lmylib
```

**Libraries:**
```bash
ar rcs libstatic.a file.o       # static
gcc -shared -o libshared.so file.o
```

**Debugging with GDB:**
```bash
gdb ./app
break main
run
print var
next
continue
quit
```

**Pro Tips:**
- Always compile with `-g` for debugging.
- Use `ldd app` to check linked libraries.

---

## 9. Packaging Software

**RPM Workflow:**
1. Create `.spec` file
2. Build:
```bash
rpmbuild -ba package.spec
```

**Debian Workflow:**
```bash
dpkg-deb --build mypackage/
```

**Pro Tips:**
- Keep `%files` section in `.spec` accurate to avoid packaging junk.
- Use virtual machines or containers for clean builds.

---

## 10. Study Tips & Memory Tricks

- **Muscle memory first** – type commands instead of copy-paste.
- **Safe testing** – create a `playground/` directory to experiment.
- **Group by task** – remember commands in *task categories*:
  - Finding files → `find`, `locate`
  - Viewing files → `cat`, `less`, `head`, `tail`
  - Editing streams → `sed`, `awk`
- **Regex habit** – integrate pattern matching into all searches.
- **Daily mini-lab** – pick 2–3 commands and use them in real scenarios.
- **Manpage mastery** – run `man grep` and try each example.

---

## Quick Reference – Command Flags

| Command | Common Flags | Purpose |
|---------|--------------|---------|
| ls      | `-l`, `-a`, `-h`, `--color` | long list, all files, human-readable |
| find    | `-name`, `-type`, `-size`, `-mtime` | search by property |
| grep    | `-i`, `-r`, `-E`, `-P` | case-insensitive, recursive, regex |
| chmod   | `u+x`, `755`, `g-w` | modify permissions |
| awk     | `-F','`, `'{print $1}'` | set delimiter, print columns |
| sed     | `'s/old/new/g'` | replace text |

---