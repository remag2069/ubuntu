import tkinter as tk



window=tk.Tk()

canvas=tk.Canvas(window,width=600,height=600,bg='red')
canvas.focus_set()

def create_circle(c,r):
    o1=canvas.create_oval(c[0]-r,c[1]-r,c[0]+r,c[1]+r)

c1=[300,300]
r=50
create_circle(c1,r)
# co1=canvas.coords(o1)


def background():
    canvas.delete("all")
    # canvas.create_line(0,0,600,600)
    # canvas.create_line(0,600,600,0)
    canvas.configure(bg='red')

def zoom(event):
    global r
    print(event)
    c1[0] = 2*(c1[0] - event.x + 150)
    c1[1] = 2*(c1[1] - event.y + 150)
    r=r*2
    print(c1)
    background()
    create_circle(c1,r)
    window.update()

def zoom_out(event):
    print('out')
    global r
    print(event)
    c1[0] = (c1[0] - event.x + 600)/2
    c1[1] = (c1[1] - event.y + 600)/2
    r=r/2
    print(c1)
    background()
    create_circle(c1,r)
    window.update()


canvas.bind('<z>',zoom)
canvas.bind('<Z>',zoom_out)
print(c1)

canvas.pack()
window.mainloop()