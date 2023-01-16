# 2. Smallest and Largest in 5 numbers-
smallest, largest = 0, 0
n = int(input("Enter the value of n: "))
for i in range(0, n):
    num = int(input("Enter number: "))
    if i == 0:
        smallest = largest = num
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("Smallest= ", smallest)
print("Largest= ", largest)