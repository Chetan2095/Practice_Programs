# 11111
# 2222
# 333
# 44
# 5

# 12345
# 2345
# 345
# 45
# 5

# *****
# ****
# ***
# **
# *

for i in range(1, 6):
    for j in range(i, 6):
        print(i, end="")
        # print(j, end="")
        # print("*", end="")
    print()

# 55555
# 4444
# 333
# 22
# 1

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

# 54321
# 4321
# 321
# 21
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# 1
# 22
# 333
# 4444
# 55555
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(i, end="")
        # print("*", end="")
    print()

# Pattern using 'while' loop:
i = 1
while i < 6:
    j = i
    while j > 0:
        print(i, end="")
        j -= 1
    print()
    i += 1

# A
# A
# AB
# ABC
# ABCD
# ABCDE

x = 65
print(chr(x))

for i in range(1, 6):
    A = 65
    for j in range(i, 0, -1):
        print(chr(A), end="")
        A += 1
    print()

# CCCCCC
# HHHHH
# EEEE
# TTT
# AA
# N

s = "CHETAN"
for i in range(len(s)):
    for j in range(len(s), i, -1):
        print(s[i], end="")
    print()

s = "CHETAN"
i = 0
while i < len(s):
    j = i
    while j < len(s):
        print(s[i], end="")
        j += 1
    print()
    i += 1

    # space    Stare
#   *          2        1
#  ***         1        3
# *****        0        5
#  ***         1        3
#   *          2        1

# for half top pattern(n=3 lines)-
n = 3
for i in range(1, n + 1):  # 1, 2, 3
    space = (n - i) * " "
    star = (2 * i - 1) * "*"
    print(space, star)
# for the bottom half-
for j in range(n - 1, 0, -1):  # 2, 1
    space = (n - j) * " "
    star = (2 * j - 1) * "*"
    print(space, star)

          # space(n-i)
#     1         4
#    212        3
#   32123       2
#  4321234      1
# 543212345     0
# space >> decreasing number >> increasing number, :

n = 5
for i in range(1, n + 1):  # This will print the space before the number
    space = (n - i) * " "
    print(space, end="")
    for j in range(i, 1, -1):  # This for loop will print the decreasing numbers
        print(j, end="")
    for k in range(1, i + 1):  # This for loop will print the increasing numbers
        print(k, end="")
    print()                    # Print a new line after the space and numbers are printed


          #space(n-i)
# 12345       0
#  1234       1
#   123       2
#    12       3
#     1       4


#   *
#  * *
# *   *
#  * *
#   *
# Space >> number
n = 5
for i in range (n, 0, -1):      # The space will increase on each iteration as i value will decrease
    space = (n - i)*"  "
    print(space, end=" ")
    for j in range(1, i + 1):   #This for loop will print the increasing numbers
        print(j, end=" ")
    print()

# Space >> star
n = 3
k = 0
for i in range (1, n + 1):
    space = (n - i)*" "
    print(space, end=' ')
    while k != (2 * i - 1):     #This will print the star at the start and end of every line
        if k == 0 or k == 2 * i - 2:
            print('*', end= "")
        else :                     #This will print the space in the middle
            print(' ', end = "")
        k = k + 1
    k = 0
    print()
for j in range (n - 1, 0, -1):    #This will print the bottom half of the hollow diamond shape
    space = (n - j)*" "
    print(space, end=" ")
    k = (2 * j - 1)
    while (k > 0) :                 #This will print the star at the start and end of every line
        if k==1 or k == 2*j-1:
            print("*",end="")
        else:                        #This will print the space in the middle
            print(" ",end="")
        k = k - 1
    print()