# WAP to reverse an integer number:
n = int(input("Enter an integer to reverse it:"))
reverse = 0
while n >0:
    digit = n % 10          # Modulo by 10 will give the digits of number one by one
    reverse = reverse * 10 + digit
    n //= 10                # floor operator decreases the digit one by one
print("the reverse of", n, "is: ", reverse)


