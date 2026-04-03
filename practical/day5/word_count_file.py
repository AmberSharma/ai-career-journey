def count_words(filename):
    try:
        with open(filename) as f:
            text = f.read()
            words = text.split()

            frequency = {}
            for word in words:
                frequency[word] = frequency.get(word, 0) + 1

            print(frequency)
    except FileNotFoundError:
        print("File not found")

word_count = count_words("words.txt")
