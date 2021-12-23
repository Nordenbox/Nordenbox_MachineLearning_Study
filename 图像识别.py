import base64
# 1.读取所有文件
# 使用import导入os模块
import os
# 将存储照片的文件夹路径'img'赋值给变量imgroot
imgroot = 'img' 
# 使用os.listdir()函数获取该路径下所有的照片的名字，并赋值给变量imglist
imglist = os.listdir(imgroot)
# 注意，这里拿到的不是路径！！！！！

# 从aip中导入AipImageClassify
from aip import AipImageClassify
# 将AppID"10252021"赋值给变量APP_ID
APP_ID = '25318522'
API_KEY = 'w07MZbos3TN8IiN7FZWNBDDO'
SECRET_KEY = '4M9YrNcuHc6yLdgU2svq282C5EOX0RlO'
# 新建一个AipImageClassify，并赋值给变量client
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# 遍历目录下的所有文件名
for imgname in imglist:
    # 使用if判断筛除非图像文件
    if imgname[0] == '.' or '.' not in imgname:
        # 如果符合if判断条件，跳出本次循环，进入下一次循环
        continue
    # 组合图像文件路径
    filePath = imgroot + '/' + imgname
    
    # 使用with...as以rb方式，打开路径为filePath的图片并赋值给f
    with open(filePath, 'rb') as f:
       
        #self.body['image'] = "data:image/jpg;base64," + str(base64_data, 'utf-8')
        # 使用read()读取f，赋值给变量image
        image = f.read()
    
    # 2.调用通用物体识别
    # 调用通用物体识别接口并把结果赋值给ending
    ending = client.advancedGeneral(image)
    
    # 3.提取分类结果
    # 判断是否识别成功
    if "result" in ending: 
        # 从第一个结果中提取出图像分类并赋值给变量value
        # 若没有找到root信息，则分为“未分类“目录
        value = ending['result'][0].get('root', '未分类')
        # 只取分类结果value的上层标签并赋值给变量label
        label=value.split("-")[0]
        # 字符串拼接变量imgroot、"/"、变量label并将结果赋值给变量targetPath
        targetPath = imgroot + '/' + label
    
        # 4.对应分类文件夹还未创建时，创建文件夹   
        # 如果目标文件夹不存在
        if not os.path.exists(targetPath):
            # 如果是
            # 使用os.mkdir()函数创建文件夹
            os.mkdir(targetPath)
        
        # 5.移动图像到对应文件夹   
        # TODO 导入shutil模块
        import shutil
        # TODO 使用shutil.move()函数移动文件，将图像移动到目标文件夹中
        # 将结果赋值给变量newPath
        newPath = shutil.move(filePath,targetPath)
        # TODO 使用格式化输出“已经移动到：{newPath}”
        print(f"已经移动到：{newPath}")
    
