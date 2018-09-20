#! /usr/bin/python
import os;

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print("while loop exit!")

print("-" * 80)


list = ["cat", "dog", "panther", "parakeet"]

i = 0
while i < len(list):
    element = list[i]
    i += 1

    # Test for this element.
    if element == "panther":
        continue

    # Display element.
    print("Pet", element)

"""
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data");
else:
   print ("Written content in the file successfully");
 """

#fo = open("sample.txt","wb");
#print("name of the file", fo.name);
#print("is closed", fo.closed);
#print("opening mode", fo.mode);
#fo.write("Python is great language");
#fo.close();

#s = "Python is great language";

#f = open('sample.txt', 'rb+')
#f.write(b"Python is great language");

#for line in f:
 #   print(line, end='')

#f.close();


#dir_fd = os.open('c:\pythonsamples', os.O_RDONLY);

#def opener(path, flags):
#    return os.open(path, flags, dir_fd=dir_fd)

#with open('spamspam.txt', 'w', opener=opener) as f:
#   print('This will be written to somedir/spamspam.txt', file=f);




