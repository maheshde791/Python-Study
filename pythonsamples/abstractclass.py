#!/usr/bin/python
from abc import ABCMeta, abstractmethod

class Animal(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def say_something(self): pass

class Cat(Animal):
    def say_something(self):
        return "Miauuu!"

a = Animal()
b = Cat()
print(b.say_something())