import numpy as np
import matplotlib.pyplot as plt
n = 0.1
list_x =[]
list_y=[]
for r in range(1,1000):
    list_x.append(r)
    for i in range(1000):
        n = r*n*(1-n)
        print(n, '\n')
    list_y.append(n)

x = np.array(list_x)
y = np.array(list_y)

plt.plot(list_x, list_y)
plt.show()