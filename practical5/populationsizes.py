import matplotlib.pyplot as plt#import library

uk_countries=[57.11,3.13,1.91,5.45]
china_provinces=[65.77,41.88,45.28,61.27,85.15]
print(uk_countries)
print(china_provinces)#population of each components

uk=["England","Wales","Northern Ireland","Scotland"]#name of components
zj_neighboring=["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]
color1=['blue','red','yellow','green']#colors used in pie chart
color2=color1.append('pink')

plt.figure(figsize=(6,6))#pie chart 1 to draw England
plt.pie(uk_countries,labels=uk,colors=color1)
plt.title('population distribution of England')
plt.show()

plt.figure(figsize=(6,6))#pie chart 2 to draw zhejiang neighboring provinces
plt.pie(china_provinces,labels=zj_neighboring,colors=color2)
plt.title('population distribution of Zhejiang neighboring provinces')
plt.show()