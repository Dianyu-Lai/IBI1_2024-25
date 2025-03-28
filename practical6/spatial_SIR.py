import numpy as np
import matplotlib.pyplot as plt#import libraries
import random
N=np.zeros((100,100))
beta=0.3
gamma=0.05#set constant for simulation
I= np.random.choice(range(100), 2)
N[I[0],I[1]]=1#the first infection outbreaks
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(N, cmap= 'viridis', interpolation= 'nearest')
plt.axis('off')
plt.title('initial case')
plt.show()

#points=np.where(N==1)
for t in range(100):
    for i in range(100):
        for j in range(100):
            if N[i,j]==1:
                for m in range(-1,2):
                    if 0<=i+m<100:
                        for n in range(-1,2):
                            if 0<=j+n<100:
                                if N[i+m,j+n]==0:
                                    N[i+m,j+n]=np.random.choice(range(2),p=[0.7,0.3])
                N[i,j]=np.random.choice([1,2],p=[0.95,0.05])
    if t in [0,9,49,99]:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(N, cmap= 'viridis', interpolation= 'nearest')
        plt.axis('off')
        plt.title(f'{t+1} day')
        plt.show()
        #plt.savefig('spatial_SIR.png',format='png')