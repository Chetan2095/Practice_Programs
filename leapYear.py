# leap year:
print("Enter a year: ")
year = int(input())
if year % 400 == 0:                    # (Century) - leap year if perfectly divisible by 400 - eg. 1600, 2000
    print(year, "is a leap year.")
elif year % 100 == 0:                  # (Century) - not divisible by 400 but by 100 - eg. 1700, 1800, 1900
    print(year, "is NOT a leap year.")
elif year % 4 == 0:                    # (not century) - divided by 4 but not by 100
    print(year, "is a leap year.")
else:
    print(year, "is NOT a leap year.")
