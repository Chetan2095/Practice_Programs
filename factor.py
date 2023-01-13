num = int(input("Enter a number to get it's factor: "))
print(1, end=", ")
factor = 2
while factor <= num / 2:
    if num % factor == 0:
        print(factor, end=", ")
    factor += 1
print(num)

OR #

num = int(input("Enter a number to find it's factor: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=", ")