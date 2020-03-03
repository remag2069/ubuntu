from tkinter import *
window=Tk()
pic=PhotoImage(file='D:\\python projects\\searcheingine\\d.gif')
c=Canvas(width=pic.width,height=pic.height)
c.create_image(0,0,image=pic,anchor=NW)
c.pack()
window.mainloop()