# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#set basic constant for simulation
population=10000
S = [9999]
I = [1]
R = [0]
beta = 0.3
gamma = 0.05

#simulate the infection and recovery process
for i in range(1000):
    #simulate the infection one time
    x = beta*I[i]/10000 #the probability of infection
    b = np.random.choice(range(2),S[i],p = [1-x,x]) 
    
    #refresh the number of susceptible population
    S.append(S[i]-np.sum(b == 1))
    
    #simulate the recovery one time
    a = np.random.choice([0,1],I[i], p = [0.95,0.05])

    #refresh the number of infected people and recovered people after one-time recovery
    R.append(R[i]+np.sum(a == 1)) 
    I.append(I[i] + np.sum(b == 1) - np.sum(a == 1))

#plot the susceptible, infected, and recovered population in one figure
plt.figure(figsize = (6, 4), dpi=150)

#draw the line for susceptible, infected, and recovered people
plt.plot(S, label = "Susceptible", color = "blue")
plt.plot(I, label = "Infected", color = "red") 
plt.plot(R, label = "Recovered", color = "green")

plt.xlabel("Time") 
plt.ylabel("Population") 
plt.title("SIR Model Simulation") #give a title for the figure
plt.legend(loc='upper right') #the location of legend
plt.show() #show the figure
