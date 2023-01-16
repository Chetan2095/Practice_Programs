# WAP to find sum of digits of an integer number:
print("Enter a number to find sum of it's digits: ")
n = int(input())
Sum = 0
while n > 0:
    digit = n % 10      # Modulo by 10 will give the digits of number one by one
    Sum = Sum + digit
    n = n // 10         # floor operator decreases the digit one by one
print("Sum of digit is= ", Sum)