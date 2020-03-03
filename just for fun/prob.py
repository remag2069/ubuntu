import random as r
a=0
b=0
c=0
for i in range(10000):
    k=r.randint(-1,1)
    if k==-1:
        a=a+1
    if k==0:
        b=b+1
    if k==1:
        c=c+1
print(str(a)+ ' ' + str(b)+ ' ' + str(c))