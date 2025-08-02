# Understanding `$PATH` in Linux

## What is `$PATH`?

`$PATH` is an environment variable that tells your shell **where to look for executable programs** when you type a command.

For example:

```bash
python
```

Instead of manually running:

```bash
/home/lorelei/miniconda3/bin/python
```

## How it Works

When you enter a command, Linux checks each directory listed in `$PATH`, from **left to right**, and runs the **first matching executable** it finds.

## View Your PATH

```bash
echo $PATH
```

Output example:

```bash
/home/lorelei/miniconda3/bin:/home/lorelei/.cargo/bin:/usr/bin:/bin
```

Each item is a directory, separated by colons.

## Find Command Locations

Use:

```bash
which <command>
```

### Example:

```bash
which python     # → /home/lorelei/miniconda3/bin/python
which cargo      # → /home/lorelei/.cargo/bin/cargo
which conda      # → /home/lorelei/miniconda3/bin/conda
```

This shows where each command is being sourced from.

## Adding to Your PATH

### Temporarily (for this session only):

```bash
export PATH=$PATH:/your/custom/path
```

### Permanently:

Add to your `~/.bashrc` or `~/.profile`:

```bash
echo 'export PATH=$PATH:/your/custom/path' >> ~/.bashrc
source ~/.bashrc
```

## Why PATH Order Matters

The shell uses the **first match it finds**. If a directory with a custom version of a tool (like `python`) comes **before** the system version, that one gets used.

## Common Directories in PATH

| Directory                       | Description                                  |
| ------------------------------- | -------------------------------------------- |
| `/home/youruser/miniconda3/bin` | Conda-managed Python & tools                 |
| `/home/youruser/.cargo/bin`     | Rust toolchain binaries                      |
| `/home/youruser/.local/bin`     | Pip `--user` installed Python tools          |
| `/usr/bin`, `/bin`              | System-wide commands                         |
| `/snap/bin`                     | Snap package binaries                        |
| `/usr/local/bin`                | Locally compiled or manually installed tools |

## Troubleshooting `$PATH`

### Problem: `command not found`

* Run `echo $PATH` to confirm directories
* Use `which command` to see if it’s available

### Problem: Wrong version of command running

* Reorder `$PATH` so the desired tool comes first
* Or run the full path to the executable manually:

```bash
/home/lorelei/miniconda3/bin/python script.py
```

---

Keep this note handy when troubleshooting environment or version conflicts across Python, Node, Rust, etc.
