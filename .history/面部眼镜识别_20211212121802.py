# 为了机构化显示复杂的数据
import json
import pprint

# 导入AipFace类
from aip import AipFace

# 将AppID'10252021'赋值给变量APP_ID
APP_ID = '25328314'
# 将API Key'ZHe7788sh11GEjIAdEKeY'赋值给变量API_KEY
API_KEY = 'p3hhOSswrMBtYEgtpYSaQphg'
# 将Secret Key'JMMzHe7788BUSH1ZhEnM1YUEhh'赋值给变量SECRET_KEY
SECRET_KEY = 'E1raRRhSREebVALnUVi43apuhH0RmEnk'
# 将密钥信息传递给AipFace生成客户端，并将结果存储在client中
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 导入base64模块
import base64

# 图片的路径
img_path = "/Users/nordenbox/Pictures/kimuraCollections.jpg"

# 以rb的方式读取图片
with open(img_path, "rb") as file:
    # 读取图片内容
    res = file.read()
    # 图片文件进行base64编码
    img = base64.b64encode(res)
    # 图片转换为字符串
    img = str(img, 'utf-8')
# TODO 可选参数options，添加要识别的面部属性：glasses
options = {'max_face_num': 10,'face_field':'age,quality,glasses'}

# TODO 设定图片类型为base64类型
img_type = 'BASE64'

# TODO 带参数调用人脸检测
ret_data = client.detect(img,img_type,options)
# 用结构化的表现方式打印出数据结果，看起来一目了然。
#pprint.pprint(ret_data)
print(json.dumps(ret_data,indent=4))


# TODO 使用if语句判断检测是否成功：错误信息是否为SUCCESS
if ret_data['error_msg'] == 'SUCCESS':
    
    # 人脸的数目
    face_num = int(ret_data['result']['face_num'])
    # TODO 若检测成功，将眼镜信息赋值给变量glasses
    glasses = ret_data['result']['face_list'][0]['glasses']
    # TODO 将眼镜信息中的type数据值，赋值给变量glasses_type
    glasses_type = glasses['type']
    # TODO 将眼镜信息中的probability数据值，赋值给变量glasses_pro
    glasses_pro = glasses['probability']
    
    print(f'There are {face_num} prople.')
    # TODO 使用if语句判断，如果glasses_type的值为"sun"
    if glasses_type == 'sun':
        # TODO 格式化输出眼镜类型为墨镜
        print(f"图片中的人有百分之{glasses_pro*100}的可能戴了墨镜")
    # TODO 如果glasses_type的值为"common"
    elif glasses_type == 'common':
        # 格式化输出眼镜类型为普通眼镜
        print(f"图片中的人有百分之{glasses_pro*100}的可能戴了普通眼镜")
    # TODO 如果glasses_type的值为"none"
    elif glasses_type == 'none':
        # 格式化输出没有眼镜
        print(f"图片中的人有百分之{glasses_pro*100}的可能没有戴眼镜")
# 否则输出检测失败
else:
    print('检测失败！')