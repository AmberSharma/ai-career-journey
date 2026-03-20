# LARGET OF THREE NUMBERS

x, y, z = input("Enter three numbers: ").split()
print(x,y,z)
if x > y:
    if x > z:
        print(f"{x} is the largest number")
    else:
        print(f"{z} is the largest number")
else:
    if y > z:
        print(f"{y} is the largest number")
    else:
        print(f"{z} is the largest number")