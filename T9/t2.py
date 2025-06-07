import tkinter
from tkinter import *
root = Tk()
v = StringVar()
label = Label(textvariable = v, fg = "blue")
v.set("You didn't click button")
def clickTest(event) :
    v.set("You clicked button")
########################################
label.pack()
b = Button(text = "Click me")
b.pack(pady = 30)
b.bind('<Button-1>', clickTest)
mainloop()
    