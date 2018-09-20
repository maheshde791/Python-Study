#! /usr/bin/python
import time
import datetime

localtime = time.localtime(time.time())
print("Local current time :", localtime)
print("-" * 80)
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
print("-" * 80)
print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: " , datetime.datetime.now())
print("Other way: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print("-" * 80)
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("-" * 80)
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
print("-" * 80)
#Getting the weekday of a certain date
mydate = datetime.date(2017,7,4)  #year, month, day
print(mydate.strftime("%A"))
print(type(mydate))
