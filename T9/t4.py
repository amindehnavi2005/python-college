title='creating a frame'
from tkinter import *
root = Tk()
frame = Frame(root, borderwidth = 10)
frame.pack(side = LEFT, padx = 15, pady = 15)
label = Label(frame , text = 'I am in frame')
label.pack(side = LEFT)
label2 = Label(root, text = "I am in root")
label2.pack(side = RIGHT)
button = Button(frame, text = "I am in frame")
button.pack(side = RIGHT)
root.title(title)
root.mainloop()