
from aip import AipOcr


APP_ID = '25341900'

API_KEY = 'ToGQ5jzESTEtRCBWaCGd4IPZ'

SECRET_KEY = '7PYRyKzrOkmg1ckq1yB6ByBTy7DaaHOV'
# 将密钥信息传递给AipFace生成客户端，并将结果存储在client中
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 1. 读取图像文件
# 将照片路径'/Users/ocr/test.png'赋值给变量filePath
filePath = '/Users/nordenbox/Pictures/石桐保险经纪证件02.jpeg' 
# 使用with...as以rb方式，打开路径为filePath的图片并赋值给f
with open(filePath, 'rb') as f:
    # 使用read()读取f，赋值给变量image
    image = f.read()
# 3. 调用通用文字识别
# 如果有可选参数 
# 创建字典options，并将可选参数detect_direction的值设置为"true"
options = {"detect_direction":"true"}
# 调用通用文字识别接口并把结果赋值给result
result = client.basicAccurate(image, options)

# 4. 提取返回结果
# 从返回结果中提取出参数words_result的值并赋值给变量ending
ending = result['words_result']
# 使用for循环遍历列表ending中的每一个元素
for word in ending:
    # 提取参数'words'中的文字信息
    text = word['words']
    # 5. 写入文件
    # 使用with...as以a方式，打开路径为test.txt的文件并赋值给fp
    with open("test.txt","a") as fp:
        # TODO 使用write()将文字信息text换行写入fp
        fp.write(text+'\n')   
 # 使用print()输出"写入完成"       
print("写入完成")