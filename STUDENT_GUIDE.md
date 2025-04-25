# Git Tutorial for Beginners

This guide will walk you through the process of using Git for version control, step by step.

## Setup Instructions

### 1. Install Git

#### Windows
1. Download Git from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer and follow the instructions
3. Open Git Bash to verify installation: `git --version`

#### macOS
1. Install via Homebrew: `brew install git`
   - If you don't have Homebrew, install it from [brew.sh](https://brew.sh/)
2. Or download from [git-scm.com](https://git-scm.com/download/mac)
3. Open Terminal to verify installation: `git --version`

#### Linux
1. Use your package manager:
   - Ubuntu/Debian: `sudo apt-get install git`
   - Fedora: `sudo dnf install git`
2. Verify installation: `git --version`

### 2. Configure Git

Run these commands in your terminal or Git Bash:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Create a GitHub Account

1. Go to [github.com](https://github.com) and sign up
2. Verify your email address

## Project Workflow

### 1. Clone This Repository

```bash
git clone <repository-url>
cd git-learning-repository
```

### 2. Create Your Own Repository

1. Go to GitHub and click the "+" icon in the top right
2. Select "New repository"
3. Name your repository (e.g., "my-first-git-project")
4. Make it public or private
5. Do NOT initialize with README, .gitignore, or license
6. Click "Create repository"
7. You'll see instructions on GitHub - we'll use them in the next steps

### 3. Initialize Your Local Project

```bash
# Create and navigate to a new project folder
mkdir my-first-git-project
cd my-first-git-project

# Initialize git
git init
```

### 4. Create Your First File

Create a file called `README.md` with some content:

```bash
# Windows
echo # My First Git Project > README.md

# macOS/Linux
echo "# My First Git Project" > README.md
```

### 5. Make Your First Commit

```bash
# Check what files are ready to be committed
git status

# Add the README file to staging
git add README.md

# Check status again
git status

# Commit the changes
git commit -m "Initial commit with README"
```

### 6. Connect to GitHub and Push

```bash
# Connect your local repository to your GitHub repository
git remote add origin https://github.com/yourusername/my-first-git-project.git

# Push your code to GitHub
git push -u origin main
```

Note: If your default branch is called "master" instead of "main", use:
```bash
git push -u origin master
```

### 7. Make More Changes

1. Edit your `README.md` to add more information using markdown formatting
2. Stage the changes: `git add README.md`
3. Commit: `git commit -m "Update README with project details"`
4. Push to GitHub: `git push`

### 8. View Your Commit History

```bash
git log
```

### 9. Create and Use Branches

```bash
# Create a new branch
git branch feature-branch

# Switch to the new branch
git checkout feature-branch

# Or do both in one command
git checkout -b another-feature

# Make changes, add and commit them
echo "# New Feature" > feature.md
git add feature.md
git commit -m "Add feature documentation"

# Push the branch to GitHub
git push -u origin feature-branch
```

### 10. Merge Your Changes

```bash
# Switch back to main branch
git checkout main

# Merge your feature branch
git merge feature-branch

# Push the merged changes
git push
```

## Documenting Your Project

For your Arduino project, create the following files:

1. **README.md**: Explain what your project does and how to use it
2. **HARDWARE.md**: List all the components needed
3. **CODE.md**: Explain how your code works with code snippets

## Using Markdown for Documentation

Markdown is a simple formatting syntax that makes your documentation look good. Check the `templates/MARKDOWN_GUIDE.md` file for examples of how to:

- Create headings
- Format text (bold, italic)
- Create lists
- Add code blocks with syntax highlighting
- Create tables
- Add images

## Getting Help

- Use `git --help` for general help
- Use `git <command> --help` for help with a specific command
- Refer to the resources in the main README.md

## Common Issues

### Authentication Failed
- Make sure you're using the correct GitHub username and password
- Consider setting up SSH keys or using a personal access token

### Branch Already Exists
- Use `git branch -D <branch-name>` to delete an existing branch before creating a new one

### Merge Conflicts
1. Open the files with conflicts
2. Look for the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Edit the files to resolve conflicts
4. Save the files
5. `git add <resolved-files>`
6. `git commit -m "Resolve merge conflicts"` 