'''1.读取并处理数据'''

# 导入csv模块
import csv
# 使用open()函数打开数据集
file = open('lipstickComments.csv',"r")
# 使用csv.reader()函数读取数据集
reader = csv.reader(file)
# 创建一个空列表comments
comments = []
# 使用for循环遍历reader，将遍历的数据存储到变量info中
for info in reader:
    # 使用append()函数，将info逐一添加到comments列表中
    comments.append(info[0])


'''2.调用接口'''

# 从aip中导入AipNlp
from aip import AipNlp

# 你的 APPID AK SK
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'

# TODO 生成自然语言处理客户端，并将结果存储在client中
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# TODO 定义一个整型result，初始化为0，用于记录正向评论的数量
result = 0

# TODO 使用for循环遍历每条评论
for i in comments:
    
    # TODO 调用sentimentClassify接口，并将结果存储在comm_result中
    comm_result=client.sentimentClassify(i)
    
    # TODO 获取评论的情感极性分类结果，并将结果储存在senti_result中
    ret= comm_result['items'][0]
    senti_result = ret['sentiment']
    # TODO 使用if语句判断评论是否为正向
    if senti_result > 0:
    
        # TODO 如果是正向，result加1
        result +=1
        
# TODO 计算正向情感比例，储存在变量ratio中
ratio = result/len(comments)

# TODO 输出比例ratio
print(ratio)