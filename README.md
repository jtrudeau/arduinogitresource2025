# Git Learning Repository for Arduino Projects

This repository is designed to help you learn and practice Git fundamentals while working with Arduino projects. As a student, you'll clone this repository, create your own, and document your projects according to the specifications.

## Getting Started

### Prerequisites
- Git installed on your computer
- A GitHub account
- Arduino IDE installed (https://www.arduino.cc/en/software)
- Basic understanding of Arduino programming

### Step 1: Clone this repository
```bash
git clone https://github.com/jtrudeau/arduinogitresource2025.git
cd arduinogitresource2025
```

### Step 2: Create your own repository
1. Go to GitHub and create a new repository
2. Initialize your project:
```bash
# Navigate to your project folder
mkdir my-arduino-project
cd my-arduino-project

# Initialize git
git init

# Add your files
# Create some sample Arduino files for your project

# Stage your changes
git add .

# Commit your changes
git commit -m "Initial commit"

# Link to your GitHub repository
git remote add origin <your-repository-url>

# Push to GitHub
git push -u origin main
```

## Basic Git Commands

### Checking Status
```bash
git status
```

### Adding Files
```bash
git add <filename>  # Add specific file
git add .           # Add all files
```

### Committing Changes
```bash
git commit -m "Your commit message"
```

### Viewing History
```bash
git log
```

### Creating & Switching Branches
```bash
git branch <branch-name>     # Create branch
git checkout <branch-name>   # Switch to branch
git checkout -b <branch-name> # Create and switch in one command
```

### Merging Branches
```bash
git checkout main    # Switch to main branch
git merge <branch-name> # Merge the branch into main
```

## Documentation Guidelines

When documenting your Arduino projects, please follow these guidelines:

1. Create a clear README.md file with:
   - Project description
   - Components list
   - Wiring instructions
   - Code explanation
   - Usage instructions

2. Include comments in your Arduino code to explain:
   - What each part does
   - Pin connections
   - Any special functions

3. Use descriptive commit messages that explain what changed and why

## Sample Project

Check out the sample Arduino Data Logger project in the `templates/sample_project` directory. This example demonstrates:

1. Proper documentation structure
2. Arduino code organization
3. Change tracking with Git
4. Data analysis approach

## Templates and References

The `templates` directory contains helpful examples:
- Sample project structure
- README template
- Markdown syntax guide

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Arduino Reference](https://www.arduino.cc/reference/en/)
- [Dawson College Virtual Lab for Arduino Interns](https://englab.dawsoncollege.qc.ca/interns/Intro.html) 