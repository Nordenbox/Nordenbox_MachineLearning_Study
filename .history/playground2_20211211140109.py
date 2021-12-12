import base64

# 图片的路径
img_path = "img/ask-godiva.jpg"
# 以rb的方式读取图片
with open(img_path, "rb") as file:
    # 读取图片内容
    res = file.read()
    # 图片文件进行base64编码
    img = base64.b64encode(res)
    # 图片转换为字符串
    img = str(img, 'utf-8')