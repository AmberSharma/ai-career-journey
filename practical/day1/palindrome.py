# PALINDROME

num = str(input("Enter a number:"))
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")