# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
population=10000
S=[9999]
I=[1]
R=[0]
beta=0.3
gamma=0.05#set basic constant for simulation

for i in range(1000):
    x=beta*I[i]/10000#the probability of infection
    b=np.random.choice(range(2),S[i],p=[1-x,x])#simulate the infection one time
    S.append(S[i]-np.sum(b==1))#calculate suscpetible people after one-time infection
    I.append(I[i]+np.sum(b==1))#calculate infected people after one-time infection
    a=np.random.choice([0,2],I[i+1], p=[0.95,0.05])#simulate the recovery one time
    R.append(R[i]+np.sum(a==2))#calculate recovered people after one-time recovery
    I[i+1]-=np.sum(a==2)#record the final infected people after the whole turn

plt.figure(figsize=(6, 4), dpi=150)#set figure size and dpi
plt.plot(S, label="Susceptible", color="blue")#draw the line for susceptible people
plt.plot(I, label="Infected", color="red")#draw the line for sinfected people
plt.plot(R, label="Recovered", color="green")#draw the line for recovered people
plt.xlabel("Time")#name x axis
plt.ylabel("Population")#name y axis
plt.title("SIR Model Simulation")#give a title for the figure
plt.legend(loc='upper right')#the location of legend
plt.show()#show the figure
plt.savefig('simpleSIR.png',format='png')#save the figure
