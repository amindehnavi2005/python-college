import tkinter
from tkinter import *
root = Tk()
prompt='Click any button, or press a key'
label = Label(root, text = prompt, width = len(prompt), font=("Helvetica", 16))
label.pack(pady = 50)
###################################
def key(event):
    if event.char == event.keysym:
        msg ='Normal Key %r' % event.char
    elif len(event.char) == 1:
        msg ='Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg ='Special Key %r' % event.keysym
    label.config(text = msg)
label.bind_all('<Key>', key)
###################################
def do_mouse(eventname):
    def mouse_binding(event):
        msg = 'Mouse event %s' % eventname
        label.config(text = msg)
    label.bind_all('<%s>'%eventname, mouse_binding)
###################################
for i in range(1,4):
    do_mouse('Button-%s'%i)
    do_mouse('ButtonRelease-%s'%i)
    do_mouse('Double-Button-%s'%i)
###################################
root.mainloop()