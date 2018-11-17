import matplotlib.pyplot as plt 

x_values = list(range(1,11))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Blues,edgecolor = None,s = 40)

plt.title("Square numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

plt.axis([0,11,0,110])

plt.show()