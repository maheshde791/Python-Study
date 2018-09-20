#! usr/bin/phthon 
#C:\python33

import smtplib
try:
	smtpObj = smtplib.SMTP('localhost',25)
	smtpObj.sendmail("vikasja@cybage.com", "vikasswara@gmail.com", "message")
	print "success"
except SMTPException:
	print "error"


    