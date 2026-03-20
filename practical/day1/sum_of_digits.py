# Sum of Digits
num = str(input("Enter a number:"))
sum_of_digits = 0
for i in num:
    sum_of_digits += int(i)

print(sum_of_digits)