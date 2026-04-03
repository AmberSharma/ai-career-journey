def count_lines(filename):
    with open(filename) as f:
        content = f.readlines()
        return len(content)


print(count_lines('error.txt'))