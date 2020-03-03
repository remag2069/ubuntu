# import tkinter as tk
# l=10
# def draw(can,x_c,y_c):
#     print('draw')
#     can.create_line(x_c-l,y_c,x_c+l,y_c)
    

# class stick:
#     x=400
#     y=400
#     def __init__(self,v_x,v_y):
#         self.v_x=v_x
#         self.v_y=v_y

# root=tk.Tk()
# s=stick(10,5)
# can=tk.Canvas(root,width=800,height=800)
# def update():
#     s.x=s.x+s.v_x
#     s.y=s.y+s.v_y
#     draw(root,s.x,s.y)
#     print('hi')
#     # root.after(10000,update())
# update()
# draw(can,s.x,s.y)
# can.grid(row=0,column=0)
# root.mainloop()

import tkinter as tk
import time
v_x=9.6
v_y=7.9
window=tk.Tk()
c=tk.Canvas(width=600,height=600)
ball=c.create_oval(0,0,100,100)
c.grid(row=0,column=0)

prevpos=[0,0,0,0]
while True:
    c.move(ball,v_x,v_y)
    pos=c.coords(ball)
    c.create_line(prevpos[0],prevpos[1],pos[0],pos[1])
    if pos[2]>=600:
        v_x=-v_x
    if pos[0]<=0:
        v_x=-v_x
    if pos[3]>=600:
        v_y=-v_y
    if pos[1]<=0:
        v_y=-v_y
    prevpos=pos
    window.update()
    time.sleep(0.01)