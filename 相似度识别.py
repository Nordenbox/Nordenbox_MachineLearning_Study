''' 图片载入'''
# 载入base64模块
import base64

# TODO 构造用于载入和进行base64编码的函数load_base64：输入为图片地址，输出为图片编码后转换的字符串
def load_base64(img_path):
    # TODO 使用with...as以rb方式，打开路径为img_path的图片并赋值给file
    with open(img_path,'rb') as file:
        # TODO 使用read()读取图片内容file，赋值给res
        res = file.read()
        # TODO 使用base64.b64encode()对图片文件res进行base64编码
        image_64 = base64.b64encode(res)
        # TODO 使用str()函数将图片img转换为字符串,以utf-8的格式存储在img变量中
        img = str(image_64,'utf-8')
        # TODO 返回img
        return img


# 使用构造的函数载入图片‘/yequ/match1.png’,命名为img1
img1 = load_base64('/yequ/match1.png')
# 使用构造的函数载入图片‘/yequ/match2.png’,命名为img2
img2 = load_base64('/yequ/match2.png')

'''相似度检测'''
# 导入AipFace类
from aip import AipFace
import base64
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'

# 将密钥信息传递给AipFace生成客户端，并将结果存储在client中 
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# TODO 使用match()函数计算图片img1、img2相似度，image_type设置为BASE64，将检测结果命名为result

result = client.match([{'image':img1,'image_type':'BASE64'},
                      {'image':img2,'image_type':'BASE64'}])


# TODO 从result返回值中获取result字典中的相似度得分score，并命名为score
score = result['result']['score']

'''在图片上展示相似度得分'''
#导入图片模块
from PIL import Image
# 导入图片修改模块
from PIL import ImageDraw
#导入字体模块
from PIL import ImageFont

# TODO 通过with...as使用Image模块中的open函数打开要修改的图片'/yequ/matchAll.png'赋值给img
with Image.open('/yequ/matchAll.png') as img:
    # TODO 对img使用copy()函数，创建一个备份img_cp
    img_cp = img.copy()

# TODO 使用ImageDraw模块中Draw函数在备份img_cp中创建画布draw_img
draw_img = ImageDraw.Draw(img_cp)

#设置字体
font_type = '/yequ/yahei_consola.ttf'
font_size = 35
# TODO 对ImageFont使用truetype()函数创建字体font，样式设置为font_type，大小设置为font_size
font = ImageFont.truetype(font_type,font_size)
#设置文字位置
text_location = [10, 420]
# TODO 对draw_img绘制文字: 位于text_location,内容使用格式化输出f'相似度为{score}'、颜色设置为'black'、字体为font
draw_img.text(text_location,f'相似度为{score}','black',font)
# TODO img_cp存储绘制的结果为'/yequ/all_draw.png'
img_cp.save('/yequ/all_draw.png')