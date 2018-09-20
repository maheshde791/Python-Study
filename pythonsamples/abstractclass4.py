#!/usr/bin/python
class Base(object):
	@property
	def example(self):
		raise NotImplementedError("sub class should implement this")

class Child(Base):
	def example(self):
		print("message")

#b = Base()
#print(b.example())
c = Child()
c.example()