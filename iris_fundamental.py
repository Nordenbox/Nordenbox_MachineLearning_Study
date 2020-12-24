from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import numpy as np
import pandas as pd

from sklearn import datasets  # 导入 SciLearn 库

iris = datasets.load_iris()  # 获取鸢尾花的数据。这个数据SKlean 库中已经有了，是一个基础学习数据Bunch。

species = [iris.target_names[x] for x in iris.target]  # 或许分类的列数据。数据的列（column）

iris = pd.DataFrame(iris['data'], columns=[
    'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])  # 一次赋值

# DataFrame 是 pandas 的数据类型，分为行和列数据。

iris['Species'] = species  # 将 iris 的数据中的『类别』列，赋值给最终的数据。

print(type(iris), type(species), type(iris))

# print(iris)

iris['count'] = 1
iris[['Species', 'count']].groupby('Species').count()  # 合并统计 分类和个数

print(iris[['Species', 'count']].groupby('Species').count())


def plot_iris(iris, col1, col2):
    import seaborn as sns  # Seaborn is a Python visualization library based on matplotlib
    import matplotlib.pyplot as plt

    sns.lmplot(x=col1, y=col2,
               data=iris,
               hue="Species",
               fit_reg=False)

    plt.xlabel(col1)

    plt.ylabel(col2)

    plt.title('Iris species shown by color')

    plt.show()


# plot_iris(iris, 'Petal_Width', 'Sepal_Length')

# plot_iris(iris, 'Sepal_Width', 'Sepal_Length')


num_cols = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']  # 创立一个列表

iris_scaled = scale(iris[num_cols])
# DataFrame 类型的iris_scaled使用这个列表，赋值给一个新的 DataFrame 变量， sklearn 的scale 函数提取数据

iris_scaled = pd.DataFrame(iris_scaled, columns=num_cols)  # 再一次赋值，列的title 由列表 num_cols 给出

# print(iris_scaled.describe().round(3))  # pandas 的一些参数。describe 参数为显示主要数据统计：最大值，最小值，中位值
# round 保留多少位小数


levels = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
# 每一列平均值为 0，标准差大约是 1.0。为了分类需要，我们用字典把花种从字符串类型转换成数字表示。

iris_scaled['Species'] = [levels[x] for x in iris['Species']]  # 这个数据表格增加一列数据 Species

print(iris_scaled.head())  # 默认显示头五行的数据。

'''follow:
把数据集随机分割成样本训练集和评估数据集，训练集用来训练 KNN 模型，评估集用来测试和评估 KNN 的分类结果。'''

np.random.seed(3456)

iris_split = train_test_split(np.asmatrix(iris_scaled), test_size=75)

iris_train_features = iris_split[0][:, :4]

iris_train_labels = np.ravel(iris_split[0][:, 4])

iris_test_features = iris_split[1][:, :4]

iris_test_labels = np.ravel(iris_split[1][:, 4])

print(iris_train_features.shape)

print(iris_train_labels.shape)

print(iris_test_features.shape)

print(iris_test_labels.shape)

'''数据准备好后，就是第三步训练模型了。这里我们使用 K=3 来训练 KNN 模型，当然你也可以调整这个参数来进行观察和调优。'''

KNN_mod = KNeighborsClassifier(n_neighbors=3)

KNN_mod.fit(iris_train_features, iris_train_labels)

'''模型测试，这里我们使用测试集来测试模型。'''
iris_test = pd.DataFrame(iris_test_features, columns = num_cols)

iris_test['predicted'] = KNN_mod.predict(iris_test_features)

iris_test['correct'] = [1 if x == z else 0 for x, z in zip(iris_test['predicted'], iris_test_labels)]

accuracy = 100.0 * float(sum(iris_test['correct'])) / float(iris_test.shape[0])

print(accuracy)