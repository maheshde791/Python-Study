#!/usr/bin/python
class Cup(object):
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable

    def __fill(self, beverage):
        self.__content = beverage
        print "in fill method " + self.__content

    def empty(self):
        self.__content = None
        print "in empty mehtod"

redCup = Cup("red")
redCup.__fill('tea')
redCup.empty()


