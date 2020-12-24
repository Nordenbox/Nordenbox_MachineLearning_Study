import pandas as pd

from sklearn import datasets # 导入 SciLearn 库

iris = datasets.load_iris()   # 获取鸢尾花的数据。这个数据SKlean 库中已经有了，是一个基础学习数据Bunch。

species = [iris.target_names[x] for x in iris.target] # 或许分类的列数据。数据的列（column）

iris = pd.DataFrame(iris['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']) #一次赋值

# DataFrame 是 pandas 的数据类型，分为行和列数据。

iris['Species'] = species  # 将 iris 的数据中的『类别』列，赋值给最终的数据。

print(type(iris), type(species), type(iris))

print(iris)
