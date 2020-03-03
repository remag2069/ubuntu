import tkinter as tk
import time

class circle():
    radius=0

size=int(input('size'))


window=tk.Tk()
c=[]
speed=[]
speed.append(0.3)
for i in range(size):
    c.append(circle())
    speed.append(speed[i]+0.3)

canvas=tk.Canvas(window,height=600,width=600)
def grow():
    global canvas
    for i in range(size):
        canvas.create_oval(300-c[i].radius,300-c[i].radius,300+c[i].radius,300+c[i].radius,fill='white')

    for i in range(size):
        c[i].radius=c[i].radius+speed[i]
        # if c[i].radius>420:
        #     c.pop(i)
        canvas.create_oval(300-c[i].radius,300-c[i].radius,300+c[i].radius,300+c[i].radius)

canvas.pack()
while True:
    grow()
    time.sleep(0.0002)
    canvas.update()