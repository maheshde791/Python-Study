#!/usr/bin/python

"""
def displayMessage():
   print("Hello World")

a = displayMessage
a()
b = a
print(id(a))
print(id(b))
"""

"""
def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print(greet("John"))
"""
"""
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return func(other_name)  

print(call_func(greet))
"""

"""
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print(greet())
"""

"""
def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("John")
print(greet())
"""
"""
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "Hi, {0} Welcome to Cybage".format(name)

print(get_text("John"))
"""


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper



#@div_decorate
#@p_decorate
#@strong_decorate
def get_text(name):
   return "Hi , {0} how are you".format(name)

#print(get_text("Sahil"))


get_text = div_decorate(p_decorate(strong_decorate(get_text)))
print(get_text('John'))














