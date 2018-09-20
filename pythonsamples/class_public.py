#!/usr/bin/python
class Cup:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, beverage):
        self.content = beverage
        print "in fill method"

    def empty(self):
        self.content = None
        print "in empty method"

redCup = Cup()
redCup.color = "red"
redCup.content = "tea"
redCup.empty()
redCup.fill("coffee")