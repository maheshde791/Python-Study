#! /usr/bin/python
class A(object):
  def call(self):
    pass
 
class B1(A):
  def call(self):
    print("I am parent B1")
 
class B2(A):
  def call(self):
    print("I am parent B2")
 
class B3(A):
  def call(self):
    print("I am parent B3")
 
class C(A):
  def call(self):
    print("I (C) was not invited")
 
class ME(B1, B2, B3):
  def whichCall(self):
    #print("which", self.call())
    self.call()
 
  def restructure(self, parent1, parent2, parent3):
    self.__class__.__bases__ = (parent1, parent2, parent3)
 
  def printBaseClasses(self):
    print("print base calsses" , self.__class__.__bases__)

me = ME()

me.printBaseClasses()
# result > (<class __main__.B2 at 0x8b1c02c>, <class __main__.B1 at 0x8b1c62c>, <class __main__.B3 at 0x8b1c05c>)
me.whichCall()
# result > I am parent B2


me.restructure(B3, B2, B1)
me.printBaseClasses()
# result > (<class __main__.B1 at 0xa27f62c>, <class __main__.B3 at 0xa27f05c>, <class __main__.B2 at 0xa27f02c>)
me.whichCall()
# result > I am parent B1
print("-" * 80)
me.restructure(B2, B1, B3)
me.printBaseClasses()
# result > (<class __main__.B1 at 0xa27f62c>, <class __main__.B3 at 0xa27f05c>, <class __main__.B2 at 0xa27f02c>)
me.whichCall()
# result > I am parent B1



















"""
me.restructure(C, B3, B2)
me.printBaseClasses()
# result > (<class __main__.C at 0xa27f08c>, <class __main__.B3 at 0xa27f05c>, <class __main__.B2 at 0xa27f02c>
me.whichCall()
# result > I (C) was not invited
"""

