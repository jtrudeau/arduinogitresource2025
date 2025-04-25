# Git Practice Exercises

Complete these exercises to practice your Git skills. Each exercise builds on the previous ones.

## Exercise 1: Basic Workflow

1. Create a new file called `about_me.md`
   ```bash
   # Open VS Code in the current directory
   code .
   
   # Create and edit the file in VS Code
   # Click "New File" and name it "about_me.md"
   ```

2. Add your name and one interesting fact about yourself using markdown formatting
   ```bash
   # In VS Code, add your information to about_me.md
   # Save the file with Ctrl+S (or Cmd+S on Mac)
   ```

3. Stage the file
   ```bash
   git add about_me.md
   ```

4. Commit with an appropriate message
   ```bash
   git commit -m "Add about_me file with personal information"
   ```

5. Push to GitHub
   ```bash
   git push origin main
   ```

## Exercise 2: Making Changes

1. Edit `about_me.md` to add the Arduino (C++) programming language with a heading and a code sample
   ```bash
   # Open the file in VS Code
   code about_me.md
   
   # Or if VS Code is already open, find and edit the file
   # Add a code block with Arduino example
   ```

2. Stage the changes
   ```bash
   git add about_me.md
   ```

3. Commit with a descriptive message
   ```bash
   git commit -m "Add Arduino code example to about_me"
   ```

4. Push to GitHub
   ```bash
   git push origin main
   ```

## Exercise 3: Branching and Merging

This exercise demonstrates how to use branches for developing features independently. This is important for working on multiple features at once or when collaborating with a team.

1. Create and switch to a new branch for your feature
   ```bash
   # Create and switch to a new branch in one command
   git checkout -b feature-branch
   ```

2. Create a file called `goals.md` with three learning goals as a bulleted list
   ```bash
   # Open VS Code to create the file
   code goals.md
   
   # Add your content and save
   ```

3. Stage and commit the file
   ```bash
   git add goals.md
   git commit -m "Add learning goals file"
   ```

4. Push the branch to GitHub
   ```bash
   git push -u origin feature-branch
   ```

5. Switch back to the main branch
   ```bash
   git checkout main
   ```

6. Merge your feature branch into main
   ```bash
   git merge feature-branch
   ```

7. Push the merged changes to GitHub
   ```bash
   git push origin main
   ```

## Exercise 4: Collaboration (Group Exercise)

This is important for teams collaborating on a single project repository. When everything is completed, each team member can have their own copy on GitHub as a personal project.

1. Clone a classmate's repository
   ```bash
   git clone https://github.com/classmate-username/repository-name.git
   cd repository-name
   
   # Open the project in VS Code
   code .
   ```

2. Create a new branch with your name
   ```bash
   git checkout -b your-name
   ```

3. Add a file called `feedback.md` with dummy feedback formatted with headings and lists
   ```bash
   # Create and edit the file in VS Code
   ```

4. Commit and push your branch
   ```bash
   git add feedback.md
   git commit -m "Add feedback from your-name"
   git push -u origin your-name
   ```

5. Create a Pull Request on GitHub
   ```
   # Go to the GitHub website and click on "Pull requests" > "New pull request"
   # Select the base branch (main) and your branch (your-name)
   # Click "Create pull request"
   ```

## Exercise 5: Undo Changes

1. Make a change to a file that you want to undo
   ```bash
   # Edit a file in VS Code
   code about_me.md
   ```

2. Use `git restore` to undo the change
   ```bash
   # Before staging:
   git restore about_me.md
   
   # If already staged:
   git restore --staged about_me.md
   git restore about_me.md
   ```

3. Make and commit a different change
   ```bash
   # Edit a file in VS Code
   code about_me.md
   
   # Stage and commit
   git add about_me.md
   git commit -m "Add different change to about_me"
   ```

4. Use `git revert` to undo the commit
   ```bash
   # Find the commit hash
   git log --oneline
   
   # Revert the commit
   git revert <commit-hash>
   ```

5. Push to GitHub
   ```bash
   git push origin main
   ```

## Exercise 6: Git History

1. Use `git log` to view your commit history
   ```bash
   git log 
  
2. Find a specific commit and copy its hash
   ```bash
   git log --oneline
   # Copy the hash (e.g., a1b2c3d)
   ```

3. Use `git show <commit-hash>` to see what changed
   ```bash
   git show a1b2c3d  # Replace with your commit hash
   ```

4. Create a file called `history_exploration.md` with your observations using markdown formatting


5. Commit and push this file
   ```bash
   git add history_exploration.md
   git commit -m "Add Git history exploration notes"
   git push origin main
   ```

## Arduino Project Exercises

### Exercise A1: Arduino Project Setup

1. Create a basic Arduino project structure
   ```bash
   # Create project folders
   mkdir -p arduino_project/src
   cd arduino_project
   
   # Open the project in VS Code
   code .
   ```

2. Create a basic Arduino sketch for blinking an LED
   ```bash
   # In VS Code, create a new file in the src folder named blink.ino
   # Add the standard blink sketch
   ```

3. Create a `README.md` file describing your project
   ```bash
   # In VS Code, create README.md in the root of your project
   ```

4. Initialize Git and make your first commit
   ```bash
   git init
   git add .
   git commit -m "Initial project setup with LED blink sketch"
   ```

5. Create a repository on GitHub and link your local repository
   ```bash
   # After creating the repository on GitHub, connect your local repo
   git remote add origin https://github.com/yourusername/arduino_project.git
   git push -u origin main
   ```

### Exercise A2: Working with Branches for Feature Development

1. Create a feature branch for adding an ultrasonic sensor to your project
   ```bash
   git checkout -b ultrasonic-feature
   ```

2. Add code and documentation for the ultrasonic sensor
   ```bash
   # In VS Code, create a file in the src folder called ultrasonic.ino
   # Also create a markdown file called ULTRASONIC.md with documentation
   ```

3. Commit your changes
   ```bash
   git add .
   git commit -m "Add ultrasonic sensor functionality"
   ```

4. Switch back to main and merge your feature
   ```bash
   git checkout main
   git merge ultrasonic-feature
   ```

5. Push all changes to GitHub
   ```bash
   git push origin main
   ```

### Exercise A3: Documenting Your Arduino Project

1. Create comprehensive documentation for your project
   ```bash
   # In VS Code, edit or create these files:
   README.md         # Main project documentation
   HARDWARE.md       # Hardware components list and specifications
   SETUP.md          # Setup and build instructions
   ```

2. Use markdown features effectively:
   - Include a table of pin connections
   - Add code blocks with Arduino syntax highlighting
   - Use lists and headings for clear organization
   - Add links to relevant resources

3. Commit your documentation
   ```bash
   git add *.md
   git commit -m "Add comprehensive project documentation"
   git push origin main
   ```

### Exercise A4: Data Logger Project

1. Create a data logger based on our example
   ```bash
   # Copy the sample files to your project
   cp -r ../templates/sample_project/datalogger.ino ./
   
   # Open the project in VS Code
   code .
   ```

2. Modify the data logger to suit your needs
   ```bash
   # Edit the data logger code in VS Code
   # For example, change the sampling rate or add new features
   ```

3. Document your changes
   ```bash
   # Create documentation in VS Code
   datalogger_doc.md
   ```

4. Commit and push your changes
   ```bash
   git add .
   git commit -m "Customize data logger for my project"
   git push origin main
   ```

### Exercise A5: Data Analysis with Python

1. Add a Python script for analyzing your Arduino data
   ```bash
   # Create a directory for your analysis code
   mkdir -p analysis
   
   # Create a Python script in VS Code
   code analysis/analyze_data.py
   
   # You can start with our example
   cp ../examples/analyze_data_example.py ./analysis/analyze_data.py
   ```

2. Create documentation for your analysis
   ```bash
   # In VS Code, create an analysis README
   code analysis/README.md
   ```

3. Test your analysis with sample data
   ```bash
   # Create or obtain sample data
   # Run your script to test it
   python analysis/analyze_data.py sample_data.csv
   ```

4. Commit and push your analysis code
   ```bash
   git add analysis
   git commit -m "Add data analysis tools"
   git push origin main
   ```

## Submit Your Work

After completing these exercises, submit the URL to your GitHub repository. 