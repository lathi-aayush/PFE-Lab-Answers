#  H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now. 

H = int(input("Enter Time in Hours (1 to 12): "))
M = int(input("Enter Time in minutes : "))
S = int(input("Enter Time in seconds : "))

# converting hours to degrees
hd = H*30 #hd means hours degrees

# converting minutes to degrees
md = M*6 #md means minute degrees

# total degrees 
td = hd+md

# converting hours to degrees
# seconds doesn't need anything, you can directly write this 

print(f"{H} Hours, {M} Minutes, {S} Seconds in Clock hand Degrees is : {td} Degrees '{S} Seconds")