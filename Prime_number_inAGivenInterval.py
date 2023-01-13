# Write a program to fine all prime number till an entered number and also fine number of prime number:-
print("Enter the lower bound: ", end="")
a = int(input())
b = int(input("Enter upper bound: "))
print("All the prime number from", a, "to", b, "are: ")
count = 0
for i in range(a, b+1):
    if i == 0 or i == 1:
        continue
    flag = 0
    for j in range(2, i//2+1):
        if i % j ==0:
            flag = 1
            break
    if flag == 0:
        print(i, end=", ")
        count += 1
print()
print("Total prime number from", a, "to", b, "is", count)