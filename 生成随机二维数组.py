import numpy as np
import random


b = []

for i in range(1, 5):
    b.append([random.randint(0, 10) for i in range(1, 5)]) 
    #    这个地方用了表达式，因为一开始使用的嵌套的 for 循环让我迷失了。

print(b)
new_four_dimensions = np.array(b)
print(new_four_dimensions)
