# Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to read and maintain.

## 1. Defining a Function

Use the `def` keyword to define a function:

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

## 2. Parameters and Arguments

Functions can accept input values:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

## 3. Return Statement

Functions can return values using `return`:

```python
def square(x):
    return x ** 2

result = square(4)
print(result)  # Output: 16
```

### Returning Multiple Values

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(minimum, maximum)  # Output: 1 9
```

## 4. Default Parameters

Provide default values for parameters:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Output: Hello, Alice!
greet("Bob", "Hi")          # Output: Hi, Bob!
greet("Charlie", "Welcome") # Output: Welcome, Charlie!
```

## 5. Keyword Arguments

Call functions using parameter names for clarity:

```python
def create_profile(name, age, city):
    print(f"{name}, {age} years old, from {city}")

# Positional arguments
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(age=30, city="LA", name="Bob")
```

## 6. *args and **kwargs

### *args - Variable Positional Arguments

Accept any number of positional arguments:

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2))           # Output: 3
print(add_all(1, 2, 3, 4, 5))  # Output: 15
```

### **kwargs - Variable Keyword Arguments

Accept any number of keyword arguments:

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Combining All Parameter Types

```python
def example(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

example(1, 2, 3, 4, 5, x=10, y=20)
# Output:
# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}
```

## 7. Lambda Functions

Lambda functions are small, anonymous functions defined in a single line. They're useful for short, throwaway functions.

### Basic Syntax

```python
lambda arguments: expression
```

- `lambda` - keyword to define the function
- `arguments` - input parameters (can be zero or more)
- `expression` - single expression that gets returned (no `return` keyword needed)

### Comparing Regular vs Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # Output: 25
```

### Examples with Different Arguments

```python
# No arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# Single argument
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Multiple arguments
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8

# Default arguments
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))       # Output: Hello, Alice!
print(greet("Bob", "Hi"))   # Output: Hi, Bob!
```

### With sorted() - Custom Sorting

```python
# Sort list of tuples by second element
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort descending
sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_desc)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Sort strings by length
words = ["apple", "pie", "banana", "kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['pie', 'kiwi', 'apple', 'banana']

# Sort dictionaries by a key
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

### With map() - Transform Each Element

`map()` applies a function to every item in an iterable:

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Add 10 to each number
plus_ten = list(map(lambda x: x + 10, numbers))
print(plus_ten)  # [11, 12, 13, 14, 15]

# Map with multiple lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [11, 22, 33]
```

### With filter() - Keep Elements That Match

`filter()` keeps only elements where the function returns `True`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Keep numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # [6, 7, 8, 9, 10]

# Filter strings by length
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)  # ['banana', 'cherry', 'elderberry']
```

### With reduce() - Combine All Elements

`reduce()` applies a function cumulatively to reduce a list to a single value:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers: ((((1+2)+3)+4)+5)
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Multiply all numbers: ((((1*2)*3)*4)*5)
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

### Combining map, filter, and lambda

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16, 36, 64, 100]

# Equivalent using list comprehension (often more readable)
result = [x ** 2 for x in numbers if x % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]
```

### Lambda with Conditional Expressions

```python
# If-else in lambda
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  # Even
print(check(7))  # Odd

# Grade calculator
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade(95))  # A
print(grade(82))  # B
print(grade(65))  # F
```

### Limitations of Lambda

1. **Single expression only** - can't have multiple statements
2. **No assignments** - can't use `=` inside lambda
3. **No loops** - can't use `for` or `while`
4. **Less readable** - for complex logic, use regular functions

```python
# This WON'T work:
# lambda x: x = x + 1              # No assignment allowed
# lambda x: for i in range(x): print(i)  # No loops

# Use regular function instead for complex logic
def complex_operation(x):
    result = x * 2
    result += 10
    return result
```

### When to Use Lambda vs Regular Functions

| Use Lambda | Use Regular Function |
|------------|---------------------|
| Short, simple operations | Complex logic |
| As arguments to `sorted()`, `map()`, `filter()` | Functions you'll reuse |
| One-time use | When you need multiple statements |
| When a name isn't needed | When readability matters |

## 8. Docstrings

Document your functions:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
```

## 9. Scope

### Local vs Global Variables

```python
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)   # Can access global
    print(local_var)    # Can access local

my_function()
print(global_var)       # Works
# print(local_var)      # Error! Not accessible
```

### Modifying Global Variables

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Output: 1
```

## 10. Nested Functions

Functions defined inside other functions:

```python
def outer():
    def inner():
        print("Inside inner function")
    
    print("Inside outer function")
    inner()

outer()
# Output:
# Inside outer function
# Inside inner function
```

## 11. Recursion

Functions that call themselves:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
```

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # Output: 13
```

## 12. Higher-Order Functions

Functions that take or return other functions:

```python
def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

result = apply_operation(double, 5)
print(result)  # Output: 10
```

## Summary Table

| Concept | Description |
|---------|-------------|
| `def` | Define a function |
| `return` | Return a value from function |
| Default params | `def func(a, b=10)` |
| `*args` | Variable positional arguments |
| `**kwargs` | Variable keyword arguments |
| `lambda` | Anonymous single-expression function |
| Docstring | Document function with `"""..."""` |
| `global` | Access/modify global variable |
| Recursion | Function calls itself |

## Best Practices

- Use descriptive function names (`calculate_total` not `ct`)
- Keep functions small and focused on one task
- Always add docstrings for complex functions
- Use default parameters for optional values
- Avoid modifying global variables when possible
- Use type hints for better code clarity (Python 3.5+)

```python
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b
```
