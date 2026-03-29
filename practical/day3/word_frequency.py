fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_count = {}
for fruit in fruits:
    word_count[fruit] = word_count.get(fruit, 0) + 1

print(word_count)