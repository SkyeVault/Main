# File Extensions

## Introduction
Git supports various file types for **code, documentation, and configurations**. Each file extension has a specific purpose. This guide explains the most common file types used in GitHub repositories.

---

## What is a `.md` File?
- **`.md` stands for Markdown**, a lightweight markup language.
- It is mainly used for **documentation**, such as `README.md` files.
- Markdown allows **easy formatting** with plain text.
- GitHub **automatically renders Markdown** into readable text.

**Example Markdown Syntax:**
```markdown
# This is a Heading
**Bold text** and *italic text*  
- Bullet list item  
1. Numbered list item
`This creates a box around text`
```

 **Where `.md` is Used:**
- `README.md` (Repository overview)
- `CONTRIBUTING.md` (Contributor guidelines)
- `SECURITY.md` (Security policies)
- Any documentation in `/docs/`

---

## Other Common File Extensions on GitHub
| Extension | Description | Usage |
|-----------|------------|-------|
| **`.txt`** | Plain text file | Simple notes, logs, documentation |
| **`.json`** | JavaScript Object Notation | Config files (AWS policies, API responses) |
| **`.yaml` / `.yml`** | YAML Ain't Markup Language | Config files (GitHub Actions, Docker, AWS CloudFormation) |
| **`.sh`** | Shell script | Bash scripts for automation (installations, AWS commands) |
| **`.py`** | Python script | Python scripts for automation, APIs, and security tools |
| **`.html`** | HyperText Markup Language | Web development, GitHub Pages |
| **`.css`** | Cascading Style Sheets | Styling for web pages |
| **`.js`** | JavaScript | Frontend & backend development (Node.js, React) |
| **`.ipynb`** | Jupyter Notebook | Data science and machine learning projects |
| **`.mdx`** | Extended Markdown | Interactive documentation with React components |
| **`.lock`** | Dependency lock files | Used in package managers (`package-lock.json`, `Pipfile.lock`) |
| **`.gitignore`** | Git ignore file | Specifies files Git should **not track** |

---

## How GitHub Uses These Files
- **Text-based files** (`.md`, `.txt`, `.json`, `.yaml`, `.gitignore`) are displayed **directly in the browser**.
- **Scripts & code files** (`.py`, `.sh`, `.js`) can be **executed in repositories** (e.g., GitHub Actions, AWS Lambda).
- **Configuration files** (`.json`, `.yaml`) define **how GitHub services interact** with AWS, CI/CD, and Docker.

---

## What Should You Use?
- **For documentation:** Use **Markdown (`.md`)**.
- **For AWS & config files:** Use **YAML (`.yaml`)** or **JSON (`.json`)**.
- **For automation scripts:** Use **Bash (`.sh`)** or **Python (`.py`)**.
- **For web development:** Use **HTML, CSS, and JavaScript (`.html`, `.css`, `.js`)**.


