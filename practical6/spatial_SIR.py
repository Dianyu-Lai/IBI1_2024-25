#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

#initialise the array and constants for simulation
N = np.zeros((100,100))
beta = 0.3
gamma = 0.05

#initialise the first infection outbreaks and plotting
I = np.random.choice(range(100), 2)
N[I[0], I[1]] = 1
plt.figure(figsize = (6,4), dpi = 150)
plt.imshow(N, cmap = 'viridis', interpolation= 'nearest')
plt.axis('off')
plt.title('initial case')
plt.show()

#simulate the 2D spread of infection
for t in range(100): #100 days
    for i in range(100): #100 columns
        for j in range(100): #100 rows
            if N[i,j] == 1:
                for m in range(-1,2):
                    if 0 <= i + m < 100:
                        for n in range(-1,2):
                            if 0 <= j + n < 100:
                                if N[i + m,j + n] == 0:
                                    N[i + m,j + n] = np.random.choice(range(2),p = [0.7,0.3])
                    else:
                        break
                N[i,j] = np.random.choice([1,2],p = [0.95,0.05])
    if t in [0,9,49,99]:
        plt.figure(figsize = (6,4),dpi=150)
        plt.imshow(N, cmap = 'viridis', interpolation = 'nearest')
        plt.axis('off')
        plt.title(f'{t+1} day')
        plt.show()
