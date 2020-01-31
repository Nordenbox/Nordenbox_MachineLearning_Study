import numpy as np
import random


Origin_List = []
Dimentions = int(input('how many dimentions di you want: '))
range_scale = int(input('how large the random numbers: '))

for i in range(1, Dimentions+1):
    Origin_List.append([random.randint(0, range_scale+1) for i in range(1, Dimentions+1)])
    #    这个地方用了表达式，因为一开始使用的嵌套的 for 循环让我迷失了。

print(Origin_List)
new_four_dimensions = np.array(Origin_List)
print(new_four_dimensions)

