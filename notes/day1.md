# Day 1: Python Basics + Setup 🐍

**Topics:** Python Syntax, Variables, Loops, Conditions, Running Python Programs  
**Resources:** CS50P Lectures 0 & 1, Python Official Tutorial

---

## 1. Getting Started with Python

### What is Python?
- **Python** is a high-level, general-purpose programming language designed for clarity and simplicity
- Excellent for beginners and professionals alike
- No special software required—just a web browser or a text editor + Python interpreter

### Running Python
- **Interactive Mode:** Type `python` in terminal to access the interactive shell (>>>)
- **Script Mode:** Create `.py` files and run with `python filename.py`
- Useful for testing small code snippets quickly

---

## 2. Python as a Calculator

### Basic Arithmetic Operations
```python
# Addition, Subtraction, Multiplication
2 + 2       # Output: 4
50 - 5 * 6  # Output: 20 (respects operator precedence)
(50 - 5) * 6  # Output: 270

# Division & Operators
8 / 5       # Output: 1.6 (float division, always returns float)
8 // 3      # Output: 2 (integer division, floor division)
17 % 3      # Output: 2 (modulo - remainder)
5 ** 2      # Output: 25 (exponentiation/power)
```

### Key Points
- `/` always returns a **float**
- `//` performs integer (floor) division
- `%` returns the remainder
- `**` is the exponentiation operator
- Python respects standard operator precedence: `()` → `**` → `*/, //,%` → `+, -`

---

## 3. Variables and Data Types

### Variable Assignment
```python
width = 20
height = 5 * 9
area = width * height  # Output: 900

# Multiple assignment
a, b = 0, 1  # Assigns 0 to a, 1 to b simultaneously
```

### Key Points
- No special keywords needed to declare variables
- Variables store values in memory
- Assignment uses `=` (right-to-left: evaluate right side first, then assign)
- Undefined variables raise `NameError`

### Data Types

#### **Integers (int)**
```python
>>> type(42)
<class 'int'>
>>> 2 + 2
4
```

#### **Floats (float)**
- Any number with a decimal point
- Result of division `/` is always float
```python
>>> type(3.14)
<class 'float'>
>>> 8 / 5
1.6
```

#### **Strings (str)**
- Text enclosed in single `'...'` or double `"..."` quotes (no difference)
- **Immutable** (cannot be changed after creation)
```python
>>> 'spam eggs'
'spam eggs'
>>> "Hello, World!"
'Hello, World!'
>>> '1975'  # Numbers in quotes are strings
'1975'
```

### String Operations

**Concatenation (joining):**
```python
>>> 'Py' + 'thon'
'Python'
>>> 'un' * 3
'unununium'
```

**Escaping Characters:**
```python
>>> 'doesn\'t'  # Use \' to escape single quote
"doesn't"
>>> "doesn't"   # Or use double quotes
"doesn't"
>>> print('Line1\nLine2')  # \n is newline
Line1
Line2
```

**String Indexing (0-based):**
```python
word = 'Python'
>>> word[0]     # First character
'P'
>>> word[5]     # 6th character
'n'
>>> word[-1]    # Last character
'n'
>>> word[-2]    # Second to last
'o'
```

**String Slicing:**
```python
>>> word[0:2]   # Characters from index 0 to 1 (2 excluded)
'Py'
>>> word[2:5]   # Characters from index 2 to 4
'tho'
>>> word[:2]    # From start to index 1
'Py'
>>> word[4:]    # From index 4 to end
'on'
>>> word[-2:]   # Last 2 characters
'on'
```

**String Length:**
```python
>>> len('supercalifragilisticexpialidocious')
34
```

**Important:** Strings are immutable—you cannot change individual characters:
```python
>>> word[0] = 'J'
TypeError: 'str' object does not support item assignment
# Instead, create a new string:
>>> 'J' + word[1:]
'Jython'
```

---

## 4. Lists

### Creating and Accessing Lists
```python
squares = [1, 4, 9, 16, 25]

# Indexing (same as strings)
>>> squares[0]
1
>>> squares[-1]
25

# Slicing (same as strings)
>>> squares[-3:]
[9, 16, 25]
```

### Key Differences from Strings
- Lists are **mutable**—elements can be changed
- Lists can contain different data types

```python
cubes = [1, 8, 27, 64, 125]
>>> cubes[3] = 64  # Can reassign elements
>>> cubes.append(216)  # Add element to end
>>> cubes
[1, 8, 27, 64, 125, 216]
```

### List Operations
```python
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> len([1, 2, 3])
3
```

### Nested Lists
```python
x = [['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

---

## 5. Control Flow: Conditionals

### Comparison Operators
```
<   # Less than
>   # Greater than
==  # Equal to
<=  # Less than or equal to
>=  # Greater than or equal to
!=  # Not equal to
```

### Boolean Values
- `True` and `False` (capitalized)
- In conditions: non-zero numbers are `True`, zero is `False`
- Empty sequences are `False`, non-empty sequences are `True`

### if Statements
```python
# Basic if
if x > 0:
    print("x is positive")

# if-else
if x > 0:
    print("positive")
else:
    print("not positive")

# if-elif-else
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

### Key Points
- **Indentation** is critical in Python (use 4 spaces or 1 tab, be consistent)
- Colon `:` required at end of condition line
- Indented block executes only if condition is True

---

## 6. Control Flow: Loops

### while Loop
```python
# Count from 0 to 9
i = 0
while i < 10:
    print(i)
    i += 1
```

**Example: Fibonacci Sequence**
```python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b  # Multiple assignment in loop
# Output: 0, 1, 1, 2, 3, 5, 8
```

### for Loop
```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

**Iterating through sequences:**
```python
for num in [1, 2, 3]:
    print(num)

word = "Python"
for letter in word:
    print(letter)
```

### Loop Keywords
- **break** — Exit the loop immediately
- **continue** — Skip to next iteration

```python
while True:
    if condition:
        break  # Exit loop
    if skip_this:
        continue  # Skip to next iteration
```

### range() Function
```python
range(5)        # 0, 1, 2, 3, 4
range(2, 5)     # 2, 3, 4
range(0, 10, 2) # 0, 2, 4, 6, 8 (step of 2)
```

---

## 7. Comments and Syntax

### Comments
```python
# This is a single-line comment
x = 5  # Comment at end of line

# Comments start with # and go to end of line
# They are ignored by Python interpreter
```

### Indentation
- **Critical in Python** — defines code blocks
- Use 4 spaces (or 1 tab consistently)
- Must align properly for if/loops/functions to work

```python
if x > 0:          # No indent needed for condition
    print("pos")   # Indent required for body
    print("yes")   # Must align with line above
print("done")      # Back to no indent (outside if)
```

---

## 8. Useful Built-in Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `print()` | Display output | `print("Hello")` |
| `len()` | Get length | `len([1,2,3])` → 3 |
| `type()` | Check data type | `type(42)` → `<class 'int'>` |
| `int()` | Convert to integer | `int("42")` → 42 |
| `str()` | Convert to string | `str(42)` → "42" |
| `float()` | Convert to float | `float("3.14")` → 3.14 |
| `range()` | Generate sequence | `range(5)` → 0,1,2,3,4 |
| `input()` | Get user input | `input("Enter: ")` |
| `round()` | Round number | `round(3.7)` → 4 |

---

## 9. Working with User Input

```python
# Get input as string
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Convert to integer
age = int(input("Enter age: "))
print(f"Next year you'll be {age + 1}")

# Handle input conversion
try:
    num = int(input("Enter a number: "))
except:
    print("That's not a number!")
```

---

## 10. Key Takeaways

✅ Python is beginner-friendly with clean, readable syntax  
✅ Variables store data; assign with `=`  
✅ Main data types: `int`, `float`, `str`, `list`  
✅ **Strings are immutable; Lists are mutable**  
✅ Conditionals (`if/else`) control program flow  
✅ Loops (`while/for`) repeat code blocks  
✅ **Indentation is essential** in Python  
✅ Use `#` for comments  
