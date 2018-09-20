#!usr/bin/python

class parent(object):
    parentAttr = 100;
    def __init__(self):
        print("Parent Constructor")

    def parentMethod(self):
        print("In Parent Method")

    def setAtt(self, attr):
        parent.parentAttr = attr

    def getAtt(self):
        print("Parent Attribute",parent.parentAttr)

    def message(self):
        print("Parent message")


class child(parent):
    childAtt = 200;
    def __init__(self):
        print("Child Constructor")

    def childMethod(self):
        print("In Child Method")

    def message(self):
        print("child message")
        super(child,self).message()


c1 = child()
c1.message()
c1.childMethod()
c1.parentMethod()
c1.setAtt(500)
c1.getAtt()
