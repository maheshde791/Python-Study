#!/usr/bin/python


from Tkinter import *
import tkMessageBox

root = Tk()
root.title('A Tkinter Example')

frame = Frame()
frame.pack()

def helloCallBack():
	print("one button clicked")
	tkMessageBox.showinfo( "Hello Python","Hello World")

Button(frame, text='One',command=helloCallBack).pack(side=TOP, pady=5)
Button(frame, text='Two').pack(side=TOP, pady=5)
Button(frame, text='Three').pack(side=TOP, pady=5)

frame2 = Frame(frame)
frame2.pack(side=TOP, pady=5)

Button(frame2, text='Apple').pack(padx=5, side=LEFT)
Button(frame2, text='Banana').pack(padx=5, side=LEFT)
Button(frame2, text='Cranberry').pack(padx=5, side=LEFT)

Button(frame, text='Durian').pack(pady=5, side=BOTTOM)

root.mainloop()

"""
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
    messagebox.showinfo( "Hello Python","Hello World")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
"""


















