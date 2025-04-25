# Git Practice Exercises

Complete these exercises to practice your Git skills. Each exercise builds on the previous ones.

## Exercise 1: Basic Workflow

1. Create a new file called `about_me.md`
   ```bash
   # Use your favorite text editor to create the file, or:
   echo "# About Me" > about_me.md
   ```

2. Add your name and one interesting fact about yourself using markdown formatting
   ```bash
   # Edit the file with your information
   nano about_me.md  # or use any text editor
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
   # Edit the file using any text editor
   nano about_me.md
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

## Exercise 3: Branching

This is most important for groups working on multiple features (e.g., separate code files for different sensors during your testing).

1. Create a new branch called `new-feature`
   ```bash
   git branch new-feature
   ```

2. Switch to the new branch
   ```bash
   git checkout new-feature
   ```
   
   Or do both in one command:
   ```bash
   git checkout -b new-feature
   ```

3. Create a file called `goals.md` with three learning goals as a bulleted list
   ```bash
   # Create and edit the file
   nano goals.md
   ```

4. Stage and commit the file
   ```bash
   git add goals.md
   git commit -m "Add learning goals file"
   ```

5. Push the branch to GitHub
   ```bash
   git push -u origin new-feature
   ```
   Note: `-u` sets up tracking for this branch

## Exercise 4: Merging

1. Switch back to the main branch
   ```bash
   git checkout main
   ```

2. Merge the `new-feature` branch
   ```bash
   git merge new-feature
   ```

3. Resolve any conflicts (if they occur)
   ```bash
   # If conflicts occur, edit the conflicted files
   # Then stage the resolved files
   git add <conflicted-files>
   git commit -m "Resolve merge conflicts"
   ```

4. Push to GitHub
   ```bash
   git push origin main
   ```

## Exercise 5: Collaboration (Group Exercise)

This is the most important for teams collaborating on a single project repository. When everything is completed each member of the team can have their own copy on github as a personal project.

1. Clone a classmate's repository
   ```bash
   git clone https://github.com/classmate-username/repository-name.git
   cd repository-name
   ```

2. Create a new branch with your name
   ```bash
   git checkout -b your-name
   ```

3. Add a file called `feedback.md` with positive feedback formatted with headings and lists
   ```bash
   # Create and edit the file
   nano feedback.md
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

## Exercise 6: Undo Changes

1. Make a change to a file that you want to undo
   ```bash
   # Edit a file
   nano about_me.md
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
   # Edit a file
   nano about_me.md
   
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

## Exercise 7: Git History

1. Use `git log` to view your commit history
   ```bash
   git log
   
   # Show compact history
   git log --oneline
   
   # Show with graph
   git log --oneline --graph
   ```

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
   ```bash
   # Create and edit the file
   nano history_exploration.md
   ```

5. Commit and push this file
   ```bash
   git add history_exploration.md
   git commit -m "Add Git history exploration notes"
   git push origin main
   ```

## Arduino Project Exercises

### Exercise A1: Version Control for Arduino Code

1. Create a new file called `blink.ino` with the basic Arduino Blink sketch
   ```bash
   # Create the file
   nano blink.ino
   ```

2. Create a `README.md` file describing what the sketch does
   ```bash
   # Create the file
   nano README.md
   ```

3. Stage and commit both files
   ```bash
   git add blink.ino README.md
   git commit -m "Add Blink sketch with documentation"
   ```

4. Modify the delay times and add comments
   ```bash
   # Edit the file
   nano blink.ino
   ```

5. Update the README.md to reflect the changes
   ```bash
   # Edit the file
   nano README.md
   ```

6. Commit these changes with a descriptive message
   ```bash
   git add blink.ino README.md
   git commit -m "Adjust blink timing and improve documentation"
   ```

7. Push to GitHub
   ```bash
   git push origin main
   ```

### Exercise A2: Feature Branching for Arduino

1. Create a branch called `ultrasonic-feature`
   ```bash
   git checkout -b ultrasonic-feature
   ```

2. Create a new file `ultrasonic.ino` with the code for an ultrasonic sensor
   ```bash
   # Create the file
   nano ultrasonic.ino
   ```

3. Add documentation in a markdown file called `ultrasonic.md`
   ```bash
   # Create the file
   nano ultrasonic.md
   ```

4. Commit these files
   ```bash
   git add ultrasonic.ino ultrasonic.md
   git commit -m "Add ultrasonic sensor functionality"
   ```

5. Switch back to main and create another branch called `led-feature`
   ```bash
   git checkout main
   git checkout -b led-feature
   ```

6. Add `led_control.ino` with code for controlling multiple LEDs
   ```bash
   # Create the file
   nano led_control.ino
   ```

7. Add documentation in a markdown file called `led_control.md`
   ```bash
   # Create the file
   nano led_control.md
   ```

8. Commit these files
   ```bash
   git add led_control.ino led_control.md
   git commit -m "Add LED control functionality"
   ```

9. Merge both feature branches into main (resolve any conflicts)
   ```bash
   git checkout main
   
   # First merge
   git merge ultrasonic-feature
   
   # Second merge (might have conflicts)
   git merge led-feature
   
   # If conflicts occur:
   # Edit conflicted files
   git add <conflicted-files>
   git commit -m "Resolve merge conflicts between features"
   ```

10. Push all branches to GitHub
    ```bash
    git push origin main
    git push origin ultrasonic-feature
    git push origin led-feature
    ```

### Exercise A3: Documentation Updates

1. Create a `HARDWARE.md` file listing all components needed for your Arduino project using markdown tables
   ```bash
   # Create the file
   nano HARDWARE.md
   ```

2. Create a `SETUP.md` file with setup instructions including images if possible
   ```bash
   # Create the file
   nano SETUP.md
   ```

3. Add both files to Git, commit with a message about improving documentation
   ```bash
   git add HARDWARE.md SETUP.md
   git commit -m "Add hardware list and setup instructions"
   ```

4. Push to GitHub
   ```bash
   git push origin main
   ```

### Exercise A4: Iterative Development

1. Start with the basic data logger code from the sample project
   ```bash
   # Copy the sample code
   cp templates/sample_project/datalogger.ino ./my_datalogger.ino
   ```

2. Create a branch called `optimization`
   ```bash
   git checkout -b optimization
   ```

3. Modify the code to take readings every 1 second instead of 0.5 seconds
   ```bash
   # Edit the file
   nano my_datalogger.ino
   
   # Change the delay(500); line to delay(1000);
   ```

4. Create or update documentation to reflect the change
   ```bash
   # Create or edit a documentation file
   nano datalogger_readme.md
   ```

5. Commit these changes
   ```bash
   git add my_datalogger.ino datalogger_readme.md
   git commit -m "Increase sampling interval to 1 second"
   ```

6. Make another improvement (your choice) and commit it
   ```bash
   # Edit the file
   nano my_datalogger.ino
   
   # Make your improvements
   git add my_datalogger.ino
   git commit -m "Add battery-saving optimization"
   ```

7. Merge back to main when satisfied with your optimizations
   ```bash
   git checkout main
   git merge optimization
   ```

8. Push all changes to GitHub
   ```bash
   git push origin main
   git push origin optimization
   ```

### Exercise A5: Data Analysis with Python

1. Create a branch called `data-analysis`
   ```bash
   git checkout -b data-analysis
   ```

2. Add a Python script called `analyze_data.py` that:
   - Reads data from a CSV file collected by your Arduino
   - Creates visualizations of the data
   - Calculates basic statistics
   ```bash
   # Create the file
   nano analyze_data.py
   
   # Or copy the example
   cp examples/analyze_data_example.py ./analyze_data.py
   ```

3. Add a `ANALYSIS.md` file documenting how to use the script and explaining the results
   ```bash
   # Create the file
   nano ANALYSIS.md
   
   # Or copy the example
   cp examples/ANALYSIS_example.md ./ANALYSIS.md
   ```

4. Commit both files
   ```bash
   git add analyze_data.py ANALYSIS.md
   git commit -m "Add data analysis tools and documentation"
   ```

5. Test with sample data and improve the script as needed
   ```bash
   # Create some test data if needed
   # Make improvements to the script
   nano analyze_data.py
   ```

6. Make additional commits with your improvements
   ```bash
   git add analyze_data.py
   git commit -m "Improve chart visualization"
   ```

7. Merge back to main when satisfied
   ```bash
   git checkout main
   git merge data-analysis
   ```

8. Push all changes to GitHub
   ```bash
   git push origin main
   git push origin data-analysis
   ```

## Submit Your Work

After completing these exercises, submit the URL to your GitHub repository. 