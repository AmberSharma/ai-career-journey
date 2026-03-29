# Variables in Python

Variables in Python are names that refer to values stored in memory. They act as containers for data that you can use and manipulate throughout your program.

## Key Concepts

### 1. Variable Assignment
Python uses the `=` operator to assign values to variables:

```python
name = "Alice"
age = 25
price = 19.99
is_active = True
```

### 2. Dynamic Typing
Python is dynamically typed—you don't need to declare a variable's type. The type is determined automatically based on the assigned value:

```python
x = 10       # x is an integer
x = "hello"  # x is now a string (reassigned)
```

### 3. Naming Rules
- Must start with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- Case-sensitive (`name` and `Name` are different)
- Cannot use Python reserved keywords (`if`, `for`, `class`, etc.)

```python
# Valid
my_variable = 1
_private = 2
userName123 = 3

# Invalid
2fast = 10      # cannot start with number
my-var = 5      # hyphens not allowed
class = "test"  # reserved keyword
```

### 4. Common Data Types
```python
integer_var = 42           # int
float_var = 3.14           # float
string_var = "Hello"       # str
boolean_var = True         # bool
list_var = [1, 2, 3]       # list
dict_var = {"key": "val"}  # dict
none_var = None            # NoneType
```

### 5. Multiple Assignment
```python
# Assign same value to multiple variables
a = b = c = 0

# Assign multiple values at once
x, y, z = 1, 2, 3
```

### 6. Variable Scope
- **Local**: Defined inside a function, only accessible there
- **Global**: Defined outside functions, accessible everywhere

```python
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)   # Works
    print(local_var)    # Works

my_function()
print(global_var)       # Works
print(local_var)        # Error! Not accessible here
```

### 7. Best Practices
- Use descriptive names: `user_count` instead of `uc`
- Follow snake_case convention: `my_variable`
- Constants in UPPERCASE: `MAX_SIZE = 100`
- Avoid single letters except for loops: `for i in range(10)`
