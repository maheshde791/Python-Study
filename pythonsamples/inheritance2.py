#!/usr/bin/python
class Person(object):

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

    def displayName(self):
        print(self.firstname + " " + self.lastname)

class Employee(Person):

    def __init__(self, first, last, staffnum):
        super(Employee, self).__init__(first, last)
        self.staffnumber = staffnum
        
    def __str__(self):
        return super(Employee, self).__str__() + ", " +  self.staffnumber    


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x)
print(y)
