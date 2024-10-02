import os
os.system('cls')
import matplotlib.pyplot as plt
import pandas as pd
#Real life based program
##PLOTING LINE GRAPH:
#Sales of  smartphones in plot line format:
data=pd.read_csv(r"C:\Users\RIYA\OneDrive\Desktop\VS Code Quickstart\sales_revenue.csv")
plt.plot(data['Year'],data['Xiaomi-Sales'],label='Xiaomi')
plt.plot(data['Year'],data['Apple-Sales'],label='Apple')
plt.plot(data['Year'],data['Samsung'],label='Samsung')
plt.plot()
plt.title("Comparative Analysis of Smartphone Sales",fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('Yearwise Sales',fontdict={'fontsize':10})
plt.ylabel('Sales in millions',fontdict={'fontsize':10})
plt.legend()
plt.show()
#Revenue of the smartphones:
plt.plot(data['Year'],data['XR'],'r',label='Xiaomi Revenue')
plt.plot(data['Year'],data['AR'],'k',label='Apple Revenue')
plt.plot(data['Year'],data['SR'],'b',label='Samsung Revenue')
plt.title("Comparative Analysis of Revenue",fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('Yearwise Revenue',fontdict={'fontsize':10})
plt.ylabel('Revenue in billions(USD)',fontdict={'fontsize':10})
plt.legend()
plt.show()
#To summarise the revenue within 5 year gap:
plt.xticks(data['Year'][::5])
plt.plot(data['Year'],data['XR'],'r*-',label='Xiaomi Revenue')
plt.plot(data['Year'],data['AR'],'^k:',label='Apple Revenue')
plt.plot(data['Year'],data['SR'],'b.-',label='Samsung Revenue')
plt.title("Summarized Comparative Analysis of Revenue with a 5year gap ",fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('Yearwise Revenue',fontdict={'fontsize':10})
plt.ylabel('Revenue in billions(USD)',fontdict={'fontsize':10})
plt.legend()
plt.show()