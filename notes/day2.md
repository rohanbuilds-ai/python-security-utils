# Day 2 — Python Data Structures + Git

## Overview
Day 2 focuses on fundamental Python data structures (lists and dictionaries), functions with parameters and return values, and Git basics for version control. These concepts form the foundation for organizing data and writing reusable, collaborative code.

---

## Part 1: Python Data Structures

### Lists
Lists are ordered, mutable collections of items. They allow you to store multiple values and access them by index (position).

#### Creating and Accessing Lists
```python
# Create a list
students = ["Hermione", "Harry", "Ron"]

# Access elements by index (0-indexed)
print(students[0])  # Output: Hermione
print(students[1])  # Output: Harry
print(students[2])  # Output: Ron
```

#### Iterating Over Lists
```python
# Simple iteration
for student in students:
    print(student)

# Iteration with index
for i in range(len(students)):
    print(i + 1, students[i])  # Prints position and name
```

#### Key List Concepts
- **0-indexed**: First element is at index 0, not 1
- **Mutable**: Can be modified after creation (add, remove, change elements)
- **len()**: Returns the number of elements in a list
- **range()**: Generates a sequence of numbers; `range(3)` produces 0, 1, 2

---

### Dictionaries
Dictionaries are unordered collections of key-value pairs. Unlike lists that use numeric indexes, dictionaries use keys (usually strings) to associate with values.

#### Creating and Accessing Dictionaries
```python
# Create a dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Access values by key
print(students["Hermione"])  # Output: Gryffindor
```

#### Iterating Over Dictionaries
```python
# Iterate through keys
for student in students:
    print(student)  # Prints keys only

# Iterate through keys and values
for student in students:
    print(student, students[student], sep=", ")
```

#### Lists of Dictionaries
You can combine lists and dictionaries for more complex data structures:

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# Access and iterate
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```

#### Key Dictionary Concepts
- **Keys must be immutable**: Typically strings, numbers, or tuples
- **Values can be any type**: Strings, integers, lists, other dictionaries, None, etc.
- **None**: Special Python value representing "no value" or "missing data"
- **Unordered**: While modern Python (3.7+) preserves insertion order, dictionaries are conceptually unordered

---

## Part 2: Functions

Functions allow you to write reusable blocks of code that perform specific tasks. They improve code organization and reduce repetition.

### Function Definition and Calling
```python
# Define a function
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Hermione")  # Output: Hello, Hermione!
```

### Parameters and Arguments
- **Parameters**: Variables defined in the function definition (e.g., `name` in `greet(name)`)
- **Arguments**: Actual values passed when calling the function (e.g., `"Hermione"` in `greet("Hermione")`)

### Return Values
Functions can return values back to the caller using the `return` statement:

```python
def square(n):
    return n * n

result = square(4)
print(result)  # Output: 16
```

#### Multiple Return Values
Python allows returning multiple values as a tuple:

```python
def get_values():
    x = 10
    y = 20
    return x, y

a, b = get_values()
print(a)  # Output: 10
print(b)  # Output: 20
```

#### Early Returns
The `return` statement immediately exits the function:

```python
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # Returns immediately when condition is met
```

### Practical Example: Decomposing Code with Functions
```python
def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
```

### Key Function Concepts
- **DRY Principle**: Don't Repeat Yourself — functions help eliminate redundancy
- **Abstraction**: Functions hide implementation details, making code clearer
- **Reusability**: Write once, use many times
- **Decomposition**: Break complex problems into smaller, manageable functions

---

## Part 3: Control Flow with Loops

### While Loops
Execute code repeatedly as long as a condition is true:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

### For Loops
Iterate through a sequence of items:

```python
# Using range()
for i in range(3):
    print("meow")

# Using a list
for student in students:
    print(student)

# Using underscore when variable isn't needed
for _ in range(3):
    print("meow")
```

### Loop Control Keywords
- **break**: Exit the loop immediately
- **continue**: Skip to the next iteration

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break  # Exit loop
    else:
        continue  # Skip to next iteration (optional here)
```

---

## Part 4: Git Basics

Git is a version control system that tracks changes to your code and enables collaboration.

### Core Concepts
- **Repository**: A folder containing your project and its version history
- **Commit**: A saved snapshot of your code at a specific point in time
- **Branch**: A separate line of development (main branch is the default)
- **Remote**: A version of your repository hosted on a server (like GitHub)

### Essential Git Commands

#### Clone
Downloads a repository from GitHub to your local computer:
```bash
git clone https://github.com/username/repository.git
```
Creates a local copy that connects to the remote repository.

#### Add
Stages files for commit (tells Git which changes to save):
```bash
git add filename.py        # Add specific file
git add .                  # Add all changes
```

#### Commit
Saves a snapshot of your staged changes with a descriptive message:
```bash
git commit -m "Add list sorting functionality"
```
Good commit messages:
- Describe **what** changed and **why**
- Use imperative mood: "Add feature" not "Added feature"
- Keep messages concise but informative

#### Push
Uploads your local commits to GitHub:
```bash
git push
```
Makes your changes available to collaborators and creates a backup.

#### Pull
Downloads changes from GitHub to your local computer:
```bash
git pull
```
Use before pushing to ensure you have the latest code.

#### Status
Checks the current state of your repository:
```bash
git status
```
Shows:
- Modified files
- Staged files
- Untracked files

### GitHub Workflow Example

1. **Clone** a repository:
   ```bash
   git clone https://github.com/username/hello-world.git
   cd hello-world
   ```

2. **Create a branch** for your changes (optional but recommended):
   ```bash
   git branch feature-name
   git checkout feature-name
   ```

3. **Make changes** to your files

4. **Check status**:
   ```bash
   git status
   ```

5. **Stage changes**:
   ```bash
   git add .
   ```

6. **Commit changes**:
   ```bash
   git commit -m "Descriptive commit message"
   ```

7. **Push to GitHub**:
   ```bash
   git push origin feature-name
   ```

8. **Create a Pull Request** on GitHub to merge changes into main

### Key Git Concepts
- **Commits preserve history**: Every commit is saved, allowing you to revert if needed
- **Collaborative workflow**: Multiple people can work on the same project
- **Branching**: Experiment without affecting the main codebase
- **Merge conflicts**: Occur when multiple people edit the same lines; must be resolved manually

---

## Summary of Key Takeaways

### Data Structures
| Concept | Use Case |
|---------|----------|
| **Lists** | Ordered collections; access by position; use when order matters |
| **Dictionaries** | Key-value associations; access by meaningful keys; use for structured data |
| **Lists of Dicts** | Complex data with multiple fields per item (common in real-world data) |

### Functions
- Write once, use many times (DRY principle)
- Accept parameters and return values
- Enable code decomposition and abstraction
- Essential for scalable, maintainable code

### Version Control (Git)
- **Track changes**: Know who changed what and when
- **Collaborate**: Multiple developers working simultaneously
- **Backup**: Code hosted remotely
- **Workflow**: Clone → Modify → Commit → Push → Pull Request

---