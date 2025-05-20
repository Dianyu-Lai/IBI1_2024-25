#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#initialise the array and constants for simulation
N = np.zeros((100,100))
beta = 0.3
gamma = 0.05

#initialise the first infection outbreaks and plotting
cmap = ListedColormap(['#BBBBBB', '#FF6666', '#66CC66'])
I = np.random.choice(range(100), 2)
N[I[0], I[1]] = 1
plt.figure(figsize = (6,4), dpi = 150)
plt.imshow(N, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
plt.axis('off')
plt.title('initial case')
plt.show()

#simulate the 2D spread of infection
for t in range(100): #100 days
    N_new = N.copy() #create a copy to avoid over-infection

    for i in range(100): #100 columns
        for j in range(100): #100 rows
            if N[i,j] == 1:
                #recover
                N_new[i,j] = np.random.choice([1,2],p = [1 - gamma, gamma])
                #infect the neighbors
                for m in range(-1,2):
                    for n in range(-1,2):
                        if (m, n) != (0, 0) and 0 <= i + m < 100 and 0 <= j + n < 100:
                            if N[i+m, j+n] == 0 and np.random.rand() < beta:
                                N_new[i+m, j+n] = 1
    N = N_new #update the array after recovery and infection
                
    #plot the 2D figure in day 1, day 10, day 50, and day 100
    if t in [0,9,49,99]:
        plt.figure(figsize = (6,4), dpi = 150)
        plt.imshow(N, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
        plt.axis('off')
        plt.title(f'{t+1} day')
        plt.show()
