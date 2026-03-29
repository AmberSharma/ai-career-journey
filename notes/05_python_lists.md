# Lists in Python

A list is an ordered, mutable collection that can hold items of different types. Lists are one of the most commonly used data structures in Python.

## 1. Creating Lists

```python
# Empty list
empty_list = []
empty_list = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## 2. Accessing Elements

### Indexing

Lists are zero-indexed (first element is at index 0):

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])   # apple (first element)
print(fruits[1])   # banana (second element)
print(fruits[-1])  # elderberry (last element)
print(fruits[-2])  # date (second to last)
```

### Slicing

Extract a portion of the list with `[start:end:step]`:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] (index 2 to 4)
print(numbers[:4])     # [0, 1, 2, 3] (start to index 3)
print(numbers[6:])     # [6, 7, 8, 9] (index 6 to end)
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
print(numbers[1:8:2])  # [1, 3, 5, 7] (index 1 to 7, step 2)
```

## 3. Modifying Lists

### Changing Elements

```python
fruits = ["apple", "banana", "cherry"]

# Change single element
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Change multiple elements
fruits[0:2] = ["apricot", "blackberry"]
print(fruits)  # ['apricot', 'blackberry', 'cherry']
```

### Adding Elements

```python
fruits = ["apple", "banana"]

# append() - add to end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert() - add at specific index
fruits.insert(1, "apricot")
print(fruits)  # ['apple', 'apricot', 'banana', 'cherry']

# extend() - add multiple elements
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry']

# Using + operator
more_fruits = fruits + ["fig", "grape"]
print(more_fruits)
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - remove first occurrence of value
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana', 'date']

# pop() - remove and return element at index (default: last)
last = fruits.pop()
print(last)    # date
print(fruits)  # ['apple', 'cherry', 'banana']

first = fruits.pop(0)
print(first)   # apple
print(fruits)  # ['cherry', 'banana']

# del - delete element or slice
del fruits[0]
print(fruits)  # ['banana']

# clear() - remove all elements
fruits.clear()
print(fruits)  # []
```

## 4. List Methods

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Add element to end | `list.append(5)` |
| `insert(i, x)` | Insert at index | `list.insert(0, 5)` |
| `extend(iter)` | Add multiple elements | `list.extend([1,2,3])` |
| `remove(x)` | Remove first occurrence | `list.remove(5)` |
| `pop(i)` | Remove and return at index | `list.pop(0)` |
| `clear()` | Remove all elements | `list.clear()` |
| `index(x)` | Find index of element | `list.index(5)` |
| `count(x)` | Count occurrences | `list.count(5)` |
| `sort()` | Sort in place | `list.sort()` |
| `reverse()` | Reverse in place | `list.reverse()` |
| `copy()` | Create shallow copy | `new = list.copy()` |

### Examples

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# index() - find position of element
print(numbers.index(5))  # 4 (first occurrence)

# count() - count occurrences
print(numbers.count(5))  # 2

# sort() - sort in place
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# sort descending
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]

# reverse() - reverse in place
numbers.reverse()
print(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# copy() - create a copy
numbers_copy = numbers.copy()
```

## 5. List Operations

### Length, Min, Max, Sum

```python
numbers = [5, 2, 8, 1, 9, 3]

print(len(numbers))  # 6
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 28
```

### Membership Testing

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # True
print("grape" in fruits)       # False
print("grape" not in fruits)   # True
```

### Concatenation and Repetition

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## 6. Iterating Over Lists

### Basic Loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### With Index (enumerate)

```python
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

### Iterating Multiple Lists (zip)

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

## 7. List Comprehensions

A concise way to create lists:

```python
# Basic syntax
# [expression for item in iterable]

# Create list of squares
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## 8. Sorting Lists

### sort() vs sorted()

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - modifies original list
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() - returns new list, original unchanged
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)         # [3, 1, 4, 1, 5, 9, 2, 6] (unchanged)
```

### Custom Sorting with key

```python
words = ["banana", "pie", "apple", "cherry"]

# Sort by length
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # ['pie', 'apple', 'banana', 'cherry']

# Sort by last character
sorted_by_last = sorted(words, key=lambda x: x[-1])
print(sorted_by_last)  # ['banana', 'pie', 'apple', 'cherry']

# Sort list of tuples
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_score)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

## 9. Nested Lists (2D Lists)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0])      # [1, 2, 3] (first row)
print(matrix[0][1])   # 2 (first row, second column)
print(matrix[2][2])   # 9 (third row, third column)

# Iterate through 2D list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# Flatten a 2D list
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 10. Copying Lists

### Shallow Copy vs Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy - nested objects are still references
shallow = original.copy()
shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - original affected!

# Deep copy - completely independent copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - original unchanged
```

### Ways to Copy

```python
original = [1, 2, 3]

# Method 1: copy()
copy1 = original.copy()

# Method 2: list()
copy2 = list(original)

# Method 3: slicing
copy3 = original[:]

# Method 4: list comprehension
copy4 = [x for x in original]
```

## 11. Common List Patterns

### Finding Elements

```python
numbers = [10, 20, 30, 40, 50]

# Check if element exists
if 30 in numbers:
    print("Found!")

# Find index (with error handling)
try:
    index = numbers.index(30)
    print(f"Found at index {index}")
except ValueError:
    print("Not found")

# Find all indices of a value
numbers = [1, 2, 3, 2, 4, 2, 5]
indices = [i for i, x in enumerate(numbers) if x == 2]
print(indices)  # [1, 3, 5]
```

### Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Using set (doesn't preserve order)
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4]

# Preserving order (Python 3.7+)
unique_ordered = list(dict.fromkeys(numbers))
print(unique_ordered)  # [1, 2, 3, 4]
```

### Filtering Lists

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

### Transforming Lists

```python
numbers = [1, 2, 3, 4, 5]

# Using list comprehension
squares = [x ** 2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Using map()
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]
```

## Summary Table

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Create | `[1, 2, 3]` | Create a list |
| Access | `list[0]` | Get element by index |
| Slice | `list[1:3]` | Get a portion |
| Add | `list.append(x)` | Add to end |
| Insert | `list.insert(i, x)` | Add at index |
| Remove | `list.remove(x)` | Remove by value |
| Pop | `list.pop(i)` | Remove by index |
| Length | `len(list)` | Get number of elements |
| Sort | `list.sort()` | Sort in place |
| Reverse | `list.reverse()` | Reverse in place |
| Copy | `list.copy()` | Create shallow copy |
| Check | `x in list` | Check membership |

## Best Practices

- Use list comprehensions for simple transformations
- Use `append()` for single elements, `extend()` for multiple
- Use `enumerate()` when you need both index and value
- Use `sorted()` when you need to keep the original list unchanged
- Be careful with shallow copies when dealing with nested lists
- Use meaningful variable names (e.g., `students` not `s`)
