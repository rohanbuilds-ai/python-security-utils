# Day 3 Notes — Git Workflows & Basic Automation

## What I Worked On
- Learned Git branching and safe workflows
- Practiced working with feature branches
- Merged changes back into the main branch
- Created a simple automation script to run tests
- Continued documenting progress consistently

## Concepts Learned

### Git Branching
- A branch is an isolated line of development
- Open-source work should never be done directly on `main`
- Feature branches help keep changes safe and reviewable
- Branches are deleted after merging to keep history clean

### Git Workflow
- Create a feature branch for every change
- Make small, focused commits
- Merge back into `main` only after changes are verified
- Clean up branches after merge

### Automation Basics
- Repetitive commands can be automated using scripts
- Automation reduces human error and saves time
- Even simple scripts are valuable in real projects

## Practical Work Done
- Created and switched to a feature branch
- Made a small documentation improvement
- Committed changes on the feature branch
- Merged the branch back into `main`
- Deleted the feature branch after merge
- Added a script to run tests automatically

## Commands Practiced
- `git checkout -b <branch-name>`
- `git status`
- `git add`
- `git commit`
- `git merge`
- `git branch -d`
- `python -m pytest`

## Challenges Faced
- Remembering the correct order of Git commands
- Understanding when to merge vs when to keep a branch

## Key Takeaways
- Clean Git workflows are critical for open-source contributions
- Small, isolated changes are safer than large commits
- Automation improves productivity even at a small scale

## Next Steps
- Read and understand larger codebases
- Learn how to reproduce and fix issues safely
- Begin interacting more deeply with open-source issues
