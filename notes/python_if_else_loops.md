# If-Else and Loops in Python

Control flow statements allow you to control the order in which code is executed based on conditions and repetition.

## If-Else Statements

If-else statements execute code conditionally based on whether a condition is true or false.

### 1. Basic Syntax

```python
if condition:
    # code if condition is True
elif another_condition:
    # code if another_condition is True
else:
    # code if all conditions are False
```

### 2. Example

```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

### 3. Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### 4. Logical Operators

```python
x = 10

# and - both conditions must be True
if x > 5 and x < 15:
    print("x is between 5 and 15")

# or - at least one condition must be True
if x < 5 or x > 8:
    print("x is outside 5-8 range")

# not - inverts the condition
if not x == 5:
    print("x is not 5")
```

### 5. Ternary Operator (Conditional Expression)

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

## Loops

Loops allow you to repeat code multiple times.

### 1. For Loop

Iterates over a sequence (list, tuple, string, range, etc.):

```python
# Iterate over a list
for item in [1, 2, 3]:
    print(item)

# Iterate over a string
for char in "hello":
    print(char)

# Using range
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):    # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i)
```

### 2. While Loop

Repeats as long as a condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 3. Loop Control Statements

| Statement | Description |
|-----------|-------------|
| `break` | Exit the loop immediately |
| `continue` | Skip to the next iteration |
| `pass` | Do nothing (placeholder) |

```python
for i in range(10):
    if i == 3:
        continue    # skip 3
    if i == 7:
        break       # stop at 7
    print(i)        # prints 0, 1, 2, 4, 5, 6
```

### 4. Else with Loops

Python uniquely allows `else` after loops—it runs if the loop completes without `break`:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")
```

### 5. Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

### 6. Enumerate

`enumerate()` adds a counter to an iterable, returning pairs of (index, value). This is useful when you need both the position and the item while looping.

```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate (manual index tracking)
index = 0
for fruit in fruits:
    print(f"{index}: {fruit}")
    index += 1

# With enumerate (cleaner)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**Output:**
```
0: apple
1: banana
2: cherry
```

#### Custom Start Index

```python
# Start counting from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

**Output:**
```
1: apple
2: banana
3: cherry
```

#### Practical Example

```python
# Find the index of a specific item
names = ["Alice", "Bob", "Charlie", "Bob"]

for index, name in enumerate(names):
    if name == "Bob":
        print(f"Found Bob at index {index}")

# Output:
# Found Bob at index 1
# Found Bob at index 3
```

### 7. Zip

`zip()` combines multiple iterables element-by-element, creating pairs (or tuples) of corresponding items. It stops when the shortest iterable is exhausted.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

**Output:**
```
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

#### Zipping More Than Two Lists

```python
names = ["Alice", "Bob"]
ages = [25, 30]
cities = ["NYC", "LA"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")
```

#### Unequal Length Lists

```python
# zip stops at the shortest list
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

for x, y in zip(a, b):
    print(x, y)

# Output: only 3 pairs
# 1 a
# 2 b
# 3 c
```

#### Creating Dictionaries with Zip

```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]

person = dict(zip(keys, values))
print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

#### Unzipping (Reverse of Zip)

```python
pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

names, ages = zip(*pairs)  # * unpacks the list

print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)   # (25, 30, 35)
```

### 8. List Comprehensions

List comprehensions provide a concise way to create lists. They can replace multi-line `for` loops with a single readable line.

#### Basic Syntax

```python
[expression for item in iterable]
```

#### Basic Example

```python
# Traditional loop
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension (same result)
squares = [x ** 2 for x in range(5)]

print(squares)  # [0, 1, 4, 9, 16]
```

#### With Condition (Filtering)

```python
[expression for item in iterable if condition]
```

```python
# Only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Squares of even numbers only
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

#### With If-Else (Conditional Expression)

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

```python
numbers = [1, 2, 3, 4, 5]

labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']
```

#### Nested List Comprehensions

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a 2D list (multiplication table)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

#### Practical Examples

```python
# Convert strings to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Extract first letter of each word
first_letters = [word[0] for word in words]
print(first_letters)  # ['h', 'w', 'p']

# Filter and transform
names = ["Alice", "Bob", "Charlie", "David"]
long_names_upper = [name.upper() for name in names if len(name) > 4]
print(long_names_upper)  # ['ALICE', 'CHARLIE', 'DAVID']
```

### 9. Dictionary and Set Comprehensions

The same concept applies to dictionaries and sets:

```python
# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}
```

## Summary Table

| Feature | Use Case |
|---------|----------|
| `enumerate()` | Need index + value while looping |
| `zip()` | Iterate over multiple lists in parallel |
| List Comprehension | Create lists with concise syntax |
| Dict Comprehension | Create dictionaries with concise syntax |
| Set Comprehension | Create sets with concise syntax |

## Best Practices

- Avoid infinite loops by ensuring the while condition eventually becomes False
- Use `for` loops when iterating over a known sequence
- Use `while` loops when the number of iterations is unknown
- Keep loop bodies simple and readable
- Use list comprehensions for simple transformations
- Use `enumerate()` instead of manual index tracking
- Use `zip()` to iterate over multiple lists together
