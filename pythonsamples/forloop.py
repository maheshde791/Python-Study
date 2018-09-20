#!usr/bin/python
for num1 in [1,5,7,3,7,3,5,7,0,6,4,7,8]:
	try:
		num3 = 10/num1
		print(">"*80)
		print("number3----->" + str(num3))
		
	except ZeroDivisionError as err:
		print("Error: {0}".format(err))
		print("*"*80)
		continue
	else:
		#print("="*80)
		print("execution of else block")
		#print("="*80)
	finally:
		#print("-"*80)
		print("execution of the finally block")
		print("-"*80)
    