# TODO 导入jieba模块
import jieba

# TODO 从sklearn.feature_extraction.text中导入CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# 将字符串赋给变量text
text = "深度学习是一种在表达能力上灵活多变，同时又允许计算机不断尝试，直到最终逼近目标的机器学习方法。 它能学习样本数据的内在规律和表示层次，能自动从图像中学习有效的特征。深度学习来源于人工神经网络，之所以叫“深度”是因为它自身由许多不同的层组成。 第一层一般以图像为输入，通过特定的运算从图像中提取特征。接下来，每一层以前一层提取出的特征为输入，对其进行特定形式的变换，便可以得到更复杂一些的特征。经过很多层的变换之后，这种结构就可以组合原始图像中的低层特征形成更加抽象的高层特征。 这种由简单到复杂、由低级到高级的抽象过程，可以通过生活中的例子来体会。 例如，人脸识别。进行人脸识别时，最底层特征是各种类似的轮廓。 越往上，越能提取出物体的一些特征，比如眉毛、眼睛、鼻子等。 到最上层，不同的高级特征组合成相应的图像，就能够区分出不同的人。这个过程就是更高级别的抽象。这种层次化的特征提取过程可以累加，赋予深度学习强大的特征提取能力。 因此，深度学习更有能力发现大数据中隐含的复杂结构。"

# TODO 使用lcut()函数进行分词，并赋值给ret
ret = jieba.lcut(text)

# TODO 创建CountVectorizer对象，设定参数max_features=10，并存储在vect中
vect = CountVectorizer(max_features = 10)

# TODO 将ret中的数据传递给vect，并赋值给变量X
X = vect.fit_transform(ret)

# TODO 使用get_feature_names()函数获取关键词，并将结果赋值给keywords
keywords = vect.get_feature_names()

# TODO 输出keywords
print(keywords)