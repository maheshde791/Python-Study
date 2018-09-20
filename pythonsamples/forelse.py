#!/usr/bin/python

def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print ("list contains an even number")
            break
 
    # This else executes only if break is NEVER
    # reached and loop terminated after all iterations.
    else:     
        print ("list does not contain an even number")
 
# Driver code
print("For List 1:")
contains_even_number([1, 9, 7, 3, 8])
print(" \nFor List 2:")
contains_even_number([1, 3, 5])


"""
for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print(num, 'is a prime number')
"""