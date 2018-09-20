#! /usr/bin/python

class A(object):
   message = "class message"

   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo(self, msg):
      self.message = msg
      print(self.message)

   def __str__(self):
      return self.message

a = A()
a.foo('Hello')
#a.foo('Hello')
A.cfoo()
#a.cfoo()
print(id(A))
print(id(a))

