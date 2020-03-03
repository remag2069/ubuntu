import matplotlib.pyplot as plt
import math as m

n=int(input('n'))
d=int(input('d'))
d=d*m.pi/180

r=[m.sin(n*k*d) for k in range(360)]
a=[k*d for k in range(360)]

x=[]
y=[]
for k in range(360):
    x.append(r[k]*m.cos(a[k]))
    y.append(r[k]*m.sin(a[k]))

plt.plot(x,y)
plt.show([-1,1,-1,1])