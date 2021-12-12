from aip import AipNlp
''' my APP_ID, APP_KEY, SECRET_KEY'''

APP_ID = '25286241'
API_KEY = 'PxQVtfKht0Zh0LoZSIyUtTfq'
SECRET_KEY = 'SjBChp4MDGVGQfqcl5GplsSdegsysTV1'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
text = '我没有什么观点，买不买都好，但最好还是不要买。'

# 调用sentimentClassify接口，并将结果存储在result里
result = client.sentimentClassify(text)

# 输出结果
print(result)