#!/usr/bin/python

import pymysql



#print("Hello World");

# Open database connection
db = pymysql.connect("localhost","root","Cybage@123","pythondb")

#print db


# prepare a cursor object using cursor() method
cursor = db.cursor()



sql = "INSERT INTO EMPLOYEE(name, \
       dept, sal) \
       VALUES ('%s', '%s', '%d' )" % \
       ('ABC', 'Sales', 50000)
try:
	cursor.execute(sql)
	db.commit()
except Exception as e:
	print("Unable to insert data")
	print(e)
	db.rollback()

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

# disconnect from server
db.close()
