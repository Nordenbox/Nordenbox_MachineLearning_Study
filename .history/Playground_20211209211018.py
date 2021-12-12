# TODO 导入os模块

import os
# TODO 导入shutil模块
import shutil

# 将文件所在路径"/yequ/photo"赋值给变量allImgPath
allImgPath = "photo"

# TODO 使用os.listdir()函数获取该路径下所有的文件，并赋值给变量Items
Items = os.listdir(allImgPath)

# TODO 使用for循环遍历Items
for i in Items:

    # TODO 使用if语句判断若文件为非图片文件
    if i[0]=='.' or '.' not in i:

        # TODO 则跳过
        continue

    # TODO 拼接图片路径
    classPath = allImgPath+i

    # TODO 使用split()函数以"_"分隔文件名，并赋值给变量result
    result = '_'.split(classPath)

    # TODO 读取result中第1个元素，并赋值给变量root
    root = result[0]

    # TODO 使用os.path.join()函数拼接文件路径，并赋值给变量targetPath
    targetPath = os.path.join(allImgPath,root)

    # TODO 使用os.path.exists()函数判断如果不存在目标文件夹
    if not os.path.exists(targetPath):

        # TODO 则使用os.mkdir()函数创建对应文件夹
        os.mkdir(targetPath)

    # TODO 使用shutil.move()函数将图片移动到对应的文件夹中
    shutil.move(classPath,targetPath)

# TODO 使用os.listdir()函数遍历文件夹allImgPath，并赋值给变量updateItems
updateItems = os.listdir(allImgPath)

# TODO 输出变量updateItems
print(updateItems)