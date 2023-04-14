"""Usage of DateTime and Time methods"""

from datetime import date as d
input("Date example prints. Hit Enter.")

today = d.today() # current date as object of class date

# attributes of date object
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

a_date = d.fromisoformat('2019-11-04') # date from ISO
print(a_date)

a_date = d(1991, 2, 5) # date from (year,month,day)
print(a_date)

a_date = a_date.replace(year=1992, month=1, day=16) # replacing stuff
print(a_date)

print(a_date.weekday()) # 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
print(a_date.isoweekday()) # weekday() + 1


print("\n-------------------------------------------------\n")
input("Time example prints (from datetime module). Hit Enter.")
from datetime import  time as t

a_time = t(14, 53, 20, 1) # time object from datetime module

# attributes
print("Time:", a_time)
print("Hour:", a_time.hour)
print("Minute:", a_time.minute)
print("Second:", a_time.second)
print("Microsecond:", a_time.microsecond)

print("\n-------------------------------------------------\n")
input("Datetime example prints. Hit Enter.")
from datetime import datetime as dt

a_datetime = dt(2019, 11, 4, 14, 53) # datetime object from (year, month, day, hours, minutes)

# attributes
print("Datetime:", a_datetime)
print("Date:", a_datetime.date())
print("Time:", a_datetime.time())

# some methods of the datetime class
print("today:", dt.today())
print("now:", dt.now())
print("utcnow:", dt.utcnow())
print("Timestamp:", a_datetime.timestamp())

# String formatting
a_date = d(2020, 1, 4)
print(a_date.strftime('%Y/%m/%d'))

a_time = t(14, 53)
print(a_time.strftime("%H:%M:%S"))

a_datetime = dt(2020, 11, 4, 14, 53)
print(a_datetime.strftime("%y/%B/%d %H:%M:%S"))

# Get datetime object from (correctly) formatted String
print(dt.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

print("\n-------------------------------------------------\n")
input("Timedelta example prints. Hit Enter.")
from datetime import timedelta as td

# Calculating with dates returns timedelta object
d1 = d(2020, 11, 4)
d2 = d(2019, 11, 4)

print(d1 - d2) # timedelta object
print(type(d1-d2))

# ...so das calculating with datetimes
dt1 = dt(2020, 11, 4, 0, 0, 0)
dt2 = dt(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)
print(type(dt1-dt2))

# Calculating with timedeltas
delta = td(weeks=2, days=2, hours=3)
print(delta)

delta2 = delta * 2
print(f"Delta2: {delta2}")

print(f"Date: {d1}")
print(f"Date + delta2: {d1+delta2}")

print(f"Datetime: {dt1}")
print(f"Date + delta2: {dt1+delta2}")

print("\n-------------------------------------------------\n")
input("Time example prints (from time module). Hit Enter.")
import time

timestamp = time.time() # returns time as float (secs since Unix epoch)
print("Timestamp:", timestamp)

print("Process sleeps a while...")
for i in range(4):
    print(f"{3-i}...")
    time.sleep(1)

d = d.fromtimestamp(timestamp) # date object from time object
print("Date:", d)

print(time.ctime(timestamp)) # convert the timestamp to readable datetime-like string

print(time.gmtime(timestamp)) # returns struct_time object
print(time.localtime(timestamp)) # returns struct_time object

print(timestamp)
print(time.mktime(time.localtime(timestamp))) # mktime converts struct_time object back to float

# String formatting in time module
st = time.gmtime(timestamp)
print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))