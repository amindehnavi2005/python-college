from tkinter import *
########################################
def show_entry_fields():
    v = StringVar()
    label = Label(master, textvariable = v)
    v.set("First Name: %s, Last Name: %s" % (e1.get(), e2.get()))
    label.grid(row = 2)
########################################   
master = Tk()
master.title("Grid")
Label(master, text="First Name").grid(row = 0)
Label(master, text="Last Name").grid(row = 1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
button1 = Button(master, text = 'Quit', command = master.quit)
button1.grid(row = 3, column = 0, sticky = W, pady = 4)
button2 = Button(master, text = 'Show', command = show_entry_fields)
button2.grid(row = 3, column = 1, sticky = W, pady = 4)
mainloop( )
 