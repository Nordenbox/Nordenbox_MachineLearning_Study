import pandas as pd

from sklearn import datasets # 导入 SciLearn 库

iris = datasets.load_iris()   # 获取鸢尾花的数据。这个数据SKlean 库中已经有了，是一个基础学习数据Bunch。

species = [iris.target_names[x] for x in iris.target] # 或许分类的列数据。数据的列（column）

iris = pd.DataFrame(iris['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']) #一次赋值

# DataFrame 是 pandas 的数据类型，分为行和列数据。

iris['Species'] = species  # 将 iris 的数据中的『类别』列，赋值给最终的数据。

print(type(iris), type(species), type(iris))

#print(iris)

iris['count'] = 1
iris[['Species', 'count']].groupby('Species').count() # 合并统计 分类和个数

print(iris[['Species', 'count']].groupby('Species').count())




def plot_iris(iris, col1, col2):
    import seaborn as sns # Seaborn is a Python visualization library based on matplotlib
    import matplotlib.pyplot as plt

    sns.lmplot(x = col1, y = col2,
               data = iris,
               hue = "Species",
               fit_reg = False)

    plt.xlabel(col1)

    plt.ylabel(col2)

    plt.title('Iris species shown by color')

    plt.show()

plot_iris(iris, 'Petal_Width', 'Sepal_Length')

plot_iris(iris, 'Sepal_Width', 'Sepal_Length')


from sklearn.preprocessing import scale

import pandas as pd

num_cols = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

iris_scaled = scale(iris[num_cols])

iris_scaled = pd.DataFrame(iris_scaled, columns = num_cols)

print(iris_scaled.describe().round(3))