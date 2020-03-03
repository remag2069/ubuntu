import tkinter as tk
import random as r

factor=1.05
displacement=30

window=tk.Tk()

canvas=tk.Canvas(window,width=600,height=600,bg='black')
canvas.focus_set()

class stars():
    def __init__(self):
        # r.seed(x+y)
        self.c=[r.randint(-5000,5000),r.randint(-5000,5000),r.randint(0,500)]
        self.r=(r.random()*10)
        self.colour=r.randint(-10,10)
        self.in_view=True

def create_circle(c,r,colour):
    if colour>-9:
        col='white'
    elif colour>-10:
        col='white'
    else:
        col='#FFED8A'
    
    canvas.create_oval(c[0]-r,c[1]-r,c[0]+r,c[1]+r,fill=col)
    


# c1=[r.randint(50,550),r.randint(50,550),r.randint(0,500)]
# r1=(r.randint(0,100)+20)%100



# c2=[r.randint(0,600),r.randint(0,550),r.randint(0,500)]
# r2=r.randint(0,100)

st=[]
for i in range(2000):
    st.append(stars())

for i in range(len(st)):
    create_circle(st[i].c,st[i].r,st[i].colour)

# co1=canvas.coords(o1)

# def update()

def background():
    canvas.delete("all")
    canvas.create_line(300,0,300,600)
    canvas.create_line(0,300,600,300)
    canvas.configure(bg='black')

def zoom(event):
    global r1,r2,st
    # print(event)
    for i in st:
        i.c[0] = factor*(i.c[0] - event.x + event.x/factor)
        i.c[1] = factor*(i.c[1] - event.y + event.y/factor)
        i.r=i.r*factor
    # c2[0] = factor*(c2[0] - event.x + event.x/factor)
    # c2[1] = factor*(c2[1] - event.y + event.y/factor)
    # r1=r1*factor
    # r2=r2*factor
    # print(c1)
    background()
    # create_circle(c1,r1)
    # create_circle(c2,r2)
    for i in range(len(st)):
        create_circle(st[i].c,st[i].r,st[i].colour)
    window.update()

def zoom_out(event):
    print('out')
    global st
    # print(event)
    for i in st:
        i.c[0] = (i.c[0] - event.x + factor*event.x)/factor
        i.c[1] = (i.c[1] - event.y + factor*event.y)/factor
        i.r=i.r/factor
    # c2[0] = (c2[0] - event.x + event.x*factor)/factor
    # c2[1] = (c2[1] - event.y + event.y*factor)/factor
    # r1=r1/factor
    # r2=r2/factor
    # print(c1)
    background()
    # create_circle(c1,r1)    
    # create_circle(c2,r2)
    for i in range(len(st)):
        create_circle(st[i].c,st[i].r,st[i].colour)
    window.update()

def right(event):
    print('right')
    global st
    for i in st:
        i.c[0] = i.c[0]-displacement
        i.c[1] = i.c[1] 
    background()
    for i in range(len(st)):
        create_circle(st[i].c,st[i].r,st[i].colour)
    window.update()

def left(event):
    print('right')
    global st
    for i in st:
        i.c[0] = i.c[0]+displacement
        i.c[1] = i.c[1] 
    background()
    for i in range(len(st)):
        create_circle(st[i].c,st[i].r,st[i].colour)
    window.update()
def up(event):
    print('right')
    global st
    for i in st:
        i.c[0] = i.c[0]
        i.c[1] = i.c[1]+displacement 
    background()
    for i in range(len(st)):
        create_circle(st[i].c,st[i].r,st[i].colour)
    window.update()
def down(event):
    print('right')
    global st
    for i in st:
        i.c[0] = i.c[0]
        i.c[1] = i.c[1]-displacement
    background()
    for i in range(len(st)):
        create_circle(st[i].c,st[i].r,st[i].colour)
    window.update()

canvas.bind('<z>',zoom)
canvas.bind('<Z>',zoom_out)
canvas.bind('<Right>',right)
canvas.bind('<Left>',left)
canvas.bind('<Up>',up)
canvas.bind('<Down>',down)
# print(c1)

canvas.pack()
window.mainloop()