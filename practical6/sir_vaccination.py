import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm# import necessary libraries
population=10000
infected_curve=[]
for j in range(11):
    S=[9999-j*1000]
    I=[1]
    R=[j*1000]
    beta=0.3
    gamma=0.05#set basic constant for simulation
    if j==10:#when j=10 S=[-1], give S a zero value to fix the error
        S=[0]
    for i in range(1000):
        x=beta*I[i]/10000#the probability of infection
        b=np.random.choice(range(2),S[i],p=[1-x,x])#simulate the infection one time
        S.append(S[i]-np.sum(b==1))#calculate suscpetible people after one-time infection
        I.append(I[i]+np.sum(b==1))#calculate infected people after one-time infection
        a=np.random.choice([0,2],I[i+1], p=[0.95,0.05])#simulate the recovery one time
        R.append(R[i]+np.sum(a==2))#calculate recovered people after one-time recovery
        I[i+1]-=np.sum(a==2)#record the final infected people after the whole turn
    infected_curve.append(I)

plt.figure(figsize=(6, 4), dpi=150)#set figure size and dpi
colormap = plt.cm.get_cmap('viridis', 11)#use the library to get some colors
for j in range(11):
    color=colormap(j)
    plt.plot(infected_curve[j], label=f"{10*j}%",color=color)#draw the lines of infected people with different vaccination rate
plt.xlabel("Time")#name x axis
plt.ylabel("Infected Population")#name y axis
plt.title("SIR Model Simulation of Herd Immunity")#give a title for the figure
plt.legend(loc='upper right')#the location of legend
plt.show()#show the figure
plt.savefig('SIR_vaccination.png',format='png')#save the figure