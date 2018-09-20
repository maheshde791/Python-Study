#!usr/bin/python

def imageDetails():
	return "16X16",1024,"png",'root/images'

dimension, size, imagetype, path = imageDetails()
print(dimension)
print(size)
print(imagetype)
print(path)	
