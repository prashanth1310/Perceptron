import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



X1 = np.array([[1,1,1]])
X2 = np.array([[1,1,0]])
X3 = np.array([[1,0,1]])
X4 = np.array([[1,0,0]])


y1 = np.array([[1]])
y2 = np.array([[-1]])
y3 = np.array([[-1]])
y4 = np.array([[-1]])



#X=np.insert(X,0,1,axis=1)
print X3

#m=y.shape[0]
alpha=1
threshold=0.5

weight=np.zeros((3,1))

print weight

def out(X1,weight):
    weightsum=np.dot(X1,weight)
    
    if(weightsum>0.5):
        return 1
    elif(weightsum<(-0.5)):
        return -1
    else:
        return 0
    
    
print out(X1,weight)


for i in xrange(100):
    if(y1!=out(X1,weight)):
        weight+=np.dot(X1.T,y1)
    if(y2!=out(X2,weight)):
        weight+=np.dot(X2.T,y2)
    if(y3!=out(X3,weight)):
        weight+=np.dot(X3.T,y3)
    if(y4!=out(X4,weight)):
        weight+=np.dot(X4.T,y4)
    print weight    