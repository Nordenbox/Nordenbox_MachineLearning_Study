# 导入csv模块
import csv

# 使用open()函数打开数据集
file = open("hotelComment_300.csv", "r")
# 使用csv.reader()函数读取数据集
reader = csv.reader(file)
# 创建一个空列表data
data = []
# 使用for循环遍历reader，将遍历的数据存储到变量info中
for info in reader:
    # 使用append()函数，将info逐一添加到data列表中
    data.append(info)  # 也可以使用 list()方法
    
# 导入jieba模块
import jieba

# TODO 创建一个空列表word存储结果

word =[]
# 使用for循环遍历data列表
for row in data:
    # 获取具体的评价内容，并赋值给变量text
    text = row[0]
    # 使用jieba.lcut()将text进行分词，并把结果赋值给ret
    ret = jieba.lcut(text)
    
    # 使用join()函数，将分词结果以空格合并为一个完整的字符串
    ret = ' '.join(ret)
    
    # TODO 使用append()函数，添加分词结果到列表word中
    word.append(ret)
   
# 输出word进行查看

# 从sklearn.feature_extraction.text中导入CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# 创建CountVectorizer对象，并存储在vect中
vect = CountVectorizer(max_features=15)

# 通过vect.fit_transform()和word，构造词袋模型
X = vect.fit_transform(word)

# 使用toarray()函数，将x转换为数组
X = X.toarray()

# 创建一个空列表y，用于存储标签
y = []
# 使用for循环遍历data，将遍历的数据存储到allInfo变量中
for allInfo in data:
    # 提取allInfo中的标签数据
    label = allInfo[1]
    # 将标签逐一添加到列表y中
    y.append(label)

    
# 从sklearn.model_selection中导入train_test_split
from sklearn.model_selection import train_test_split

# 划分数据集，将数据分为训练集和测试集
result = train_test_split(X, y, train_size=0.8, random_state=1)

# 依次提取result中训练集和测试集数据
train_feature = result[0]
test_feature = result[1]
train_label = result[2]
# TODO 提取测试集的标签test_label
test_label = result[3]

# 输出测试集的标签test_label
print(test_label)