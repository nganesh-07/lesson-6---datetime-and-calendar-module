import random
import time

def getrandomdate(startdate, endDate):
    print("Printing a random date between", startdate, "and", endDate)
    randomgenerator = random.random()
    format = "%m/%d/%Y"

    timestart = time.mktime(time.strptime(startdate, format))
    endtime = time.mktime(time.strptime(endDate, format))

    randomtime = timestart+randomgenerator * (endtime - timestart)
    randomdate = time.strftime(format, time.localtime(randomtime))
    return randomdate
print("Your random date is", getrandomdate("3/14/2025", "7/29/2025"))