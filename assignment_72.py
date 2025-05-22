# 72. Write a Python program to plot line chat, bar chart, pi chart, scatter chart, histogram for taking two different arrays as input.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y)
plt.show()
plt.bar(x, y)
plt.show()
plt.pie(y, labels=x)
plt.show()
plt.scatter(x, y)
plt.show()
plt.hist(y)
plt.show()
