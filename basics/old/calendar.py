# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:00:22 2018

@author: maheshde
"""

import calendar
import time
import datetime

cal = calendar.month(2018,9)
print(cal)

localtime = time.localtime(time.time())
print("Local current time:",localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Local current time:",localtime)
print("Time in seconds:%s"%time.time())
print("Current Date and Time:", datetime.datetime.now())