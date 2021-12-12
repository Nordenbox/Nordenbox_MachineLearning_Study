'''
这是在夜曲编程上学习人工智能基础的一个程序，基于文本的监督学习。
里面的注释为课堂上的内容，不少部分也有自己的添加。
'''
# 导入csv模块
import csv
import numpy as np

# 使用open()函数打开数据集
file = open("TVComments_5000.csv", "r")
# 使用csv.reader()函数读取数据集
reader = csv.reader(file)

# make reader to a list，到这一步还是清楚的，即拿到数据。
# 这个数据是一个列表，多层嵌套的列表。
data = list(reader)
   
# 导入jieba模块。多个模块组建成一个特定的包，但彼此的包含关系并不确定。几个包组合成一个库。
import jieba

#  创建一个空列表word存储结果

word =[]
# 使用for循环遍历data列表
# 似乎有更简便的办法，不用列表遍历循环，或者有某个函数直接可以用。
for row in data:
    # 获取具体的评价内容，并赋值给变量text。
    # data 是一个二维列表，即有两层嵌套。第二层元素是一个列表，有两个元素，第一个是具体的评价文本。所以这里取第一个。
    text = row[0]
    # 使用jieba.lcut()将text进行分词，并把结果赋值给ret。输出是一个列表。
    ret = jieba.lcut(text)
    
    # 使用join()方法，将分词结果以空格合并为一个完整的字符串。
    # join 不是函数而是方法，所以前面要用类来调用。
    ret = ' '.join(ret)
    
    #  使用append()方法，添加分词结果到列表word中。 
    # word 实质上一个类的实例化，然后再调用类中的方法 append
    # word 现在是一个所有评价的列表文档。
    word.append(ret)
   

# 从sklearn.feature_extraction.text中导入CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# 创建CountVectorizer对象，并存储在vect中.
# CountVectorizer是一个类，class。
# 对小的数据集，最好别在这里设定 max_feature，如果特征标签取的少的话，会学习不好。
vect = CountVectorizer()

# 通过vect.fit_transform()方法，加入参数word，构造词袋模型。
# fit_transform 要求的参数是一个可迭代的文档，比如列表。word 目前就是一个。
# X 目前是一个阵列，形如（样本数，特征数）的陈列。
X = vect.fit_transform(word)

# 对于目前这个样本数据集，执行 np.shape(X)可以得到它是一个（4238，7977）的阵列
# 其中有 4283 个评价，提取特征数量为 7977

# 使用toarray()方法，将x转换为数组 ndarray
X = X.toarray()  # one-hot 编码又是一个知识点

# 创建一个空列表y，用于存储标签
y = []
# 使用for循环遍历data，将遍历的数据存储到allInfo变量中
# 两层嵌套的列表，第二层是第二个元素是评价标签，也是人工给定的 label
for allInfo in data:
    # 提取allInfo中的标签数据，注意提取第二层的第二个。
    label = allInfo[1]
    
    # 将标签逐一添加到列表y中
    y.append(label)

    
# 从sklearn.model_selection模块中导入train_test_split函数
from sklearn.model_selection import train_test_split

# 划分数据集，将数据分为训练集和测试集。
# 返回的数据被分成了四个部分：训练集特征，测试集特征，训练集标签，测试集标签
#result = train_test_split(X, y, train_size=0.8, random_state=1)

#以下代码可以替代对训练集索引。
(train_feature,
test_feature,
train_label,
test_label )= train_test_split(X,y,train_size= 0.75,random_state = 1)

'''
# 和上面的相同结果，依次提取result中训练集和测试集数据
train_feature = result[0]
test_feature = result[1]
train_label = result[2]
#  提取测试集的标签test_label
test_label = result[3]
'''


# 输出测试集的标签test_label
#print(test_label)

'''5. 生成分类器模型'''

# TODO 从sklearn.neural_network中导入MLPClassifier
from sklearn.neural_network import MLPClassifier

# TODO 创建MLPClassifier对象，并存储在mlp变量中
mlp = MLPClassifier()

# TODO 使用fit()方法，通过train_feature和train_label，训练分类器。
# 训练集特征与训练集标签（人工）有一一对应的关系。让机器用算法确定一个数学模型。
# mlp 变量调用了 MLPClassifier 类
mlp.fit(train_feature, train_label)

'''6. 评估模型准确率'''

# TODO 从sklearn.metrics中导入accuracy_score
from sklearn.metrics import accuracy_score

# TODO 对测试集数据进行预测，换句话说就是要求输出对测试特征的标签结果。
# mlp_pred 就是对 test_label 的假想对应结果。
mlp_pred = mlp.predict(test_feature)

# TODO 计算预测准确率，并将结果赋值给score。
score = accuracy_score(mlp_pred,test_label)

# TODO 输出准确率
print(score)


'''7. 自定义评价，并预测'''

# TODO 自定义一条评价，并存储在变量comment中
comment = '屏幕还不错，总体来说也可以推荐'

# 使用jieba.lcut()对comment进行分词
comment = jieba.lcut(comment)
# 使用join()函数处理分词结果
comment =  [' '.join(comment)]
# 构造词袋模型
try_feature = vect.transform(comment)
# 使用toarray()函数把结果转换为NumPy数组
try_feature = try_feature.toarray()
# 使用predict()函数预测结果（前面 mlp 模型已经经过训练了，fit 方法）
try_pred = mlp.predict(try_feature)
# 输出预测结果
print(try_pred)