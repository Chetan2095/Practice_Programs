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








