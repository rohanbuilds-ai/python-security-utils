# Day 3 — Linux + Bash

## Overview
Day 3 focuses on fundamental Linux skills and Bash scripting. You'll learn essential command-line commands for navigating the filesystem, managing files, understanding permissions, and writing basic Bash scripts. These skills form the foundation for system administration and DevOps work.

---

## Part 1: Linux Basics

### The Linux Filesystem

Linux uses a hierarchical filesystem starting from the root directory `/`. Key directories include:

- `/home` - User home directories
- `/tmp` - Temporary files
- `/etc` - System configuration files
- `/var` - Variable data (logs, caches)
- `/usr` - User programs and libraries
- `/bin` - Essential system binaries
- `/root` - Root user's home directory

---

## Part 2: Essential Linux Commands

### Navigating the Filesystem

#### pwd (Print Working Directory)
Shows the current directory path:
```bash
pwd
# Output: /home/username/Documents
```

#### ls (List Directory Contents)
Lists files and directories in the current or specified directory:

```bash
ls                    # List files in current directory
ls -l                 # List with detailed information (permissions, size, date)
ls -a                 # Include hidden files (starting with .)
ls -la                # Combined: detailed view with hidden files
ls -F                 # Show file types (/ for directories, * for executables)
ls /path/to/dir       # List specific directory
```

#### cd (Change Directory)
Navigates between directories:

```bash
cd /home/user/Documents    # Change to absolute path
cd Desktop                 # Change to relative path
cd ..                      # Go to parent directory
cd -                       # Go to previous directory
cd ~                       # Go to home directory
cd                         # Go to home directory (shortcut)
```

---

### File Operations

#### touch (Create File)
Creates an empty file or updates file modification time:

```bash
touch filename.txt          # Create empty file
touch file1 file2 file3     # Create multiple files
```

#### mkdir (Make Directory)
Creates new directories:

```bash
mkdir mydir                 # Create single directory
mkdir -p path/to/nested/dir # Create nested directories with parent directories
mkdir -m 755 restricted     # Create with specific permissions
```

#### cp (Copy Files/Directories)
Copies files or directories:

```bash
cp source.txt destination.txt           # Copy file
cp -r source_dir dest_dir               # Copy directory recursively
cp file.txt /home/user/Documents        # Copy to specific directory
```

#### mv (Move or Rename)
Moves or renames files and directories:

```bash
mv oldname.txt newname.txt              # Rename file
mv file.txt /home/user/Documents        # Move to directory
mv /source/file /destination            # Move with full paths
```

#### rm (Remove Files)
Deletes files and directories:

```bash
rm file.txt                  # Delete file
rm -r directory              # Delete directory and contents recursively
rm -f file.txt               # Force delete (no confirmation)
rm *.txt                     # Delete all .txt files
```

#### rmdir (Remove Empty Directory)
Removes empty directories only:

```bash
rmdir empty_directory        # Remove empty directory
rmdir -p path/to/nested      # Remove nested empty directories
```

#### cat (Concatenate/Display Files)
Displays file contents:

```bash
cat filename.txt             # Display file contents
cat file1.txt file2.txt      # Display multiple files
```

---

## Part 3: File Permissions

Linux file permissions determine who can read, write, and execute files. Understanding permissions is crucial for system security.

### Permission Notation

File permissions are displayed as 10 characters, for example: `-rwxr-xr--`

Breaking it down:
- **1st character**: File type (`-` = regular file, `d` = directory, `l` = symbolic link)
- **Characters 2-4**: Owner permissions (`rwx`)
- **Characters 5-7**: Group permissions (`rwx`)
- **Characters 8-10**: Other permissions (`rwx`)

### Permission Types

| Permission | Symbol | Octal | Meaning |
|-----------|--------|-------|---------|
| Read | r | 4 | View file contents or list directory |
| Write | w | 2 | Modify file or create/delete in directory |
| Execute | x | 1 | Run file as program or access directory |

### Reading Permission Strings

Example: `-rw-r--r--`
- **`-`**: Regular file
- **`rw-`**: Owner can read and write, cannot execute (6)
- **`r--`**: Group can only read (4)
- **`r--`**: Others can only read (4)
- **Octal form**: `644`

### chmod (Change Permissions)

#### Octal Method
```bash
chmod 755 script.sh      # rwxr-xr-x (owner full, group/others execute+read)
chmod 644 document.txt   # rw-r--r-- (owner read+write, group/others read only)
chmod 700 private.sh     # rwx------ (owner only access)
chmod 777 file.txt       # rwxrwxrwx (everyone full access - DANGEROUS!)
```

#### Symbolic Method
```bash
chmod u+x script.sh      # Add execute for user (owner)
chmod g+w file.txt       # Add write for group
chmod o-r file.txt       # Remove read for others
chmod a+r file.txt       # Add read for all
chmod u=rwx,g=rx,o= file.txt  # Set specific permissions
```

**Symbolic shortcuts:**
- `u` = user (owner)
- `g` = group
- `o` = others
- `a` = all
- `+` = add permission
- `-` = remove permission
- `=` = set exact permission

### chown (Change Ownership)
Changes the owner of a file:

```bash
sudo chown newuser filename.txt              # Change owner
sudo chown newuser:newgroup filename.txt    # Change owner and group
sudo chown -R newuser directory             # Recursive change
```

### chgrp (Change Group)
Changes the group ownership:

```bash
chgrp newgroup filename.txt     # Change group
chgrp -R newgroup directory     # Recursive change
```

### umask (Default Permissions)
Sets default permissions for newly created files and directories:

```bash
umask                   # Display current umask
umask 022              # Set umask (files get 644, directories get 755)
```

**How umask works:**
- Files: `666 - umask = default file permissions`
- Directories: `777 - umask = default directory permissions`
- `umask 022`: files get `666 - 022 = 644`, directories get `777 - 022 = 755`

---

## Part 4: Bash Scripting Basics

Bash scripts are text files containing commands that the shell executes. They automate repetitive tasks and make system administration easier.

### Creating Your First Bash Script

#### Step 1: Create a File
```bash
touch myscript.sh
```

#### Step 2: Add the Shebang
The shebang (`#!`) tells the system which interpreter to use:

```bash
#!/bin/bash
```

This must be the first line of the script.

#### Step 3: Write Commands
```bash
#!/bin/bash
echo "Hello, World!"
```

#### Step 4: Make it Executable
```bash
chmod +x myscript.sh
```

#### Step 5: Run the Script
```bash
./myscript.sh
# Output: Hello, World!
```

### Variables

Variables store data that can be used throughout the script:

```bash
#!/bin/bash
name="Alice"
age=25
echo "My name is $name and I am $age years old"

# Output: My name is Alice and I am 25 years old
```

**Variable rules:**
- No spaces around `=`
- Access variables with `$variable_name` or `${variable_name}`
- Use quotes for strings with spaces

### Input: read Command

Get input from the user:

```bash
#!/bin/bash
echo "What is your name?"
read name
echo "Nice to meet you, $name!"
```

```bash
# Or with prompt
read -p "Enter your name: " name
echo "Hello, $name!"
```

### Conditionals: if, elif, else

Execute code based on conditions:

```bash
#!/bin/bash
read -p "Enter a number: " num

if [[ $num -gt 10 ]]; then
    echo "Number is greater than 10"
elif [[ $num -eq 10 ]]; then
    echo "Number equals 10"
else
    echo "Number is less than 10"
fi
```

**Comparison operators:**
| Operator | Meaning |
|----------|---------|
| `-gt` | Greater than |
| `-lt` | Less than |
| `-ge` | Greater than or equal to |
| `-le` | Less than or equal to |
| `-eq` | Equal to |
| `-ne` | Not equal to |

**String comparisons:**
```bash
if [[ "$name" == "Alice" ]]; then
    echo "Hello Alice!"
fi

if [[ -z "$name" ]]; then      # Check if empty
    echo "Name is empty"
fi

if [[ -n "$name" ]]; then      # Check if not empty
    echo "Name is: $name"
fi
```

### Loops

#### For Loop

Iterate over a list of items:

```bash
#!/bin/bash
for i in 1 2 3 4 5; do
    echo "Iteration $i"
done
```

**Range syntax:**
```bash
for i in {1..5}; do
    echo "Number: $i"
done

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
```

**C-style for loop:**
```bash
for ((i=1; i<=5; i++)); do
    echo "Number: $i"
done
```

**Iterating over arrays:**
```bash
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done
```

**Iterating over command output:**
```bash
for file in $(ls *.txt); do
    echo "Found: $file"
done
```

#### While Loop

Execute while a condition is true:

```bash
#!/bin/bash
i=1
while [[ $i -le 5 ]]; do
    echo "Number: $i"
    ((i++))  # Increment i
done
```

**Read file line by line:**
```bash
while IFS= read -r line; do
    echo "Line: $line"
done < filename.txt
```

### Functions

Reusable blocks of code:

```bash
#!/bin/bash

# Define function
greet() {
    echo "Hello, $1!"
}

# Call function
greet "Alice"
greet "Bob"
```

**Functions with return values:**
```bash
add() {
    local result=$(($1 + $2))
    echo $result  # Return via echo
}

sum=$(add 5 3)
echo "Sum is: $sum"
```

**Local variables:**
```bash
myfunction() {
    local var="local value"
    global_var="global value"
}
```

### Arrays

Store multiple values:

```bash
#!/bin/bash

# Define array
fruits=("apple" "banana" "cherry")

# Access elements
echo ${fruits[0]}        # apple
echo ${fruits[1]}        # banana

# All elements
echo ${fruits[@]}        # apple banana cherry

# Array length
echo ${#fruits[@]}       # 3

# Add to array
fruits+=("date")

# Iterate
for fruit in "${fruits[@]}"; do
    echo $fruit
done
```

---

## Part 5: Practical Bash Script Examples

### Example 1: File Backup Script

```bash
#!/bin/bash
# Simple backup script

SOURCE_DIR="/home/user/documents"
BACKUP_DIR="/home/user/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

if [[ ! -d "$BACKUP_DIR" ]]; then
    mkdir -p "$BACKUP_DIR"
fi

cp -r "$SOURCE_DIR" "$BACKUP_DIR/backup_$TIMESTAMP"
echo "Backup completed: $BACKUP_DIR/backup_$TIMESTAMP"
```

### Example 2: File Processing Script

```bash
#!/bin/bash
# Process all text files in a directory

directory=${1:-.}  # Default to current directory

if [[ ! -d "$directory" ]]; then
    echo "Error: Directory does not exist"
    exit 1
fi

for file in "$directory"/*.txt; do
    if [[ -f "$file" ]]; then
        lines=$(wc -l < "$file")
        echo "$file has $lines lines"
    fi
done
```

### Example 3: User Input Validation

```bash
#!/bin/bash
# Validate user age

read -p "Enter your age: " age

if ! [[ "$age" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number"
    exit 1
fi

if [[ $age -lt 18 ]]; then
    echo "You are a minor"
elif [[ $age -lt 65 ]]; then
    echo "You are an adult"
else
    echo "You are a senior"
fi
```

---

## Part 6: Running Bash Scripts

### Three Ways to Execute

```bash
# 1. Make executable and run directly
chmod +x script.sh
./script.sh

# 2. Explicitly use bash
bash script.sh

# 3. Source the script (runs in current shell)
source script.sh
```

### Debugging Scripts

```bash
# Verbose mode (print commands as executed)
bash -x script.sh

# Or add to script
set -x  # Enable debug mode
set +x  # Disable debug mode
```

---

## Common Linux Commands Reference

| Command | Purpose |
|---------|---------|
| `pwd` | Print working directory |
| `ls` | List directory contents |
| `cd` | Change directory |
| `mkdir` | Create directory |
| `touch` | Create file |
| `cp` | Copy file/directory |
| `mv` | Move/rename file |
| `rm` | Delete file |
| `rmdir` | Delete empty directory |
| `chmod` | Change permissions |
| `chown` | Change owner |
| `grep` | Search text patterns |
| `find` | Find files |
| `cat` | Display file contents |
| `echo` | Print text |

---

## Key Concepts Summary

### Linux Permissions
- Represented as 9 characters (3 sets of 3): owner, group, others
- Octal notation: read=4, write=2, execute=1
- Use `chmod` to change, `umask` to set defaults
- Always use minimal necessary permissions (principle of least privilege)

### Bash Scripting
- Start with `#!/bin/bash` shebang
- Variables store data (use `$variable` to access)
- Conditionals (`if/elif/else`) control flow
- Loops (`for/while`) repeat commands
- Functions organize reusable code
- Always make scripts executable with `chmod +x`

### File System Navigation
- Use relative paths (faster) for nearby directories
- Use absolute paths (starting with `/`) for clarity
- `..` goes to parent, `.` is current, `~` is home
- Tab completion speeds up typing

---

## Common Pitfalls to Avoid

- **Missing shebang**: Always start scripts with `#!/bin/bash`
- **Forgetting `chmod +x`**: Script won't run without execute permission
- **Spaces around `=`**: Variable assignment fails with spaces (`name = value` is wrong)
- **Unquoted variables**: Use `"$variable"` to handle spaces safely
- **Too permissive permissions**: Avoid `chmod 777` unless absolutely necessary
- **Forgetting `./`**: Must use `./script.sh` to run scripts in current directory

---

## Quick Reference: Permission Numbers

| Permission | Octal | Meaning |
|-----------|-------|---------|
| `rwx------` | 700 | Owner only (private scripts) |
| `rwxr-xr-x` | 755 | Owner can do anything, others can read/execute (common for scripts) |
| `rw-r--r--` | 644 | Owner can read/write, others read only (files) |
| `rwxrwxrwx` | 777 | Everyone can do anything (AVOID!) |
| `rw-------` | 600 | Owner read/write only (sensitive files) |

