#!/usr/bin/python


import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Cybage@123',
                             db='pythondb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

"""
import pymysql
import pymysql.cursors

#print("Hello World")

# Open database connection

db = pymysql.connect(passwd="Cybage@123",db="pythondb",host="127.0.0.1",port=3306,user="root",charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("db", db)
# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")




sql = "select * from employee"

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		name = row[0]
		dpt = row[1]
		sal = row[2]
		print("name=%s,department=%s,sal=%d" % \
             (name, dpt, sal))
except:
	print("Unable to fetch data")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print "Database version : %s " % data

# disconnect from server
db.close()
"""
