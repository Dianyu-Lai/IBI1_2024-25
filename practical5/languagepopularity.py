import matplotlib.pyplot as plt#import library I need

language=["JavaScript", "HTML", "Python","SQL", "TypeScript"]#build two list and then a dictionary
popularity=[62.3,52.9, 51, 51, 38.5]

catergory_dict=dict(zip(language,popularity))
print(catergory_dict)#print dictionary

plt.bar(language,popularity)
plt.xlabel("language")
plt.ylabel("popularity")#draw the plot with x,y label and title
plt.title("the percentage of developers who use the top 5 programming languages globally")
plt.show()#show the plot

x=input("which language?")#ask for user's input
if x in catergory_dict:
    print(f"the percentage of developers who use this language is {catergory_dict[x]}")
else:
    print("language not found")#a simple fix to avoid bugs