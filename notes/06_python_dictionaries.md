# Dictionaries in Python

A dictionary is an unordered, mutable collection of key-value pairs. Dictionaries are optimized for retrieving values when you know the key.

## 1. Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with elements
person = {"name": "Alice", "age": 25, "city": "New York"}

# Using dict() constructor
person = dict(name="Alice", age=25, city="New York")

# From list of tuples
pairs = [("name", "Alice"), ("age", 25)]
person = dict(pairs)

# Using dict comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## 2. Accessing Values

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Using square brackets
print(person["name"])  # Alice

# Using get() - returns None if key doesn't exist (safer)
print(person.get("name"))       # Alice
print(person.get("country"))    # None
print(person.get("country", "USA"))  # USA (default value)

# Direct access raises KeyError if key doesn't exist
# print(person["country"])  # KeyError: 'country'
```

## 3. Modifying Dictionaries

### Adding and Updating Elements

```python
person = {"name": "Alice", "age": 25}

# Add new key-value pair
person["city"] = "New York"
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Update existing value
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}

# update() - add/update multiple key-value pairs
person.update({"country": "USA", "age": 27})
print(person)  # {'name': 'Alice', 'age': 27, 'city': 'New York', 'country': 'USA'}

# setdefault() - add key with default value if it doesn't exist
person.setdefault("email", "alice@example.com")
print(person["email"])  # alice@example.com

person.setdefault("name", "Bob")  # Won't change existing key
print(person["name"])  # Alice
```

### Removing Elements

```python
person = {"name": "Alice", "age": 25, "city": "New York", "country": "USA"}

# pop() - remove and return value
age = person.pop("age")
print(age)     # 25
print(person)  # {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

# pop() with default (no error if key doesn't exist)
result = person.pop("phone", "Not found")
print(result)  # Not found

# popitem() - remove and return last inserted key-value pair
item = person.popitem()
print(item)    # ('country', 'USA')
print(person)  # {'name': 'Alice', 'city': 'New York'}

# del - delete specific key
del person["city"]
print(person)  # {'name': 'Alice'}

# clear() - remove all elements
person.clear()
print(person)  # {}
```

## 4. Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `get(key, default)` | Get value or default | `dict.get("key", 0)` |
| `keys()` | Get all keys | `dict.keys()` |
| `values()` | Get all values | `dict.values()` |
| `items()` | Get all key-value pairs | `dict.items()` |
| `update(other)` | Update with another dict | `dict.update({"a": 1})` |
| `pop(key)` | Remove and return value | `dict.pop("key")` |
| `popitem()` | Remove and return last item | `dict.popitem()` |
| `setdefault(key, val)` | Set default if key missing | `dict.setdefault("k", 0)` |
| `clear()` | Remove all elements | `dict.clear()` |
| `copy()` | Create shallow copy | `new = dict.copy()` |

### Examples

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# keys() - get all keys
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(list(person.keys()))  # ['name', 'age', 'city']

# values() - get all values
print(person.values())  # dict_values(['Alice', 25, 'New York'])
print(list(person.values()))  # ['Alice', 25, 'New York']

# items() - get all key-value pairs
print(person.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# copy() - create a shallow copy
person_copy = person.copy()
```

## 5. Dictionary Operations

### Membership Testing

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Check if key exists
print("name" in person)      # True
print("country" in person)   # False
print("country" not in person)  # True

# Check if value exists
print("Alice" in person.values())  # True
```

### Length

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(len(person))  # 3
```

### Merging Dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update() - modifies dict1
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using ** unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## 6. Iterating Over Dictionaries

### Iterate Over Keys

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

for key in person:
    print(key)

# Output:
# name
# age
# city
```

### Iterate Over Values

```python
for value in person.values():
    print(value)

# Output:
# Alice
# 25
# New York
```

### Iterate Over Key-Value Pairs

```python
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25
# city: New York
```

## 7. Dictionary Comprehensions

```python
# Basic syntax
# {key_expr: value_expr for item in iterable}

# Create dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Filter dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
high_scores = {k: v for k, v in scores.items() if v >= 90}
print(high_scores)  # {'Bob': 92, 'Diana': 95}
```

## 8. Nested Dictionaries

```python
# Creating nested dictionaries
students = {
    "alice": {
        "age": 20,
        "grades": {"math": 90, "science": 85}
    },
    "bob": {
        "age": 22,
        "grades": {"math": 78, "science": 92}
    }
}

# Accessing nested values
print(students["alice"]["age"])  # 20
print(students["alice"]["grades"]["math"])  # 90

# Modifying nested values
students["alice"]["grades"]["math"] = 95
print(students["alice"]["grades"]["math"])  # 95

# Adding nested values
students["alice"]["grades"]["history"] = 88
print(students["alice"]["grades"])  # {'math': 95, 'science': 85, 'history': 88}

# Safe access with get()
grade = students.get("charlie", {}).get("grades", {}).get("math", "N/A")
print(grade)  # N/A
```

## 9. Common Dictionary Patterns

### Counting Elements

```python
# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Manual counting
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Using collections.Counter
from collections import Counter
word_count = Counter(words)
print(word_count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

### Grouping Elements

```python
# Group by first letter
words = ["apple", "banana", "apricot", "cherry", "blueberry"]

groups = {}
for word in words:
    first_letter = word[0]
    if first_letter not in groups:
        groups[first_letter] = []
    groups[first_letter].append(word)

print(groups)  # {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# Using setdefault()
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)

# Using collections.defaultdict
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
print(dict(groups))
```

### Default Values with defaultdict

```python
from collections import defaultdict

# defaultdict with int (default 0)
counts = defaultdict(int)
for char in "hello":
    counts[char] += 1
print(dict(counts))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# defaultdict with list (default empty list)
groups = defaultdict(list)
pairs = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
for category, item in pairs:
    groups[category].append(item)
print(dict(groups))  # {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}
```

### Finding Keys by Value

```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 92}

# Find key with maximum value
max_key = max(scores, key=scores.get)
print(max_key)  # Bob (or Diana)

# Find all keys with a specific value
keys_with_92 = [k for k, v in scores.items() if v == 92]
print(keys_with_92)  # ['Bob', 'Diana']
```

## 10. Dictionary vs Other Data Structures

| Feature | Dictionary | List | Set |
|---------|-----------|------|-----|
| Ordered | Yes (3.7+) | Yes | No |
| Mutable | Yes | Yes | Yes |
| Duplicates | Keys: No | Yes | No |
| Access | By key | By index | N/A |
| Use case | Key-value mapping | Ordered sequence | Unique elements |

## Summary Table

| Operation | Syntax | Description |
|-----------|--------|-------------|
| Create | `{"a": 1}` | Create a dictionary |
| Access | `dict["key"]` | Get value by key |
| Safe Access | `dict.get("key")` | Get value or None |
| Add/Update | `dict["key"] = val` | Set key-value pair |
| Remove | `dict.pop("key")` | Remove and return |
| Delete | `del dict["key"]` | Delete key |
| Length | `len(dict)` | Number of pairs |
| Keys | `dict.keys()` | Get all keys |
| Values | `dict.values()` | Get all values |
| Items | `dict.items()` | Get all pairs |
| Check | `"key" in dict` | Check if key exists |
| Merge | `dict1.update(dict2)` | Merge dictionaries |

## Best Practices

- Use `get()` instead of direct access to avoid KeyError exceptions
- Use meaningful key names that describe the data
- Use dictionary comprehensions for simple transformations
- Use `defaultdict` when you need automatic default values
- Use `Counter` for counting occurrences
- Be aware that dictionary keys must be immutable (strings, numbers, tuples)
- In Python 3.7+, dictionaries maintain insertion order
