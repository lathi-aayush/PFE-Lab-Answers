# 13. Program to check if a year is leap

# A leap year is an year which is a multiple of 400 as well as 4
# so 1900 is not a leap year but 1600 is, so avoid this common mistake

year = int(input("Enter Year : "))

if year % 100 == 0 and year % 400 == 0:
    print(f"The Year {year} is a Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"The Year {year} is a Leap Year")
else:
    print(f"Year {year} is NOT Leap Year")
