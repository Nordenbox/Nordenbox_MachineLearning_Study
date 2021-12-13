'''创建客户端'''
# 导入AipFace类
from aip import AipFace
import json
import pprint

APP_ID = '25328314'

API_KEY = 'p3hhOSswrMBtYEgtpYSaQphg'

SECRET_KEY = 'E1raRRhSREebVALnUVi43apuhH0RmEnk'
# 将密钥信息传递给AipFace生成客户端，并将结果存储在client中
client = AipFace(APP_ID, API_KEY, SECRET_KEY)


'''转换图片格式'''
# 导入base64模块
import base64

# 图片的路径
img_path = 'testBeauty.jpg'

# 以rb的方式读取图片
with open(img_path, "rb") as file:
    # 读取图片内容
    res = file.read()

    # 图片文件进行base64编码
    img = base64.b64encode(res)
    # 图片转换为字符串
    img = str(img, 'utf-8')
    
'''获取检测结果'''
# 可选参数
options = {
    # 最多识别的人脸数目
    'max_face_num': 10,
    # 添加要识别的面部属性：返回人脸质量信息
    'face_field': 'quality,age,gender,beauty'}


img_type = "BASE64"

# 带参数调用人脸检测
ret_data = client.detect(img, img_type, options)
pprint.pprint(ret_data)
'''PIL 打开图片'''

# 导入修改修改图片需要的模块
from PIL import Image

# 打开要修改的图片
with Image.open(img_path) as img:
    # 创建一个备份
    img_cp = img.copy()
    
    
'''修改图片标记出人脸'''
# 导入图片修改模块
from PIL import ImageDraw

# 创建画布
draw_img = ImageDraw.Draw(img_cp)


from PIL import ImageFont

# 判断检测是否成功
if ret_data['error_msg'] == 'SUCCESS':
    # 遍历面孔信息列表
    for face_msg in ret_data['result']['face_list']:
        # 获取位置信息
        location = face_msg['location']
        # 获取人脸区域的坐标
        x1 = location['left']
        y1 = location['top']
        x2 = x1 + location['width']
        y2 = y1 + location['height']
        
        
        # 根据脸型设置字体大小
        font_path = '/Library/Fonts/Microsoft/SimHei.ttf'
        font_size = location['height']//6
        font = ImageFont.truetype(font_path, font_size)
        
        # 获取年龄信息
        age = face_msg['age']
        text1 = f'年龄：{age}'
        # 获取性别信息
        gender = face_msg['gender']['type']
        text2 = f'性别：{gender}'
        beauty = face_msg['beauty']
        text5= f'颜值：{beauty}'
        
        # 获取五官遮挡情况
        quality = face_msg['quality']['occlusion']
        
        # 判断鼻子与嘴巴是否被遮挡
        if quality['nose'] > 0.5 and quality['mouth'] == 1:
            color = 'skyblue'
            text3 = '佩戴口罩'
        else:
            color = 'red'
            text3 = '未佩戴口罩'
            
        all_text = [text1, text2, text5,text3]
        
        # 绘制矩形图案
        draw_img.rectangle([x1, y1, x2, y2], outline=color, width=2)
        
        # 按行绘制文字
        for text in all_text:
            # 绘制文字背景
            draw_img.rectangle([x1, y2, x1+font_size * len(text3), y2 + font_size*2], fill='black')
            # 绘制文字内容
            draw_img.text([x1, y2], text, 'white', font)
            # 修改y坐标到下一行，每行间隙为10     
            y2 = y2 + font_size + 1
        
        
    # 存储绘制的结果
    img_cp.save('/Users/nordenbox/Documents/GitHub/NordenboxPython/Nordenbox_MachineLearning_Study/result.jpg')
else:
    print('识别失败')