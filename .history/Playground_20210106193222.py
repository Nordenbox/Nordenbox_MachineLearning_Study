import time
import matplotlib.pyplot as plt
n = 0.1
list_x = [j for j in range(10000)]
list_y=[]
for i in range(10000):
    n = 4*n*(1-n)
    print(n, '\n')
    list_y.append(n)


plt.plot.scatter(list_x, list_y)
plt.show()