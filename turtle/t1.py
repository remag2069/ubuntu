import turtle
import math as m
d=turtle.Turtle()
#r=float(input("radius of circle"))
d.speed(100000)
for i in range(0,200):
    d.forward(1)
    d.right(360/200)
turtle.done()
x=[]
y=[]
for i in range(0,200):
    x.append(i)
    y.append(i*2)

for i in range(1,200):
    #d.penup()
    r=y[i]%200
    a=90-(180-360*r/200)/2
    print(float(a))
    l=200*m.sin(a*m.pi/180)/m.sin((r*360/200)*m.pi/180)
    d.right(a)
    d.forward(l)
    
    for i in range(0,200-r):
        d.forward(1)
        d.right(360/200)

    for i in range(0,x[i]):
        d.forward(1)
        d.right(360/200)    