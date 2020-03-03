import numpy as np
import matplotlib.pyplot as plt
import random as r

#r.seed(123)
training_data={'inp':[[1,1],[0,1],[1,0],[0,0]],'out':[1,0,0,0]}
w1= r.randint(-1,1)
w2= r.randint(-1,1)
weights=[w1,w2]
w_=[]
y_=[]
print(training_data)
print(weights)

for i in range(0,4):
    for j in range(0,2):
        y_.append(training_data['inp'][i][j]*weights[j])

for i in range(0,1000):
    e=0
    for j in range(0,4):
        e=e+(training_data['out'][j]-y_[j])**2
    e=e**0.5
    print(e)
    j=r.randint(0,3)
    t=training_data['out'][j]
    if t==y_[j]:
        pass
    else:
        for j in range(0,2):
            w_.append(weights[j]+training_data['out'][j]*y_[j])
    weights=w_
    for k in range(0,4):
        for j in range(0,2):
            y_.append(training_data['inp'][k][j]*weights[j])
            
