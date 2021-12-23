'''读取图片'''
filePath = 'zuoye.jpg' 
# TODO 使用with...as以rb方式，打开路径为filePath的图片并赋值给f
with open(filePath,'rb') as f:

    # TODO 使用read()读取f，赋值给变量image
    image = f.read()
    
    
'''调用通用文字识别接口'''
# 从aip中导入AipOcr
from aip import AipOcr
# 你的 APPID AK SK
APP_ID = '25341900'

API_KEY = 'ToGQ5jzESTEtRCBWaCGd4IPZ'

SECRET_KEY = '7PYRyKzrOkmg1ckq1yB6ByBTy7DaaHOV'
# TODO 新建一个AipOcr，并赋值给变量client
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

# TODO 创建字典options，并将可选参数detect_direction的值设置"true"
options = {'detect_direction':'true'}

# TODO 调用通用文字识别接口并把结果赋值给result
result = client.basicAccurate(image,options)

'''处理文字识别后的结果'''
# TODO 创建一个空字符串text
text = ''

# TODO 使用for循环遍历识别后的文本内容
for word in result['words_result'][0]['words']:
    

    # TODO 将内容添加到text中
    text.join(word)

'''调用文本纠错识别'''
# TODO 从aip中导入AipNlp
from aip import AipNlp

# 你的 APPID AK SK
APP_ID = '25341900'

API_KEY = 'ToGQ5jzESTEtRCBWaCGd4IPZ'

SECRET_KEY = '7PYRyKzrOkmg1ckq1yB6ByBTy7DaaHOV'
# TODO 新建一个AipNlp，并赋值给变量client2
client2 = AipNlp(APP_ID,API_KEY,SECRET_KEY)

# TODO 调用ecnet()函数，并将结果赋给true_result
true_result = client2.ecnet(text)
print(true_result)


