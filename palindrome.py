# WAP to Check if a Number is a Palindrome:
num = int(input("Enter a number: "))
reverse = 0
n = num
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
if num == reverse:
    print(num, "is a palindrome number.")
else:
    print(num, "n is not a palindrome number.")


