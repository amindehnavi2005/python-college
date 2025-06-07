# برنامه ای بنویسید که با هر کلیک موس کاربر یا کلیک روی صفحه کلیک رنگ پس زمینه صفحه را تغییر دهد.

import tkinter
from tkinter import *
root = Tk()
title = "Click any button,or press a key"
label = Label(root,text=title)

def change_bg_key(event):
    colors = {
        "r": "red",
        "g": "green",
        "b": "blue",
        "y": "yellow",
        "w": "white"
    }
    color = colors.get(event.char, None)
    if color:
        root.config(bg=color)

# تابع تغییر رنگ پس‌زمینه برای ماوس
def change_bg_mouse(event):
    root.config(bg="lightblue")

# اتصال رویدادهای صفحه‌کلید
root.bind("<Key>", change_bg_key)

# اتصال رویدادهای ماوس
root.bind("<Button-1>", change_bg_mouse)  # کلیک چپ ماوس

# اجرای حلقه اصلی برنامه
root.mainloop()