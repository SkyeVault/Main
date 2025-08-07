Linux Tools for Developers – Study Guide

**Course:** Linux Tools for Developers (Linux Foundation)  
**Format:** Detailed command syntax, practical examples, best practices, common pitfalls, and study strategies  
**Goal:** Develop proficiency in command-line operations and mastery of developer-focused Linux tools

---

## Table of Contents
1. [File and Directory Management](#1-file-and-directory-management)
2. [Finding and Filtering Files](#2-finding-and-filtering-files)
3. [Text Viewing and Manipulation](#3-text-viewing-and-manipulation)
4. [Essential Utilities](#4-essential-utilities)
5. [Bash Scripting Basics](#5-bash-scripting-basics)
6. [Files and Filesystems](#6-files-and-filesystems)
7. [Permissions and Ownership](#7-permissions-and-ownership)
8. [Compiling and Debugging](#8-compiling-and-debugging)
9. [Packaging Software](#9-packaging-software)
10. [Study Strategies and Retention Techniques](#10-study-strategies-and-retention-techniques)

---

## 1. File and Directory Management

This section covers commands for creating, managing, and deleting files and directories, which are fundamental for navigating and organizing a Linux filesystem.

**Commands:**
```bash
ls -lAh --color=auto  # Lists files in long format, including hidden files, with human-readable sizes and colorized output
touch file.txt        # Creates an empty file or updates the timestamp of an existing file
mkdir -p dir/subdir   # Creates directories, including parent directories, without errors if they exist
rm -rf dir/           # Deletes a directory and its contents recursively (use with caution)
mv old.txt new.txt    # Renames or moves files/directories
cp -r src/ dest/      # Copies files or directories recursively
```

**Best Practices:**
- **Verify before deleting:** Always use `ls -l` or `ls -R` to inspect contents before running `rm -rf` to prevent accidental data loss.
- **Interactive mode:** Use `-i` with `mv` or `cp` (e.g., `mv -i` or `cp -i`) to prompt for confirmation before overwriting files.
- **Use absolute paths for safety:** When moving or copying critical files, specify full paths (e.g., `/home/user/docs`) to avoid errors in the wrong directory.

**Common Pitfalls:**
- Running `rm -rf *` in the wrong directory can delete unintended files. Always double-check the current directory with `pwd`.
- Forgetting `-r` in `cp` when copying directories leads to errors; always include it for recursive operations.

---

## 2. Finding and Filtering Files

Efficiently locating and filtering files is critical for managing large filesystems or debugging issues.

**Commands:**
```bash
find /path -name "*.log"            # Searches for files matching a pattern (e.g., all .log files)
find . -type f -size +10M           # Finds files larger than 10 MB
find . -mtime -7                    # Finds files modified in the last 7 days
locate config.json                  # Searches a pre-built database for files (faster but requires updated database)
grep -r "pattern" /etc              # Recursively searches for text in files
grep -Ei "error|fail" logfile       # Case-insensitive search for "error" or "fail"
```

**Best Practices:**
- **Update locate database:** Run `sudo updatedb` to refresh the `locate` command’s database, especially after creating new files.
- **Combine find with exec:** Use `find . -name "*.tmp" -exec rm {} \;` to perform actions (e.g., delete) on matching files.
- **Optimize grep:** Use `-r` for recursive searches and `-l` to list only matching filenames for faster results.

**Common Pitfalls:**
- Forgetting to quote patterns in `find -name` (e.g., `*.log`) can cause shell expansion errors; always use quotes (e.g., `"*.log"`).
- Running `grep -r` on large directories like `/` can be slow; narrow the scope to specific directories (e.g., `/etc`).

---

## 3. Text Viewing and Manipulation

These tools allow developers to view, process, and transform text files, which are common in log analysis, data processing, and scripting.

**Viewing Commands:**
```bash
cat file.txt                # Displays entire file content
less file.txt               # Views file interactively with scrolling
head -n 20 file.txt         # Shows first 20 lines of a file
tail -f /var/log/syslog     # Monitors a file for changes in real-time
```

**Processing Commands:**
```bash
sort file.txt | uniq -c          # Sorts lines and counts unique occurrences
cut -d',' -f1,3 data.csv         # Extracts fields 1 and 3 from a CSV file using comma as delimiter
awk '{print $1, $3}' file.txt    # Prints columns 1 and 3 from a space-separated file
sed 's/error/issue/g' file.txt   # Replaces all instances of "error" with "issue"
paste file1 file2                # Merges lines from two files side-by-side
join file1 file2                 # Joins two files based on a common field
split -l 1000 bigfile chunk_     # Splits a file into chunks of 1000 lines each
```

**Regular Expressions with `grep`:**
```bash
grep -E "foo|bar" file.txt       # Matches lines containing "foo" or "bar" using extended regex
grep -P "colou?r" file.txt       # Matches "color" or "colour" using Perl-compatible regex
```

**Best Practices:**
- **Compressed files:** Use `zcat`, `zgrep`, or `zless` for .gz files to avoid manual decompression.
- **Efficient awk for CSVs:** Use `awk -F',' '{sum+=$3} END {print sum}' file.csv` to compute sums or perform calculations on CSV columns.
- **Streamline pipelines:** Combine tools (e.g., `cat file.txt | sort | uniq`) for efficient data processing.

**Common Pitfalls:**
- Using `cat` for large files can overwhelm the terminal; prefer `less` for browsing.
- Forgetting to escape special characters in `sed` or `grep` regex patterns can lead to unexpected results.

---

## 4. Essential Utilities

These utilities provide additional functionality for counting, splitting output, and extracting data from files.

**Commands:**
```bash
wc -l file.txt              # Counts lines in a file
wc -w file.txt              # Counts words in a file
tee output.txt              # Writes output to both a file and stdout
strings binary.bin          # Extracts printable strings from binary files
```

**Best Practices:**
- **Append with tee:** Use `tee -a` to append to a file instead of overwriting.
- **Pipeline with wc:** Use `wc` in pipelines (e.g., `grep "error" log | wc -l`) to count matches.
- **Debug binaries:** Use `strings` to inspect binary files for readable content, useful for debugging.

**Common Pitfalls:**
- Forgetting `tee` redirects output; ensure downstream commands receive input via pipelines.

---

## 5. Bash Scripting Basics

Bash scripting automates repetitive tasks and enhances productivity for developers.

**Script Structure:**
```bash
#!/bin/bash
# Script to process text files
echo "Hello, $USER"
for f in *.txt; do
  echo "Processing $f"
done
```

**Key Elements:**
- **Variables:** `name="Lorelei"` – Assign values with no spaces around `=`.
- **Conditionals:**
```bash
if [ -f "$file" ]; then
  echo "File exists"
fi
```
- **Loops:**
```bash
for i in {1..5}; do
  echo "Iteration $i"
done
```
- **Functions:**
```bash
myfunc() {
  echo "Hello, $1"
}
myfunc World
```

**Best Practices:**
- **Make scripts executable:** Run `chmod +x script.sh` to allow execution.
- **Stop on errors:** Add `set -e` at the script’s start to exit on any error.
- **Safe variable usage:** Always quote variables (e.g., `"$var"`) to handle spaces or empty values correctly.

**Common Pitfalls:**
- Omitting `#!/bin/bash` can cause compatibility issues on different shells.
- Unquoted variables (e.g., `$var` vs. `"$var"`) can lead to errors with filenames containing spaces.

---

## 6. Files and Filesystems

Understanding filesystem types and management is key for developers working with storage.

**File Types:**
- Regular files, directories, symbolic links, block devices, character devices, sockets, and named pipes (FIFOs).

**Commands:**
```bash
file name.txt                # Identifies file type
mount /dev/sdb1 /mnt         # Mounts a filesystem
umount /mnt                  # Unmounts a filesystem
df -h                        # Displays disk usage in human-readable format
du -sh *                     # Summarizes disk usage for files/directories
```

**Best Practices:**
- **Loopback filesystems:** Create a test filesystem with:
```bash
dd if=/dev/zero of=disk.img bs=1M count=100  # Creates a 100 MB image
mkfs.ext4 disk.img                           # Formats as ext4
mount -o loop disk.img /mnt                  # Mounts as loop device
```
- **Monitor disk usage:** Use `df -h` and `du -sh` regularly to manage storage.

**Common Pitfalls:**
- Forgetting to unmount (`umount`) a device before removal can corrupt data.
- Incorrect `dd` parameters can overwrite critical data; always verify arguments.

---

## 7. Permissions and Ownership

File permissions and ownership control access and security in Linux.

**Commands:**
```bash
ls -l                        # Displays permissions and ownership
chmod 755 script.sh          # Sets executable permissions for owner, group, others
chown user:group file.txt    # Changes owner and group
umask 022                    # Sets default permissions for new files
```

**Permission Types:**
- **setuid:** File runs with owner’s permissions (e.g., `chmod u+s file`).
- **setgid:** File runs with group’s permissions (e.g., `chmod g+s dir`).
- **Sticky bit:** Restricts deletion in shared directories (e.g., `chmod +t dir`).

**Best Practices:**
- **Octal notation:** Use `r=4`, `w=2`, `x=1` (e.g., `chmod 640 file` = owner read/write, group read, others none).
- **Secure defaults:** Set `umask 022` for secure default permissions (owner rw, others r).

**Common Pitfalls:**
- Incorrect `chmod` values (e.g., `777`) can expose files to unauthorized access.
- Forgetting to update group ownership with `chown :group` can cause access issues.

---

## 8. Compiling and Debugging

Compiling and debugging are essential for building and troubleshooting software.

**GCC Compilation:**
```bash
gcc -Wall -g main.c -o app             # Compiles with warnings and debug symbols
gcc main.c -I/include/path -L/lib/path -lmylib  # Specifies include and library paths
```

**Library Creation:**
```bash
ar rcs libstatic.a file.o       # Creates a static library
gcc -shared -o libshared.so file.o  # Creates a shared library
```

**Debugging with GDB:**
```bash
gdb ./app
break main           # Sets breakpoint at main function
run                  # Starts execution
print var            # Prints variable value
next                 # Steps to next line
continue             # Resumes execution
quit                 # Exits GDB
```

**Best Practices:**
- **Enable debugging:** Always use `-g` with `gcc` to include debug symbols.
- **Check dependencies:** Use `ldd app` to verify linked libraries.
- **Use warnings:** Compile with `-Wall` to catch potential issues early.

**Common Pitfalls:**
- Omitting `-g` makes debugging with GDB difficult.
- Incorrect library paths can cause linking errors; verify with `-I` and `-L`.

---

## 9. Packaging Software

Packaging software ensures portability and ease of installation.

**RPM Workflow:**
1. Create a `.spec` file defining package metadata and files.
2. Build with:
```bash
rpmbuild -ba package.spec
```

**Debian Workflow:**
```bash
dpkg-deb --build mypackage/  # Builds a .deb package
```

**Best Practices:**
- **Accurate spec files:** Ensure the `%files` section in `.spec` lists only necessary files to avoid packaging errors.
- **Clean builds:** Use virtual machines or containers to isolate build environments and avoid dependency conflicts.

**Common Pitfalls:**
- Missing dependencies in `.spec` files can cause installation failures.
- Building as root can introduce security risks; use a non-root user when possible.

---

## 10. Study Strategies and Retention Techniques

Effective study habits are crucial for mastering Linux tools.

- **Practice actively:** Type commands manually to build muscle memory instead of copying and pasting.
- **Safe experimentation:** Create a dedicated `playground/` directory for testing commands without risking critical files.
- **Group commands by purpose:** Organize commands into categories for easier recall:
  - **File finding:** `find`, `locate`
  - **Text viewing:** `cat`, `less`, `head`, `tail`
  - **Text processing:** `sed`, `awk`, `cut`
- **Master regular expressions:** Practice regex with `grep -E` or `grep -P` to enhance search capabilities.
- **Daily practice:** Dedicate time each day to use 2–3 commands in real-world scenarios (e.g., parsing logs with `grep`).
- **Leverage manpages:** Run `man <command>` (e.g., `man grep`) and experiment with provided examples to deepen understanding.

---

## Quick Reference – Command Flags

| Command | Common Flags | Purpose |
|---------|--------------|---------|
| `ls`    | `-l`, `-a`, `-h`, `--color=auto` | Long format, include hidden files, human-readable sizes, colorized output |
| `find`  | `-name`, `-type`, `-size`, `-mtime` | Search by name, type, size, or modification time |
| `grep`  | `-i`, `-r`, `-E`, `-P` | Case-insensitive, recursive, extended regex, Perl regex |
| `chmod` | `u+x`, `755`, `g-w` | Add execute for user, set permissions octal, remove write for group |
| `awk`   | `-F','`, `'{print $1}'` | Set delimiter, print specific columns |
| `sed`   | `'s/old/new/g'` | Replace all occurrences of text |