numbers = [1, 2, 3, 4, 5]

# Using list comprehension
squares = list(filter(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Using map()
squares = list(map(lambda x: x ** 2, numbers))
print(squares)