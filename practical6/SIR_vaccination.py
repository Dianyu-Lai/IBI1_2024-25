# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#initialise the populations and basic constants
population = 10000
infected_curve = []
beta = 0.3
gamma = 0.05

for j in range(11):
    I = [1]
    R = [int((population-I[0])*j/10)]
    S = [population - I[0] - R[0]]

    #simulate the infection and recovery process with vaccination rate
    for i in range(1000):
        x = beta * I[i] / 10000#the probability of infection
        b = np.random.choice([0,1],S[i],p = [1-x,x])#simulate the infection one time
        a = np.random.choice([0,1],I[i], p = [0.95,0.05])#simulate the recovery one time

        #refresh the population of S, I, and R
        S.append(S[i] - np.sum(b == 1))      
        R.append(R[i] + np.sum(a == 1))
        I.append(I[i] + np.sum(b == 1) - np.sum(a == 1))
    infected_curve.append(I)

#figure plotting
plt.figure(figsize = (6, 4), dpi = 150)

#use the library to get some colors, and draw the lines of infected people with different vaccination rate
colormap = plt.cm.get_cmap('viridis', 11)
for j in range(11):
    color = colormap(j)
    plt.plot(infected_curve[j], label = f"{10*j}%",color = color)
plt.xlabel("Time")
plt.ylabel("Infected Population")
plt.title("SIR Model Simulation of Herd Immunity")
plt.legend(loc = 'upper right')#the location of legend
plt.show()
