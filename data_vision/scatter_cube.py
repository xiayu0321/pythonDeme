import matplotlib.pyplot as plt 

x_values = list(range(6))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Reds, s = 40)
plt.title('cube of numbers',fontsize = 22)
plt.xlabel('number',fontsize = 14)
plt.ylabel('cube of number',fontsize = 14)

plt.show()
