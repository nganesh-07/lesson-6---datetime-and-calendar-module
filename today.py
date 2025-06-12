from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("The time is currently", now)

print("We are in the year", today.year)
print("In the", today.month, "month of the year")
print("Today is the", today.day, "of the month")