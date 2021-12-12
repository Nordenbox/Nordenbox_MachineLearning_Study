from aip import AipNlp
''' my APP_ID, APP_KEY, SECRET_KEY'''

APP_ID = '25286241'
API_KEY = 'PxQVtfKht0Zh0LoZSIyUtTfq'
SECRET_KEY = 'SjBChp4MDGVGQfqcl5GplsSdegsysTV1'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
text = '其实这个世界上没什么事情是必须完全接受的，比如电视机。'

# 调用sentimentClassify接口，并将结果存储在result里
result = client.sentimentClassify(text)

# 输出结果
print(result)