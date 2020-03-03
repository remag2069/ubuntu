import tkinter as tk
window=tk.Tk()
count=0
t1=tk.Entry(window)
t2=tk.Entry(window)
t3=tk.Entry(window)



class rest:
    def __init__(self,r,n1,n2):
        self.r=r
        self.n1=n1
        self.n2=n2
        print(self.r+self.n1+self.n2)

res=[]

def create():
    global count,t1,t2,t3,res
    if count>0:
        n1=t1.get()
        n2=t2.get()
        n3=t3.get()
        t=rest(float(n1),float(n2),float(n3))
        res.append(t)
        
    l1=tk.Label(window,text='input'+str(count+1))
    l1.grid(row = 4, column = 0)
    l2=tk.Label(window,text='resistor')
    l3=tk.Label(window,text='node before')
    l4=tk.Label(window,text='node after')
    e1=tk.Entry(window)
    l2.grid(row = 5, column = 0)
    e1.grid(row = 5, column = 2)
    e2=tk.Entry(window)
    l3.grid(row = 6, column = 0)
    e2.grid(row = 6, column = 2)
    e3=tk.Entry(window)
    l4.grid(row = 7, column = 0)
    e3.grid(row = 7, column = 2)
    t1=e1
    t2=e2
    t3=e3
    count=count+1





    
def init_node(x):
    t=[]
    for i in range(0,len(res)):
        if res[i].n1==x:
            t.append(i)
    return t

def end_node(x):
    t=[]
    for i in range(0,len(res)):
        if res[i].n2==x:
            t.append(i)
    return t


def r(n):
    r_net=0
    start=init_node(n)
    k=res[start[0]].n2
    try:
        for i in start:
            if i.n2==k:
                t=t+1/i.r
            # else:
            #     pass
            r_net=1/t
    except:
        print('k'+str(k))
    if k==0:
        return r
    
    r_net=r_net+r(k)
    return r_net


def eq_rest():
    for i in range(0,len(res)):
        print(str(res[i].r)+'  '+str(res[i].n1)+'  '+str(res[i].n2)+'  ')
    r_net=r(1)
    print(r_net)

     


b1=tk.Button(window,text='create',command=create)
b1.grid(row = 0, column = 1)

b2=tk.Button(window,text='calculate',command=eq_rest)
b2.grid(row = 11, column = 1)

tk.Tk.mainloop(window)


