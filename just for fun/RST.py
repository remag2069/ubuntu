from tkinter import *
from tkinter import font
import os

path=input('please give the path of the file')

window=Tk()
def dom():
    window.wm_attributes("-topmost", 1)
def sub():
    window.wm_attributes("-topmost", 0)
def run():
    os.system("start /wait cmd /c ")
    print("start /wait cmd /c "+path)
h=font.Font(family='Helvetica', size=18, weight='bold')
menubar = Menu(window)
t_color=Menu(menubar,tearoff=0)
t_color.add_command(label='dominate',command=dom)
t_color.add_command(label='subordinate',command=sub)

menubar.add_cascade(label="superiority", menu=t_color)
# f.add_command(label="text colours", command=toggle_color_m)
# filemenu.add_command(label="New", command=donothing)
b1=Button(window,text='RUN',font=h,command=run)
b1.pack()

window.config(menu=menubar)

window.mainloop()