import pandas as pd

from sklearn import datasets # 导入 SciLearn 库

iris = datasets.load_iris()   # 获取鸢尾花的数据。这个数据SKlean 库中已经有了，是一个基础学习数据包。

species = [iris.target_names[x] for x in iris.target]

iris_final = pd.DataFrame(iris['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])

iris_final['Species'] = species

print(type(iris))

print(iris_final)