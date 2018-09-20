#! /usr/bin/python
def validHeight(cm):
    try:
        #cm = int(cm)
        cm = float(cm)
        return 100 <= cm <= 250
    except ValueError:
        return False
print(validHeight(190))

print(validHeight('190'))

print(validHeight(''))

print(validHeight('190.0'))