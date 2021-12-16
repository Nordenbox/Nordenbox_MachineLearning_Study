'''创建客户端'''
# 导入AipFace类
from aip import AipFace
import json
import pprint
import math

APP_ID = '25328314'

API_KEY = 'p3hhOSswrMBtYEgtpYSaQphg'

SECRET_KEY = 'E1raRRhSREebVALnUVi43apuhH0RmEnk'
# 将密钥信息传递给AipFace生成客户端，并将结果存储在client中
client = AipFace(APP_ID, API_KEY, SECRET_KEY)


'''转换图片格式'''
# 导入base64模块
import base64

# 图片的路径
img_path = 'emma.jpg'

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
    # 添加要识别的面部属性：返回年龄和颜值
    'face_field': 'age,beauty'}


img_type = "BASE64"

# 带参数调用人脸检测
ret_data = client.detect(img, img_type, options)
#print(ret_data)

'''PIL 打开图片'''

# TODO 导入修改修改图片需要的模块
from PIL import Image

# TODO 打开要修改的图片
with Image.open(img_path) as f:
    # TODO 创建一个备份im_cp
    img_cp = f.copy()
    
'''修改图片标记出人脸'''
# TODO 导入图片修改模块
from PIL import ImageDraw

# TODO 使用img_cp创建画布
draw_img = ImageDraw.Draw(img_cp)

# TODO 导入字体模块
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
        # TODO 字体的路径为'yequ/yahei_consola.ttf'
        font_path = '/Library/Fonts/Microsoft/SimHei.ttf'
        # TODO 字体的大小为脸部高度的1/4
        font_size = location['height']//8
        # TODO 创建字体对象font
        font = ImageFont.truetype(font_path,font_size)
        
        # 获取年龄信息
        age = face_msg['age']
        # TODO 将年龄信息格式化保存为'年龄：{age}'
        text1 = f'年龄：{age}'
        # 获取外貌信息
        beauty = face_msg['beauty']
        # TODO 将颜值信息格式化保存为'美貌：{beauty}'
        text2 = f'美貌：{beauty}'
        
        # 获取旋转角度
        yaw = face_msg['angle']['yaw']
        # TODO 如果角度在(-20,20)之内，text3设置为"正对镜头"，color设置为'lightgreen'
        if yaw > -20 and yaw < 20:
            text3 = "正对镜头"
            color = 'lightgreen'
        # TODO 否则，设置为"没有正对镜头"和'LightBlue'
        else:
            text3 = "没有正对镜头"
            color = 'LightBlue'
        

            
        all_text = [text1, text2, text3]
        
        # TODO 绘制矩形图案,边框颜色为color，宽度为2
        draw_img.rectangle([x1,y1,x2,y2],outline=color,width=2)
        
        # TODO 按行绘制文字
        for text in all_text:
            # TODO 绘制文字背景
            draw_img.rectangle([x1, y1, x2+0.5*font_size*len(text3), y1-font_size*2],fill=color)
            
            # TODO 绘制文字内容
            draw_img.text([x1,y1-font_size*2],text,'white',font)
            # TODO 修改y坐标到下一行    
            y1 = y1-font_size-12
        
    # 存储绘制的结果
    img_cp.save('/Users/nordenbox/Documents/GitHub/NordenboxPython/Nordenbox_MachineLearning_Study/result.jpg')
    
else:
    print('识别失败')