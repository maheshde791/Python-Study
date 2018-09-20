#!/usr/bin/python
"""
var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"
"""




#work around for switch statement
def week(i):
	switcher={
		0:'Sunday',
		1:'Monday',
		2:'Tuesday',
		3:'Wednesday',
		4:'Thursday',
		5:'Friday',
		6:'Saturday'
	}
	return switcher.get(i,"Invalid day of week")

print(week(10))
















