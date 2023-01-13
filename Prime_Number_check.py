# Write a program to check the entered number is prime or not:-
n = int(input("Enter a number to check whether it is prime or not: "))
flag = 0
if n == 0 or n == 1:
    flag = 1
for i in range(2, n//2):
    if n % i == 0:
        flag = 1
        break
if flag == 0:
    print(n, "is a Prime number.")
else:
    print(n, "is not a Prime number.")