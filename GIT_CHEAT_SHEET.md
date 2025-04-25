# Git Command Cheat Sheet

## Setup and Configuration

```bash
# Set username and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View configuration
git config --list
```

## Creating Repositories

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone <repository-url>
```

## Basic Workflow

```bash
# Check status of your files
git status

# Add files to staging area
git add <filename>      # Add specific file
git add .               # Add all files

# Commit changes
git commit -m "Commit message"

# View commit history
git log
git log --oneline       # Compact view
```

## Branching and Merging

```bash
# List branches
git branch

# Create a new branch
git branch <branch-name>

# Switch to a branch
git checkout <branch-name>

# Create and switch in one command
git checkout -b <branch-name>

# Merge a branch into current branch
git merge <branch-name>

# Delete a branch
git branch -d <branch-name>   # Safe delete
git branch -D <branch-name>   # Force delete
```

## Remote Repositories

```bash
# Add a remote
git remote add <name> <url>

# View remotes
git remote -v

# Push to a remote
git push <remote> <branch>
git push -u origin main    # First push with upstream

# Pull from a remote
git pull <remote> <branch>

# Fetch from a remote
git fetch <remote>
```

## Undoing Changes

```bash
# Discard changes in working directory
git restore <file>

# Unstage changes
git restore --staged <file>

# Amend last commit
git commit --amend

# Revert a commit
git revert <commit-hash>

# Reset to a previous state (CAUTION)
git reset --soft <commit-hash>   # Keep changes staged
git reset --mixed <commit-hash>  # Keep changes unstaged
git reset --hard <commit-hash>   # Discard changes
```

## Stashing

```bash
# Stash changes
git stash

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply specific stash
git stash apply stash@{n}

# Remove a stash
git stash drop stash@{n}

# Apply and remove stash
git stash pop
```

## Advanced

```bash
# Show changes
git diff
git diff --staged      # Staged changes

# Show specific commit
git show <commit-hash>

# Blame (see who changed each line)
git blame <file>

# Create a tag
git tag <tag-name>
git tag -a <tag-name> -m "Tag message"  # Annotated tag

# Push tags
git push --tags
``` 