# 导入csv模块
import csv

# 使用open()函数打开数据集
file = open("TVComments.csv", "r")
# 使用csv.reader()函数读取数据集
reader = csv.reader(file)
# 创建一个空列表data
data = []
# 使用for循环遍历reader，将遍历的数据存储到变量info中
for info in reader:
    # 使用append()函数，将info逐一添加到data列表中
    data.append(info)
    
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

# TODO 对vect对象使用get_feature_names()，并将结果赋值给keywords
keywords = vect.get_feature_names()

# 输出keywords
print(keywords)
print(X)