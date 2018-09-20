#!/usr/bin/python

class Employee(object):
    empCount = 0;
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d",Employee.empCount)

    def displayEmployee(self):
        print("Name=",self.name + "=>Salary=",self.salary)



emp1 = Employee("abc",20000)

emp1.displayEmployee()

print("Total Employee ",Employee.empCount)

emp2 = Employee("xyz",30000)
emp2.displayEmployee()

print("Total Employee ", Employee.empCount)

print(getattr(emp1,"name"))


print("-" * 80)
print("Employee.__doc__ " , Employee.__doc__)
print("Employee.__name__ " , Employee.__name__)
print("Employee.__module__ " , Employee.__module__)
print("Employee.__bases__ " , Employee.__bases__)
print("Employee.__dict__ " , Employee.__dict__)
print("-" * 80)









