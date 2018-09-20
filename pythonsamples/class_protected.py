#!/usr/bin/python
class Cup(object):
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def _fill(self, beverage):
        self._content = beverage
        print("in fill method " + self._content)

    def empty(self):
        self._content = None
        
class Tea(Cup):
	def __init__(self):
		super(Tea,self).__init__()

cup = Cup()
cup._fill("tea")        

tea = Tea()
tea._fill('tea')