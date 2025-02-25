# GitHub Navigation Guide

## 📌 Introduction
This guide provides essential GitHub navigation instructions, covering how to:
- Create and move folders
- Rename files and directories
- Clone repositories
- Publish updates to GitHub via the terminal

---

## 📂 Creating Folders in GitHub
Git does not track empty folders, so you must add a file inside.

### **1️⃣ Create a Folder Locally**
```bash
mkdir New-Folder
```

### **2️⃣ Ensure the Folder Appears in GitHub**
Create a `README.md` inside it:
```bash
touch New-Folder/README.md
```
Then stage, commit, and push:
```bash
git add New-Folder
git commit -m "Added New-Folder"
git push origin main
```

---

## 🔄 Moving Folders and Files
To reorganize files within your repository, use the `mv` command.

### **1️⃣ Move a File into a Folder**
```bash
mv filename.txt New-Folder/
```

### **2️⃣ Move a Folder to a Different Location**
```bash
mv Old-Folder/ New-Location/
```

### **3️⃣ Commit and Push the Changes**
```bash
git add .
git commit -m "Moved files and folders"
git push origin main
```

---

## ✏️ Renaming Files and Folders
### **1️⃣ Rename a File**
```bash
mv oldname.txt newname.txt
```

### **2️⃣ Rename a Folder**
```bash
mv old-folder-name new-folder-name
```

### **3️⃣ Commit and Push the Changes**
```bash
git add .
git commit -m "Renamed files and folders"
git push origin main
```

---

## 📥 Cloning a GitHub Repository
### **1️⃣ Clone a Repository Using HTTPS**
```bash
git clone https://github.com/your-username/your-repo.git
```

### **2️⃣ Move into the Cloned Directory**
```bash
cd your-repo
```

---

## 🚀 Publishing Updates to GitHub via Terminal
### **1️⃣ Stage Changes for Commit**
```bash
git add .
```
Or stage a specific file:
```bash
git add filename.txt
```

### **2️⃣ Commit the Changes**
```bash
git commit -m "Your commit message here"
```

### **3️⃣ Push to GitHub**
```bash
git push origin main
```

If your push is rejected due to an outdated local branch, first pull the latest changes:
```bash
git pull origin main --rebase
```
Then push again:
```bash
git push origin main
```

---

## ✅ Summary
- Use `mkdir` and `touch` to create folders and files.
- Move files using `mv`, and rename them the same way.
- Use `git add`, `git commit`, and `git push` to publish updates.
- If necessary, run `git pull --rebase` to sync before pushing.

By mastering these GitHub commands, you can effectively navigate and manage your repositories! 🚀
