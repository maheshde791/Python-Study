#! /usr/bin/python

class S(object):
   nInstances = 0
   def __init__(self):
      S.nInstances = S.nInstances + 1

   @staticmethod
   def howManyInstances():
      print('Number of instances created: ', S.nInstances)

a = S()
b = S()

S.howManyInstances()
a.howManyInstances()
b.howManyInstances()
