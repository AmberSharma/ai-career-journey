# Sets in Python

A set is an unordered, mutable collection of unique elements. Sets are useful for membership testing, removing duplicates, and mathematical set operations.

## 1. Creating Sets

```python
# Empty set (must use set(), not {})
empty_set = set()
# Note: {} creates an empty dictionary, not a set!

# Set with elements
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From a list (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_list)
print(unique_numbers)  # {1, 2, 3, 4}

# From a string (each character becomes an element)
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}

# Using set comprehension
squares = {x**2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}
```

## 2. Set Characteristics

```python
# Sets are unordered - no indexing
fruits = {"apple", "banana", "cherry"}
# print(fruits[0])  # TypeError: 'set' object is not subscriptable

# Sets contain only unique elements
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}

# Set elements must be immutable (hashable)
valid_set = {1, "hello", (1, 2, 3)}  # OK
# invalid_set = {1, [2, 3]}  # TypeError: unhashable type: 'list'
# invalid_set = {1, {"a": 1}}  # TypeError: unhashable type: 'dict'
```

## 3. Adding and Removing Elements

### Adding Elements

```python
fruits = {"apple", "banana"}

# add() - add single element
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

# Adding duplicate has no effect
fruits.add("apple")
print(fruits)  # {'apple', 'banana', 'cherry'}

# update() - add multiple elements
fruits.update(["date", "elderberry"])
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# update() with multiple iterables
fruits.update(["fig"], {"grape", "honeydew"})
print(fruits)
```

### Removing Elements

```python
fruits = {"apple", "banana", "cherry", "date", "elderberry"}

# remove() - remove element (raises KeyError if not found)
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry', 'date', 'elderberry'}
# fruits.remove("mango")  # KeyError: 'mango'

# discard() - remove element (no error if not found)
fruits.discard("cherry")
print(fruits)  # {'apple', 'date', 'elderberry'}
fruits.discard("mango")  # No error

# pop() - remove and return arbitrary element
element = fruits.pop()
print(f"Removed: {element}")
print(fruits)

# clear() - remove all elements
fruits.clear()
print(fruits)  # set()
```

## 4. Set Methods

| Method | Description | Example |
|--------|-------------|---------|
| `add(x)` | Add element | `set.add(5)` |
| `update(iter)` | Add multiple elements | `set.update([1,2,3])` |
| `remove(x)` | Remove element (error if missing) | `set.remove(5)` |
| `discard(x)` | Remove element (no error) | `set.discard(5)` |
| `pop()` | Remove and return arbitrary element | `set.pop()` |
| `clear()` | Remove all elements | `set.clear()` |
| `copy()` | Create shallow copy | `new = set.copy()` |

## 5. Set Operations

### Union (elements in either set)

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using union() method
result = a.union(b)
print(result)  # {1, 2, 3, 4, 5}

# Using | operator
result = a | b
print(result)  # {1, 2, 3, 4, 5}

# Multiple sets
c = {5, 6, 7}
result = a.union(b, c)
print(result)  # {1, 2, 3, 4, 5, 6, 7}
result = a | b | c
print(result)  # {1, 2, 3, 4, 5, 6, 7}
```

### Intersection (elements in both sets)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using intersection() method
result = a.intersection(b)
print(result)  # {3, 4}

# Using & operator
result = a & b
print(result)  # {3, 4}

# Multiple sets
c = {4, 5, 6, 7}
result = a.intersection(b, c)
print(result)  # {4}
result = a & b & c
print(result)  # {4}
```

### Difference (elements in first set but not second)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using difference() method
result = a.difference(b)
print(result)  # {1, 2}

# Using - operator
result = a - b
print(result)  # {1, 2}

# The order matters!
result = b - a
print(result)  # {5, 6}
```

### Symmetric Difference (elements in either set but not both)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Using symmetric_difference() method
result = a.symmetric_difference(b)
print(result)  # {1, 2, 5, 6}

# Using ^ operator
result = a ^ b
print(result)  # {1, 2, 5, 6}
```

### Set Operations Summary

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(f"A: {a}")
print(f"B: {b}")
print(f"Union (A | B): {a | b}")           # {1, 2, 3, 4}
print(f"Intersection (A & B): {a & b}")     # {2, 3}
print(f"Difference (A - B): {a - b}")       # {1}
print(f"Difference (B - A): {b - a}")       # {4}
print(f"Symmetric Difference (A ^ B): {a ^ b}")  # {1, 4}
```

## 6. Set Comparisons

### Subset and Superset

```python
a = {1, 2}
b = {1, 2, 3, 4}

# Subset - all elements of a are in b
print(a.issubset(b))  # True
print(a <= b)         # True
print(a < b)          # True (proper subset - not equal)

# Superset - b contains all elements of a
print(b.issuperset(a))  # True
print(b >= a)           # True
print(b > a)            # True (proper superset - not equal)

# Equal sets
c = {1, 2}
print(a <= c)  # True (subset, including equal)
print(a < c)   # False (not proper subset)
print(a == c)  # True
```

### Disjoint Sets

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

# isdisjoint() - no common elements
print(a.isdisjoint(b))  # True
print(a.isdisjoint(c))  # False (3 is common)
```

## 7. Membership Testing

```python
fruits = {"apple", "banana", "cherry"}

# Check if element exists
print("apple" in fruits)   # True
print("mango" in fruits)   # False
print("mango" not in fruits)  # True

# Membership testing is very fast in sets (O(1))
# Much faster than lists for large collections
```

## 8. Iterating Over Sets

```python
fruits = {"apple", "banana", "cherry"}

# Basic iteration
for fruit in fruits:
    print(fruit)

# Note: Order is not guaranteed!

# Convert to sorted list for ordered iteration
for fruit in sorted(fruits):
    print(fruit)

# Output:
# apple
# banana
# cherry
```

## 9. Set Comprehensions

```python
# Basic syntax
# {expression for item in iterable}

# Create set of squares
squares = {x**2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# With condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {4, 16, 36, 64, 100}

# From string - unique characters
text = "hello world"
unique_chars = {char for char in text if char != " "}
print(unique_chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Process and transform
words = ["Apple", "BANANA", "cherry"]
lowercase_words = {word.lower() for word in words}
print(lowercase_words)  # {'apple', 'banana', 'cherry'}
```

## 10. Frozen Sets

Frozen sets are immutable versions of sets:

```python
# Create frozen set
frozen = frozenset([1, 2, 3])
print(frozen)  # frozenset({1, 2, 3})

# Frozen sets are immutable
# frozen.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'

# Can be used as dictionary keys or set elements
regular_set = {frozenset([1, 2]), frozenset([3, 4])}
print(regular_set)

# Can use set operations (returns new frozenset)
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a | b)  # frozenset({1, 2, 3, 4, 5})
print(a & b)  # frozenset({3})
```

## 11. Common Set Patterns

### Remove Duplicates from List

```python
# Remove duplicates (doesn't preserve order)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4] (order may vary)

# Preserve order (Python 3.7+)
unique_ordered = list(dict.fromkeys(numbers))
print(unique_ordered)  # [1, 2, 3, 4]
```

### Find Common Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = set(list1) & set(list2)
print(common)  # {4, 5}
print(list(common))  # [4, 5]
```

### Find Unique Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Elements only in list1
only_list1 = set(list1) - set(list2)
print(only_list1)  # {1, 2, 3}

# Elements in either but not both
unique_to_each = set(list1) ^ set(list2)
print(unique_to_each)  # {1, 2, 3, 6, 7, 8}
```

### Check for Any Common Elements

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

# Check if any common elements exist
has_common = not a.isdisjoint(b)
print(has_common)  # False

has_common = not a.isdisjoint(c)
print(has_common)  # True

# Alternative
has_common = bool(a & c)
print(has_common)  # True
```

### Validate Input

```python
# Check if all required fields are present
required_fields = {"name", "email", "password"}
user_input = {"name": "Alice", "email": "alice@example.com"}

missing = required_fields - set(user_input.keys())
if missing:
    print(f"Missing fields: {missing}")  # Missing fields: {'password'}
else:
    print("All fields present")
```

## 12. Performance Comparison

| Operation | Set | List |
|-----------|-----|------|
| Membership test (`in`) | O(1) | O(n) |
| Add element | O(1) | O(1)* |
| Remove element | O(1) | O(n) |
| Union | O(n+m) | O(n*m) |
| Intersection | O(min(n,m)) | O(n*m) |

*Amortized time

## Summary Table

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Create | `{1, 2, 3}` | Create a set |
| Create empty | `set()` | Create empty set |
| Add | `set.add(x)` | Add element |
| Update | `set.update(iter)` | Add multiple |
| Remove | `set.remove(x)` | Remove (error if missing) |
| Discard | `set.discard(x)` | Remove (no error) |
| Pop | `set.pop()` | Remove arbitrary |
| Length | `len(set)` | Number of elements |
| Union | `a \| b` | Elements in either |
| Intersection | `a & b` | Elements in both |
| Difference | `a - b` | Elements only in a |
| Symmetric Diff | `a ^ b` | Elements in either, not both |
| Subset | `a <= b` | Is a subset of b |
| Superset | `a >= b` | Is a superset of b |
| Check | `x in set` | Check membership |

## Best Practices

- Use sets when you need to store unique elements
- Use sets for fast membership testing (much faster than lists)
- Use frozensets when you need an immutable set (e.g., as dictionary keys)
- Use set operations for efficient comparisons between collections
- Remember that sets are unordered - don't rely on element order
- Set elements must be immutable (hashable) - no lists or dictionaries
- Use `discard()` instead of `remove()` to avoid KeyError
- Convert to set when you need to remove duplicates from a list
