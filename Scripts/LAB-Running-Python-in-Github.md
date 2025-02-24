# **Lab: Running Python Scripts on GitHub**

This lab guides you through **running Python scripts** on GitHub using **GitHub Actions, GitHub Codespaces, and local execution**.

---

## **Lab Objectives**
By the end of this lab, you will:
✅ Understand how GitHub handles Python files.  
✅ Set up **GitHub Actions** to automatically run Python scripts.  
✅ Use **GitHub Codespaces** to run Python in the cloud.  
✅ Execute Python scripts locally using Git.  

---

## **1. Prerequisites**
Before starting, ensure you have:
- A **GitHub account**.
- Python **installed locally** (`python --version` to check).
- A GitHub repository to store your Python scripts.

---

## **2. Running Python Scripts Using GitHub Actions**
GitHub Actions allows Python scripts to run **automatically** when pushing changes.

### **Step 1: Create a GitHub Workflow**
1. Navigate to your **GitHub repository**.
2. Create a **new directory**:
   ```sh
   mkdir -p .github/workflows/
   ```
3. Inside this directory, create a new file:
   ```sh
   touch .github/workflows/run_python.yml
   ```

### **Step 2: Add the GitHub Actions Workflow**
Paste the following code into `run_python.yml`:

```yaml
name: Run Python Script

on: [push]  # Triggers when pushing code

jobs:
  run_python:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set Up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: pip install -r requirements.txt  # If dependencies exist

      - name: Run Python Script
        run: python script.py  # Replace with your Python script filename
```

### **Step 3: Commit and Push Changes**
Run the following commands to push the workflow:
```sh
git add .github/workflows/run_python.yml
git commit -m "Added GitHub Actions workflow for Python"
git push origin main
```

Now, your Python script **will execute automatically** every time you push code!

---

## **3. Running Python Code in GitHub Codespaces**
GitHub Codespaces provides a **cloud-based VS Code environment** to run Python scripts.

### **Step 1: Open Codespaces**
1. Open your **GitHub repository**.
2. Click on the **"Code"** button → **"Codespaces"** tab.
3. Click **"Create Codespace on main"**.

### **Step 2: Run Python in the Codespace Terminal**
1. Open the **terminal**.
2. Run the Python script:
   ```sh
   python script.py
   ```

---

## **4. Running Python Code Locally**
If you prefer to run the Python script on your machine:

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### **Step 2: Install Dependencies (If Required)**
```sh
pip install -r requirements.txt
```

### **Step 3: Run the Python Script**
```sh
python script.py
```

---

## **5. Can I Run Python on GitHub Pages?**
❌ **No**, GitHub Pages only supports **static files** (HTML, CSS, JS).  
✅ **Use GitHub Actions or Codespaces** for Python execution.

---

## **6. Summary**
| **Method** | **Executes Python Code?** | **Where?** |
|------------|-------------------|----------|
| **GitHub Actions** | ✅ Yes | Automated execution on push |
| **GitHub Codespaces** | ✅ Yes | Cloud-based VS Code environment |
| **Local Machine** | ✅ Yes | Runs via `python script.py` |
| **GitHub Pages** | ❌ No | Only serves static websites |

---

## **7. Cleanup (Optional)**
- To remove **GitHub Actions Workflow**, delete `.github/workflows/run_python.yml`.
- To stop using **Codespaces**, go to **"Your Codespaces"** and delete instances.

---

## **8. Additional Resources**
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Codespaces](https://github.com/features/codespaces)
- [Python on GitHub](https://docs.github.com/en/codespaces)

---

## **Lab Completion**
🎉 **Congratulations!** You have successfully run Python scripts using:
✅ **GitHub Actions**  
✅ **GitHub Codespaces**  
✅ **Local Execution**  

🚀 **Now try modifying the script and pushing updates to see GitHub Actions in action!**

