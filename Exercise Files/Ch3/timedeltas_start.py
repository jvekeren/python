#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta



# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("today is: " + str(now))

# print today's date one year from now
print("one year from now:" + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("2 days and 3 weeks:" + str(now + timedelta(days=2,weeks=3)))


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %b %d, %Y")
print (s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("1 april is al %d dagen voorbij" %((today-afd).days))
    afd = afd.replace(year = today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("nog maar: ", time_to_afd.days, "dage tot 1-april")


today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)])

print(date.today())
print(datetime.date(datetime.now()))