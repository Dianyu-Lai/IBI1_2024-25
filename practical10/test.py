import matplotlib.pyplot as plt

#create lists storing the population and names
uk=[57.11,3.13,1.91,5.45]
cn=[65.77,41.88,45.28,61.27,85.15]
uk_name=["England","Wales","Northern Ireland","Scotland"]
cn_name=["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]

#sort the list based on population, while not change the matches
sorted_uk=sorted(zip(uk,uk_name),reverse=True)
sorted_cn=sorted(zip(cn,cn_name),reverse=True)
uk_sorted,uk_sorted_name=zip(*sorted_uk)
cn_sorted,cn_sorted_name=zip(*sorted_cn)

#print the sorted lists
print(list(uk_sorted_name),list(uk_sorted))
print(list(cn_sorted_name),list(cn_sorted))

#colors used in pie chart
color1=['blue','red','yellow','green']
color2=color1.append('pink')

#pie chart 1 to draw England
plt.figure(figsize=(6,6))
plt.pie(uk_sorted,labels=uk_sorted_name,colors=color1,autopct='%1.1f%%')
plt.title('population distribution of England')
plt.legend()
plt.show()

#pie chart 2 to draw zhejiang neighboring provinces
plt.figure(figsize=(6,6))
plt.pie(cn_sorted,labels=cn_sorted_name,colors=color2,autopct='%1.1f%%')
plt.title('population distribution of Zhejiang neighboring provinces')
plt.legend()
plt.show()