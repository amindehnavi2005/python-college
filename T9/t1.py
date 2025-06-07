import tkinter
from tkinter import *
root =Tk()
root.title('Label')
w = Label(root, text = "I am first", bg = "red", fg = "white",
          padx = 50, font = ("Helvetica", 16))
w.pack()
var = StringVar()
w = Label(root, textvariable = var,  bg = "green", fg = "black",
          padx = 50, font=("Helvetica", 16))
w.pack()
var.set("I am second")
w = Label(root, text = "I am third", bg = "blue", fg = "white",
          padx = 50, font = ("Helvetica", 16))
w.pack()
root.mainloop()


