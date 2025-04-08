# Running Bash Scripts: A Beginner's Guide

## Introduction
Bash (**Bourne Again Shell**) is a command-line interpreter that allows users to run commands and automate tasks using scripts. This guide covers how to create, execute, and manage Bash scripts.

---

## 1. Creating a Bash Script
Bash scripts are simple text files containing a series of commands.

### **1. Create a New Script File**
Use `touch` or a text editor to create a script file:
```bash
touch myscript.sh
```
Or open it directly in a text editor:
```bash
nano myscript.sh
```

### **2. Add the Shebang Line**
Every Bash script starts with a **shebang** (`#!`) followed by the path to the Bash interpreter:
```bash
#!/bin/bash
```
This ensures the script runs using Bash.

### **3. Add Commands**
Example script (`myscript.sh`):
```bash
#!/bin/bash

echo "Hello, World!"
```

---

## 2. Making a Script Executable
Before running a script, you must grant it execute permission:
```bash
chmod +x myscript.sh
```

---

## 3. Running a Bash Script
### **1. Run Using `./`**
Execute the script by specifying its path:
```bash
./myscript.sh
```

### **2. Run Using `bash`**
Execute the script explicitly with Bash:
```bash
bash myscript.sh
```

### **3. Run Using `sh`**
You can also run the script using `sh`, but some Bash-specific features may not work:
```bash
sh myscript.sh
```

---

## 4. Using Variables in Scripts
```bash
#!/bin/bash

name="Alice"
echo "Hello, $name!"
```

---

## 5. Reading User Input
```bash
#!/bin/bash

echo "Enter your name:"
read name
echo "Hello, $name!"
```

---

## 6. Conditional Statements
```bash
#!/bin/bash

if [ "$1" == "hello" ]; then
    echo "Hello there!"
else
    echo "You didn't say hello."
fi
```
Run the script with:
```bash
./myscript.sh hello
```

---

## 7. Loops in Bash Scripts
### **For Loop**
```bash
#!/bin/bash

for i in {1..5}; do
    echo "Number $i"
done
```

### **While Loop**
```bash
#!/bin/bash

count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

---

## 8. Running Scripts at Startup
To run a script at startup, add it to your `.bashrc` or `.bash_profile`:
```bash
echo "./myscript.sh" >> ~/.bashrc
```
Or schedule it using `crontab`:
```bash
crontab -e
```
Then add:
```bash
@reboot /path/to/myscript.sh
```

---

## Conclusion
- Create a Bash script using a text editor.
- Add `#!/bin/bash` at the top.
- Use `chmod +x` to make it executable.
- Run it using `./script.sh` or `bash script.sh`.

Bash scripting is powerful for automation, DevOps, and cloud security tasks. Try creating your own script to automate a task!
