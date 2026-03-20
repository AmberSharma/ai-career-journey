# Input/Output in Python

Input/Output (I/O) operations allow your program to interact with users and external data sources like files.

## Console I/O

### 1. Output with `print()`

The `print()` function displays output to the console:

```python
# Basic printing
print("Hello, World!")

# Printing variables
name = "Alice"
print(name)

# Printing multiple values
print("Name:", name, "Age:", 25)

# Print with separator
print("a", "b", "c", sep="-")    # Output: a-b-c

# Print without newline
print("Hello", end=" ")
print("World")                   # Output: Hello World
```

### 2. Formatted Output

```python
name = "Alice"
age = 25
score = 95.5

# f-strings (Python 3.6+) - Recommended
print(f"Name: {name}, Age: {age}")
print(f"Score: {score:.2f}")     # 2 decimal places

# .format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))

# % formatting (older style)
print("Name: %s, Age: %d" % (name, age))
print("Score: %.2f" % score)
```

### 3. Input with `input()`

The `input()` function reads user input as a string:

```python
# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Converting input types
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Multiple inputs on one line
x, y = input("Enter two numbers: ").split()
x, y = int(x), int(y)

# Or using map
a, b = map(int, input("Enter two numbers: ").split())
```

## File I/O

### 4. Opening Files

```python
# Syntax: open(filename, mode)
# Modes:
#   'r'  - Read (default)
#   'w'  - Write (overwrites existing)
#   'a'  - Append
#   'x'  - Create (fails if exists)
#   'b'  - Binary mode
#   't'  - Text mode (default)
#   'r+' - Read and write

file = open("example.txt", "r")
# ... do something
file.close()
```

### 5. Using `with` Statement (Recommended)

The `with` statement automatically closes the file:

```python
# Reading a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line")
```

### 6. Reading Files

```python
# Read entire file
with open("example.txt", "r") as file:
    content = file.read()

# Read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()

# Read single line
with open("example.txt", "r") as file:
    first_line = file.readline()
```

### 7. Writing Files

```python
# Write (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

# Write multiple lines
lines = ["First\n", "Second\n", "Third\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append to file
with open("output.txt", "a") as file:
    file.write("New line appended\n")
```

### 8. Working with CSV Files

```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row is a list

# Writing CSV
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
```

### 9. Working with JSON Files

```python
import json

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Writing JSON
data = {"name": "Alice", "age": 25}
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# Converting to/from JSON strings
json_string = json.dumps(data)
data = json.loads(json_string)
```

## Error Handling in I/O

### 10. Handling Exceptions

```python
# Handle file not found
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# Handle invalid input
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid number!")

# Multiple exceptions
try:
    with open("data.txt", "r") as file:
        number = int(file.read())
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Invalid data in file!")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Best Practices

- Always use `with` statement for file operations
- Handle exceptions for user input and file operations
- Use f-strings for formatted output (Python 3.6+)
- Close files explicitly if not using `with`
- Validate user input before processing
- Use appropriate file modes to prevent data loss
