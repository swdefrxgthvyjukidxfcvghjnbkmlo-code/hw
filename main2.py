"""
Author: Ivan Chang
Date: August 26, 2025
Description: Gives the Time Left in the Day
"""

MINUTES_IN_DAY =  1440
MINUTES_IN_HOUR = 60

print("""Welcome to the Time Left in the Day Calculator!
Please use a 24-hour format.""")

curHour = int(input("Enter the current hour (0-23): "))
curMinute = int(input("Enter the current minute (0-59): "))

totalMinutesLeft = MINUTES_IN_DAY - (curHour * MINUTES_IN_HOUR + curMinute)

hoursLeft = totalMinutesLeft // MINUTES_IN_HOUR
minutesLeft = totalMinutesLeft % MINUTES_IN_HOUR

print(f"There are {totalMinutesLeft} minutes remaining in the day.")
print(f"That is {hoursLeft} hours and {minutesLeft} minutes until midnight.")
