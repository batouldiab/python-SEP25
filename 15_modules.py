# module = package = library
import sys # built-in module
print(sys.version) # prints: installed python version

# dates module
import datetime
d = datetime.datetime.now()
print(d)
print(d.year)
print(d.day)
print(d.strftime("%A")) #Weekday, full version: Wednesday
print(d.strftime("%a")) #Weekday, short version: Wed
print(d.strftime("%w")) #Weekday as a number 0-6, 0 is Sunday
print(d.strftime("%B")) #Month name, full version: September
print(d.strftime("%b")) #Month name, short version: Sep
print(d.strftime("%m")) #Month as a number 01-12
print(d.strftime("%d")) #Day of month 01-31	
print(d.strftime("%y")) #Year, short version, without century: 18
print(d.strftime("%Y")) #Year, full version: 2018
print(d.strftime("%H")) #Hour 00-23: 17
print(d.strftime("%I")) #Hour 00-12: 05
print(d.strftime("%p")) #AM/PM: PM
print(d.strftime("%M")) #Minute 00-59: 41
print(d.strftime("%S")) #Second 00-59: 06
print(d.strftime("%f")) #Microsecond 000000-999999: 548513
print(d.strftime("%z")) #UTC offset: +0200
print(d.strftime("%j")) #Day number of year 001-366
print(d.strftime("%U")) #Week number of year, Sunday as the first day of week, 00-53
print(d.strftime("%W")) #Week number of year, Monday as the first day of week, 00-53
print(d.strftime("%c")) #Local version of date and time: Mon Dec 31 17:41:00 2018
print(d.strftime("%C")) #Century: 20
print(d.strftime("%x")) #Local version of date: 12/31/18
print(d.strftime("%X")) #Local version of time: 17:41:00

day = d.strftime("%A")
print(day)

# creating date:
new_date = datetime.datetime(2020, 9, 30)
new_date2 = datetime.datetime(2020, 9, 15)
print(new_date - new_date2)

# math module
x= -10
abs_x = abs(x)
print(abs_x)

import math
x = 64
v = math.sqrt(x)
print(v)

res = math.pow(2,3)
print(res)

pi = math.pi
print(pi)

print(math.ceil(1.4))
print(math.floor(1.4))

# importing installed library
# to install library, run: pip install camelcase
# to upgrade library, run: pip install --upgrade camelcase
# to uninstall library, run: pip uninstall camelcase
import camelcase
c = camelcase.CamelCase()
txt = 'this is any text.'
print(c.hump(txt))