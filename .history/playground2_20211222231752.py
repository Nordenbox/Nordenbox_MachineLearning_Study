import base64
import os
import shutil
from aip import AipFace
import json
import pprint
import math

#图片分类

from aip import AipImageClassify

APP_ID = '25318522'
API_KEY = 'w07MZbos3TN8IiN7FZWNBDDO'
SECRET_KEY = '4M9YrNcuHc6yLdgU2svq282C5EOX0RlO'
# 新建一个AipImageClassify，并赋值给变量client
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

imgroot = '/Users/nordenbox/Documents/GitHub/NordenboxPython/Nordenbox_MachineLearning_Study/yequ/photo'
imglist = os.listdir(imgroot)

# 拿到图片文件夹内部所有图片的路径（不是文件名）
for image_name in imglist:
    if image_name[0] == '.' or '.' not in image_name:
        continue

    filePath = imgroot + '/' + image_name

    with open(filePath, 'rb') as f:
        each_image = f.read()

    classifyResult = client.advancedGeneral(each_image)

    if 'result' in classifyResult:
        value = classifyResult['result'][0].get('root', '未分类')
        image_label = value.split('-')[0]
        folderPath = imgroot + '/' + image_label

        if not os.path.exists(folderPath):
            os.mkdir(folderPath)

        finalPath = shutil.move(filePath, folderPath)
        print(f'已经移动到：{finalPath}')

# 人脸识别和口罩检测

from aip import AipFace
APP_ID = '25328314'

API_KEY = 'p3hhOSswrMBtYEgtpYSaQphg'

SECRET_KEY = 'E1raRRhSREebVALnUVi43apuhH0RmEnk'
# 将密钥信息传递给AipFace生成客户端，并将结果存储在client中
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

