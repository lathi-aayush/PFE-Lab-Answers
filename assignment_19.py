# 19. A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.

# 1:10:30 and 1:15:30

hh1, mm1, ss1 = map(int, input("Enter 1st Timestamps in HH:MM:SS format : ").split())
hh2, mm2, ss2 = map(int, input("Enter 2nd Timestamps in HH:MM:SS format : ").split())

seconds = ((hh2 - hh1) * 3600) + ((mm2 - mm1) * 60) + (ss2 - ss1)

print(f"There are {seconds} seconds interval between these two timestamps")
