# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming is a programming paradigm that organizes code into objects, which bundle data (attributes) and behavior (methods) together. Python is a multi-paradigm language that fully supports OOP.

## 1. Classes and Objects

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

### Creating a Class

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
```

### Creating Objects (Instances)

```python
# Create instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(dog1.name)      # Buddy
print(dog2.age)       # 5
print(dog1.species)   # Canis familiaris

# Call methods
print(dog1.bark())         # Buddy says woof!
print(dog2.description())  # Max is 5 years old
```

## 2. The `__init__` Method (Constructor)

The `__init__` method is called automatically when an object is created:

```python
class Person:
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email  # Optional parameter with default
        self.created_at = "2024"  # Attribute not from parameter
    
# Create with required parameters
person1 = Person("Alice", 25)
print(person1.email)  # None

# Create with all parameters
person2 = Person("Bob", 30, "bob@example.com")
print(person2.email)  # bob@example.com
```

## 3. Instance vs Class Attributes

```python
class Car:
    # Class attribute - shared by all instances
    wheels = 4
    all_cars = []
    
    def __init__(self, brand, model):
        # Instance attributes - unique to each instance
        self.brand = brand
        self.model = model
        Car.all_cars.append(self)  # Track all instances

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Class attributes are shared
print(car1.wheels)  # 4
print(car2.wheels)  # 4
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6

# Instance attributes are unique
print(car1.brand)  # Toyota
print(car2.brand)  # Honda

# Modifying instance attribute doesn't affect others
car1.brand = "Ford"
print(car1.brand)  # Ford
print(car2.brand)  # Honda
```

## 4. Methods

### Instance Methods

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # Instance method - has access to self
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(circle.area())  # 78.53975
```

### Class Methods

```python
class Employee:
    raise_amount = 1.05  # 5% raise
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    # Class method - has access to class, not instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # Class method as alternative constructor
    @classmethod
    def from_string(cls, emp_string):
        name, salary = emp_string.split("-")
        return cls(name, int(salary))

# Using class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)  # 1.10

# Alternative constructor
emp = Employee.from_string("Alice-50000")
print(emp.name)    # Alice
print(emp.salary)  # 50000
```

### Static Methods

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Static methods don't need an instance
print(MathUtils.add(5, 3))      # 8
print(MathUtils.is_even(4))     # True

# Can also call on instance
utils = MathUtils()
print(utils.add(2, 3))  # 5
```

### Method Types Comparison

| Method Type | Decorator | First Parameter | Access |
|-------------|-----------|-----------------|--------|
| Instance | None | `self` | Instance and class |
| Class | `@classmethod` | `cls` | Class only |
| Static | `@staticmethod` | None | No access to class/instance |

## 5. Encapsulation

Encapsulation is about bundling data and methods, and restricting direct access to some attributes.

### Public, Protected, and Private

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._account_type = "Savings"  # Protected (convention)
        self.__balance = balance    # Private (name mangling)
    
    # Getter for private attribute
    def get_balance(self):
        return self.__balance
    
    # Setter with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

account = BankAccount("Alice", 1000)

# Public - accessible
print(account.owner)  # Alice

# Protected - accessible but shouldn't be modified directly
print(account._account_type)  # Savings

# Private - not directly accessible
# print(account.__balance)  # AttributeError

# Access through methods
print(account.get_balance())  # 1000
account.deposit(500)
print(account.get_balance())  # 1500

# Private attributes are name-mangled (still accessible but discouraged)
print(account._BankAccount__balance)  # 1500
```

### Properties (Getters and Setters)

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.celsius = 30
print(temp.celsius)     # 30

temp.fahrenheit = 100
print(temp.celsius)     # 37.77...

# Validation works
# temp.celsius = -300  # ValueError
```

## 6. Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

### Basic Inheritance

```python
# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def eat(self):
        return f"{self.name} is eating"

# Child class (derived class)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    # Override parent method
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.name)     # Buddy
print(dog.breed)    # Golden Retriever
print(dog.speak())  # Buddy says Woof!
print(dog.eat())    # Buddy is eating (inherited)

print(cat.speak())  # Whiskers says Meow!
```

### Using `super()`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Initialize parent attributes
        self.student_id = student_id
    
    def introduce(self):
        # Extend parent method
        parent_intro = super().introduce()
        return f"{parent_intro}, Student ID: {self.student_id}"

student = Student("Alice", 20, "S12345")
print(student.introduce())
# I'm Alice, 20 years old, Student ID: S12345
```

### Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming fast!"

# Duck inherits from both
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # Flying high!
print(duck.swim())  # Swimming fast!
print(duck.quack()) # Quack!
```

### Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # B (follows MRO)
print(D.__mro__)   # Shows the order: D -> B -> C -> A -> object
```

### Checking Inheritance

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# isinstance() - check if object is instance of class
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True

# issubclass() - check if class is subclass of another
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

## 7. Polymorphism

Polymorphism allows different classes to be treated through the same interface.

### Method Overriding

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphic behavior
shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 3)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 20
# Area: 28.27431
# Area: 6
```

### Duck Typing

```python
# "If it walks like a duck and quacks like a duck, it's a duck"

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

# Any object with a speak() method works
def make_speak(entity):
    print(entity.speak())

make_speak(Dog())    # Woof!
make_speak(Cat())    # Meow!
make_speak(Robot())  # Beep boop!
```

## 8. Abstraction

Abstraction hides complex implementation details and shows only necessary features.

### Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        """Subclasses must implement this"""
        pass
    
    @abstractmethod
    def stop(self):
        """Subclasses must implement this"""
        pass
    
    # Concrete method (inherited as-is)
    def description(self):
        return f"This is a {self.brand} vehicle"

class Car(Vehicle):
    def start(self):
        return f"{self.brand} car engine starting..."
    
    def stop(self):
        return f"{self.brand} car engine stopping..."

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.brand} motorcycle revving..."
    
    def stop(self):
        return f"{self.brand} motorcycle shutting down..."

# Cannot instantiate abstract class
# vehicle = Vehicle("Generic")  # TypeError

# Can instantiate concrete subclasses
car = Car("Toyota")
print(car.start())        # Toyota car engine starting...
print(car.description())  # This is a Toyota vehicle
```

## 9. Special (Dunder) Methods

Special methods allow objects to work with built-in Python operations.

### Common Special Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation for users
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # String representation for developers
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Length
    def __len__(self):
        return self.pages
    
    # Equality comparison
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    # Less than comparison
    def __lt__(self, other):
        return self.pages < other.pages
    
    # Make object callable
    def __call__(self):
        return f"Reading {self.title}..."

book1 = Book("Python 101", "John Doe", 300)
book2 = Book("Python 101", "John Doe", 300)
book3 = Book("Java Basics", "Jane Doe", 250)

print(str(book1))       # 'Python 101' by John Doe
print(repr(book1))      # Book('Python 101', 'John Doe', 300)
print(len(book1))       # 300
print(book1 == book2)   # True
print(book1 == book3)   # False
print(book1 > book3)    # True (300 > 250)
print(book1())          # Reading Python 101...
```

### Arithmetic Operations

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 2)

print(v1 + v2)  # Vector(3, 5)
print(v1 - v2)  # Vector(1, 1)
print(v1 * 3)   # Vector(6, 9)
```

### Container Methods

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    # Length
    def __len__(self):
        return len(self.songs)
    
    # Indexing
    def __getitem__(self, index):
        return self.songs[index]
    
    # Setting item
    def __setitem__(self, index, value):
        self.songs[index] = value
    
    # Deletion
    def __delitem__(self, index):
        del self.songs[index]
    
    # Membership testing
    def __contains__(self, song):
        return song in self.songs
    
    # Iteration
    def __iter__(self):
        return iter(self.songs)

playlist = Playlist("My Favorites")
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

print(len(playlist))        # 3
print(playlist[0])          # Song A
print("Song B" in playlist) # True

for song in playlist:
    print(song)
```

### Special Methods Table

| Method | Purpose | Usage |
|--------|---------|-------|
| `__init__` | Constructor | `obj = Class()` |
| `__str__` | User-friendly string | `str(obj)`, `print(obj)` |
| `__repr__` | Developer string | `repr(obj)` |
| `__len__` | Length | `len(obj)` |
| `__eq__` | Equality | `obj1 == obj2` |
| `__lt__` | Less than | `obj1 < obj2` |
| `__add__` | Addition | `obj1 + obj2` |
| `__getitem__` | Indexing | `obj[key]` |
| `__setitem__` | Index assignment | `obj[key] = value` |
| `__contains__` | Membership | `item in obj` |
| `__iter__` | Iteration | `for item in obj` |
| `__call__` | Callable | `obj()` |

## 10. Composition vs Inheritance

### Composition ("has-a" relationship)

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine(200)  # Car HAS an engine
        self.wheels = [Wheel(17) for _ in range(4)]  # Car HAS wheels
    
    def start(self):
        return f"{self.brand}: {self.engine.start()}"

car = Car("Toyota")
print(car.start())  # Toyota: Engine started
print(car.engine.horsepower)  # 200
```

### When to Use Which

| Use Inheritance When | Use Composition When |
|---------------------|---------------------|
| There's a clear "is-a" relationship | There's a "has-a" relationship |
| You want to reuse code in base class | You want more flexibility |
| Classes are tightly related | Classes are loosely related |
| Example: Dog is an Animal | Example: Car has an Engine |

## 11. Dataclasses (Python 3.7+)

Dataclasses reduce boilerplate for classes that mainly store data:

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # Default value

# Automatically generates __init__, __repr__, __eq__
person = Person("Alice", 25)
print(person)  # Person(name='Alice', age=25, email='')

person2 = Person("Alice", 25)
print(person == person2)  # True

@dataclass
class Student:
    name: str
    grades: List[int] = field(default_factory=list)
    
    # Can still add methods
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("Bob")
student.grades.extend([85, 90, 78])
print(student.average())  # 84.33...
```

## Summary: Four Pillars of OOP

| Pillar | Description | Python Implementation |
|--------|-------------|----------------------|
| **Encapsulation** | Bundle data and methods, restrict access | Private (`__`), Protected (`_`), Properties |
| **Inheritance** | Create new classes from existing ones | `class Child(Parent):` |
| **Polymorphism** | Same interface, different implementations | Method overriding, Duck typing |
| **Abstraction** | Hide complexity, show essentials | Abstract base classes (`ABC`) |

## Best Practices

- Use meaningful class and method names
- Keep classes focused (Single Responsibility Principle)
- Prefer composition over inheritance when possible
- Use `@property` for controlled attribute access
- Use `super()` when overriding methods to extend functionality
- Define `__str__` and `__repr__` for better debugging
- Use abstract base classes to define interfaces
- Use dataclasses for simple data containers
- Follow the naming conventions: `_protected`, `__private`
- Document your classes and methods with docstrings
