# Git --Practical Guide & Reference

> A concise, copy-pasteable cheat-sheet with safe “undo” options, common workflows, and commands you’ll actually use.

---

## Mental Model

- **Working Directory (WD)**: Files on disk.
- **Index (Staging Area)**: Files staged for the next commit.
- **HEAD**: The current commit (usually the branch tip).

Key comparisons:
- `git diff`: WD vs Index (unstaged changes).
- `git diff --staged`: Index vs HEAD (staged changes).
- `git diff A B`: Differences between two commits/branches/tags.
- `git diff A...B`: Changes in **B** since the merge-base with **A**.

---

## First-Time Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "nano -w"  # or "code --wait", "vim"
git config --global color.ui auto
git config --global pull.ff only          # Fast-forward only for pulls
git config --global fetch.prune true      # Auto-prune stale branches
```

**Line Endings**: Use `.gitattributes` for consistent handling:

```gitattributes
* text=auto
*.sh text eol=lf
*.bat text eol=crlf
*.png binary
*.jpg binary
```

---

## Create or Clone a Repo

```bash
git init                              # Initialize new repo
git init --initial-branch=main        # Set initial branch name
git clone <url>                       # Full clone
git clone --depth=1 <url>             # Shallow clone (latest snapshot)
git clone --filter=blob:none <url>    # Partial clone (faster for large repos)
git clone --single-branch -b dev <url> # Clone single branch
```

---

## Daily Workflow

```bash
git status -sb                        # Short, branch-aware status
git add <file>                        # Stage specific file(s)
git add -p                            # Interactive staging (by hunks)
git restore <file>                    # Discard unstaged changes
git restore --staged <file>           # Unstage file (keep WD changes)
git commit -m "fix: clear error msg"  # Commit with clear message
git commit --amend --no-edit          # Amend last commit (same message)
git log --oneline --graph --all       # Visual commit history
git show <ref>                        # Inspect commit/branch/tag
```

**Commit Messages**:
- Subject: ≤50 chars, imperative (“Fix…”, “Add…”).
- Blank line, then details wrapped to 72 chars.
- Use **Conventional Commits**: `feat:`, `fix:`, `docs:`, `refactor:`, etc.

---

## Branching

```bash
git branch                            # List local branches
git branch -vv                        # Include upstream info
git branch -a                         # Include remote branches
git switch -c feat/x                  # Create and switch to new branch
git switch main                       # Switch to existing branch
git branch -d feat/x                  # Delete merged branch
git branch -D feat/x                  # Force delete unmerged branch
```

**Compare Branches**:
```bash
git diff main feat/x                  # Line-by-line differences
git log --oneline main..feat/x        # Commits in feat/x not in main
git log --oneline main...feat/x       # Changes since common ancestor
```

---

## Syncing with Remotes

```bash
git remote -v                         # List remotes
git remote add origin <url>           # Add remote
git fetch                             # Update remote refs
git fetch --all --prune               # Update and prune stale refs
git pull --ff-only                    # Fast-forward pull
git pull --rebase                     # Rebase local changes on remote
git push -u origin <branch>           # Push and set upstream
git push --force-with-lease           # Safe overwrite
```

**Best Practices**:
- Avoid `--force` on shared branches; use `--force-with-lease`.
- Use `pull --ff-only` or `pull --rebase` for linear history.

---

## Merging & Rebasing

```bash
git switch main
git merge feat/x                      # Merge with commit
git merge --ff-only feat/x            # Fast-forward merge only
git rebase main                       # Rebase current branch onto main
git rebase -i main                    # Interactive rebase (squash, reword)
```

**Resolve Conflicts**:
```bash
# Edit conflicted files, then:
git add <file>
git rebase --continue  # Or: git merge --continue
git rebase --abort     # Or: git merge --abort
```

---

## Tags (Releases)

```bash
git tag                               # List tags
git tag -a v1.2.0 -m "Release 1.2.0"  # Create annotated tag
git push origin v1.2.0                # Push specific tag
git push --tags                       # Push all tags
```

---

## Diffs

```bash
git diff                              # WD vs Index
git diff --staged                     # Index vs HEAD
git diff v1.0 v1.1 -- file.txt        # File between tags
git diff main...feat/x                # Changes since merge base
git diff --stat main feat/x           # Summary of changed files
```

---

## Undo & Recovery

| Action                                   | Command                               | Notes                     |
|------------------------------------------|---------------------------------------|---------------------------|
| Discard unstaged changes                | `git restore <file>`                  | Only uncommitted changes  |
| Unstage file                            | `git restore --staged <file>`         | Keeps WD changes          |
| Amend last commit                       | `git commit --amend`                  | Avoid if already pushed   |
| Revert a pushed commit                  | `git revert <sha>`                    | Creates inverse commit    |
| Undo last commit (keep staged)          | `git reset --soft HEAD~1`             | “Uncommit”                |
| Undo last commit (keep WD)              | `git reset --mixed HEAD~1`            | Default reset             |
| Discard last commit & changes           | `git reset --hard HEAD~1`             | **Dangerous**             |
| Recover “lost” commits                  | `git reflog` → `git reset --hard <ref>` | Use reflog to find refs |

**Stash**:
```bash
git stash push -m "wip: login form" -u  # Stash with untracked files
git stash list                          # List stashes
git stash pop                           # Apply and remove latest stash
git stash apply stash@{0}               # Apply specific stash
```

**Clean Untracked**:
```bash
git clean -n                          # Preview untracked files
git clean -fd                         # Remove untracked files/dirs
```

---

## Search & Inspect

```bash
git grep "pattern"                    # Search tracked files
git blame -L 10,20 file.c             # Who changed specific lines
git shortlog -sn                      # Commit count by author
git show <sha>:file.txt               # File content at commit
```

---

## Advanced Navigation

- **Refs**: `HEAD~2` (2 commits back), `HEAD^` (first parent), `branch@{yesterday}` (branch position yesterday).
- **Ranges**:
  - `A..B`: Commits in **B** not in **A**.
  - `A...B`: Commits in **A** or **B** but not both.
- **Pathspecs**: `-- src/` (limit to directory), `:(exclude)dist/` (exclude path).

---

## Worktrees & Sparse Checkouts

**Worktrees**:
```bash
git worktree add ../wt-docs docs      # New worktree for 'docs' branch
git worktree list                     # List worktrees
git worktree remove ../wt-docs        # Remove worktree
```

**Sparse Checkout**:
```bash
git sparse-checkout init --cone       # Enable sparse checkout
git sparse-checkout set src/ docs/    # Limit to specific paths
git sparse-checkout disable           # Revert to full checkout
```

---

## Submodules

```bash
git submodule add <url> lib/foo       # Add submodule
git submodule update --init --recursive  # Initialize submodules
git submodule foreach git pull origin main  # Update submodules
```

---

## Maintenance

```bash
git gc --aggressive                   # Optimize repo
git fsck                              # Check repo integrity
git maintenance run                   # Run maintenance tasks
```

---

## Collaboration

**Feature Branch**:
```bash
git switch -c feat/payment
# Work, commit, then:
git push -u origin HEAD
# Open PR, rebase/squash, merge with --ff-only
```

**Hotfix**:
```bash
git switch -c hotfix/v2.0.1 v2.0.0
git commit -m "fix: patch crash"
git tag -a v2.0.1 -m "Hotfix"
git push origin v2.0.1
```

---

## Large Files (Git LFS)

```bash
git lfs install                       # Setup LFS
git lfs track "*.psd"                 # Track large files
git add .gitattributes                # Commit LFS settings
```

---

## Ignore Rules

```gitignore
dist/
node_modules/
*.log
!keep.log
```

**Global Ignore**:
```bash
git config --global core.excludesFile ~/.config/git/ignore
```

---

## Aliases

```bash
git config --global alias.st "status -sb"
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.rs "restore"
```

---

## Quick Tasks

- **Start project**: `git init && git add . && git commit -m "Initial commit"`
- **New feature**: `git switch -c feat/x && git push -u origin HEAD`
- **Update branch**: `git fetch && git rebase origin/main`
- **Diff file between tags**: `git diff v1.0 v1.1 -- file.txt`
- **Undo staged file**: `git restore --staged file.txt`

---
