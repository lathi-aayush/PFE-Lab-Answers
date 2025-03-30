# 14. Program to check if a date is valid

# simple logic is to find the date to be between 30 and 31 and month between 12 and year has no limit other than being 4 digit + february leap year logic as well

dd, mm, yyyy = map(int, input("Enter Date in 'DD MM YYYY' format : ").split())

m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]
m2 = [2]

# to find if this is a leap year
if (yyyy % 100 == 0 and yyyy % 400 == 0) or (yyyy % 4 == 0 and yyyy % 100 != 0):
    leap_year = 'true'
else:
    leap_year = 'false'

# for months with 31 days
if dd > 0 and dd <= 31 and (mm in m31):
    d = 'true'
# for months with 30 days
elif dd > 0 and dd <= 30 and (mm in m30):
    d = 'true'
# for february we have to think of leap year as well
elif dd>0 and dd<=29 and leap_year=='true'and (mm in m2):
    d = 'true'
elif dd>0 and dd<=28 and leap_year=='false' and (mm in m2):
    d = 'true'
else:
    d = 'false'  
 
# to find if month is correct
if mm > 0 and mm < 13:
    m = 'true'
else:
    m ='false'
    
if d == 'true' and m == 'true':
    validity = 'valid'
else:
    validity = 'invalid'
    
print(f"The Date Entered {dd}-{mm}-{yyyy} is {validity}")


