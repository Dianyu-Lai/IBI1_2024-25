import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.iloc[0:10,2]) #the year is 1999, and DALYs is 82624.94 in Afghanistan

is_1990 = dalys_data['Year'] == 1990
print(dalys_data.loc[is_1990,'DALYs']) #

uk=dalys_data.loc[dalys_data.Entity == 'United Kingdom',['DALYs','Year']]
uk_mean=uk['DALYs'].mean()
print(uk_mean)
france = dalys_data.loc[dalys_data.Entity == 'France',['DALYs','Year']]
france_mean = france['DALYs'].mean()
print(france_mean)
#the mean of UK is larger than the mean of France

plt.plot(uk.Year,uk.DALYs,'b+-',label = 'UK')
plt.title('DALYs over time in UK')
plt.xlabel('Year')
plt.ylabel('DALYs in UK')
plt.legend()
plt.xticks(uk.Year,rotation=-75)
plt.show()

#answer to question.txt
low_income = dalys_data.loc[dalys_data.Entity == 'World Bank Low Income',['DALYs','Year']]
high_income = dalys_data.loc[dalys_data.Entity == 'World Bank High Income',['DALYs','Year']]
plt.plot(low_income.Year,low_income.DALYs,'ro-',label='low income countries')
plt.plot(high_income.Year,high_income.DALYs,'bo-',label='high income countries')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over time, low income vs high income countries')
plt.xticks(low_income.Year,rotation=-75)
plt.legend()
plt.show()
