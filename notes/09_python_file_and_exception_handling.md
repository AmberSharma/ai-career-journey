# Python File Handling and Exception Handling

A comprehensive guide to working with files and handling errors in Python.

---

## Part 1: File Handling

### File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (default) - File must exist |
| `w` | Write - Creates new file or truncates existing |
| `a` | Append - Creates new file or appends to existing |
| `x` | Exclusive create - Fails if file exists |
| `b` | Binary mode (e.g., `rb`, `wb`) |
| `t` | Text mode (default) |
| `+` | Read and write (e.g., `r+`, `w+`) |

---

### 1.1 Basic File Operations

#### Writing to a File

```python
# Using 'with' statement (recommended - auto-closes file)
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")
```

#### Reading from a File

```python
# Method 1: Read entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Method 2: Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes trailing newline

# Method 3: Read all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # ['Hello, World!\n', 'This is line 2.\n', ...]

# Method 4: Read single line
with open('example.txt', 'r') as file:
    first_line = file.readline()
    second_line = file.readline()
```

---

### 1.2 Appending to Files

```python
with open('example.txt', 'a') as file:
    file.write("This line was appended!\n")
```

---

### 1.3 Working with File Positions

```python
with open('example.txt', 'r') as file:
    print(f"Starting position: {file.tell()}")  # 0
    
    file.read(5)  # Read 5 characters
    print(f"After reading 5 chars: {file.tell()}")  # 5
    
    file.seek(0)  # Go back to beginning
    print(f"After seek(0): {file.tell()}")  # 0
```

---

### 1.4 Binary File Operations

```python
# Writing binary data
with open('binary_example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')

# Reading binary data
with open('binary_example.bin', 'rb') as file:
    data = file.read()
    print(f"Binary data: {data}")
```

---

### 1.5 Working with Multiple Files

```python
# Copy content from one file to another
with open('example.txt', 'r') as source, open('copy.txt', 'w') as dest:
    dest.write(source.read())
```

---

### 1.6 Useful File Methods

| Method | Description |
|--------|-------------|
| `file.read(size)` | Read 'size' bytes/chars (all if not specified) |
| `file.readline()` | Read single line |
| `file.readlines()` | Read all lines into list |
| `file.write(string)` | Write string to file |
| `file.writelines()` | Write list of strings |
| `file.seek(offset)` | Move to position |
| `file.tell()` | Get current position |
| `file.close()` | Close file (automatic with 'with') |
| `file.flush()` | Flush write buffer |

---

## Part 2: Exception Handling

Exception handling allows you to gracefully handle errors and prevent crashes.

### Basic Syntax

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Handle the exception
else:
    # Runs if no exception occurred
finally:
    # Always runs (cleanup)
```

---

### 2.1 Basic Try-Except

```python
# Simple exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching the exception object
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
```

---

### 2.2 Multiple Except Blocks

```python
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Invalid types for division!")

divide_numbers(10, 0)      # ZeroDivisionError
divide_numbers("10", 2)    # TypeError
```

---

### 2.3 Catching Multiple Exceptions Together

```python
try:
    value = int("not a number")
except (ValueError, TypeError) as e:
    print(f"Caught exception: {type(e).__name__}: {e}")
```

---

### 2.4 Try-Except-Else-Finally

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("EXCEPT: Cannot divide by zero")
        return None
    else:
        print(f"ELSE: Division successful, result = {result}")
        return result
    finally:
        print("FINALLY: This always executes")

safe_divide(10, 2)
# ELSE: Division successful, result = 5.0
# FINALLY: This always executes

safe_divide(10, 0)
# EXCEPT: Cannot divide by zero
# FINALLY: This always executes
```

---

### 2.5 Raising Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Valid age: {age}"

try:
    print(validate_age(25))   # Valid age: 25
    print(validate_age(-5))   # Raises ValueError
except ValueError as e:
    print(f"Validation error: {e}")
```

---

### 2.6 Custom Exceptions

```python
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount}. Balance is only ${balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)  # Cannot withdraw $150. Balance is only $100
```

---

### 2.7 Exception Chaining

```python
def fetch_data():
    raise ConnectionError("Network unavailable")

def process_data():
    try:
        fetch_data()
    except ConnectionError as e:
        raise RuntimeError("Failed to process data") from e

try:
    process_data()
except RuntimeError as e:
    print(f"Error: {e}")              # Failed to process data
    print(f"Caused by: {e.__cause__}") # Network unavailable
```

---

### 2.8 Common Built-in Exceptions

| Exception | When It Occurs |
|-----------|----------------|
| `ValueError` | Wrong value (e.g., `int("abc")`) |
| `TypeError` | Wrong type (e.g., `"2" + 2`) |
| `KeyError` | Dict key not found |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Attribute doesn't exist |
| `ImportError` | Import fails |
| `NameError` | Variable not defined |
| `RuntimeError` | Generic runtime error |
| `StopIteration` | Iterator exhausted |
| `PermissionError` | Insufficient permissions |

---

### 2.9 Exception Handling with Files

```python
def read_file_safely(filename):
    """Demonstrates proper file handling with exceptions"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Permission denied for '{filename}'")
        return None
    except IOError as e:
        print(f"IO Error: {e}")
        return None

content = read_file_safely('example.txt')
read_file_safely('nonexistent.txt')  # File 'nonexistent.txt' not found
```

---

### 2.10 Context Managers for Resource Cleanup

```python
class FileManager:
    """Custom context manager for file operations"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False  # False propagates exceptions, True suppresses

# Using custom context manager
with FileManager('example.txt', 'r') as f:
    print(f.readline().strip())
```

---

## Part 3: Best Practices Summary

### File Handling Best Practices

1. Always use `with` statement for automatic cleanup
2. Handle specific exceptions (`FileNotFoundError`, `PermissionError`)
3. Use appropriate mode (`r`, `w`, `a`, `b`)
4. Close files properly (automatic with `with`)
5. Use encoding parameter for text files: `open(file, 'r', encoding='utf-8')`

### Exception Handling Best Practices

1. Catch specific exceptions, not bare `except:`
2. Don't silently ignore exceptions
3. Use `finally` for cleanup operations
4. Create custom exceptions for domain-specific errors
5. Include helpful error messages
6. Log exceptions in production code
7. Don't use exceptions for flow control
8. Re-raise exceptions when you can't handle them properly

### Anti-Patterns to Avoid

```python
# Bad: Bare except catches everything including KeyboardInterrupt
try:
    risky_operation()
except:  # Don't do this!
    pass

# Bad: Silently ignoring errors
try:
    risky_operation()
except Exception:
    pass  # At least log the error!

# Good: Specific exception with proper handling
try:
    risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise  # or handle appropriately
```
