# FACTORIAL
num = int(input("Enter a number:"))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1

# Better Strategy
# for i in range(1, num+1):
#     factorial *= i

print(factorial)