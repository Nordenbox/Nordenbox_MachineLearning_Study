# 从aip中导入AipNlp
from aip import AipNlp

# 将需要提取摘要的新闻文本传入存储在content中
content = ("麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，"
           "创造了一种聪明的新方式。它允许公司使用更小，更安全的无人机在巨型建筑物中找到之前无法找到的东西。"
           "使用RFID标签更换仓库中的条形码，将帮助提升自动化并提高库存管理的准确性。与条形码不同，RFID标签不需要对准扫描，"
           "标签上包含的信息可以更广泛和更容易地更改。它们也可以很便宜，尽管有优点，但是它具有局限性，"
           "对于跟踪商品没有设定RFID标准，“标签冲突”可能会阻止读卡器同时从多个标签上拾取信号。"
           "扫描RFID标签的方式也会在大型仓库内引起尴尬的问题。固定的RFID阅读器和阅读器天线只能扫描通过设定阈值的标签，"
           "手持式读取器需要人员出去手动扫描物品。几家公司已经解决了无人机读取RFID的技术问题。"
           "配有RFID读卡器的无人机可以代替库存盘点的人物，并以更少的麻烦更快地完成工作。"
           "一个人需要梯子或电梯进入的高箱，可以通过无人机很容易地达到，无人机可以被编程为独立地导航空间，"
           "并且他们比执行大规模的重复任务的准确性和效率要比人类更好。"
           "目前市场上的RFID无人机需要庞大的读卡器才能连接到无人机的本身。这意味着它们必须足够大，"
           "以支持附加硬件的尺寸和重量，使其存在坠机风险。麻省理工学院的新解决方案，"
           "名为Rfly，允许无人机阅读RFID标签，而不用捆绑巨型读卡器。相反，无人机配备了一个微小的继电器，"
           "它像Wi-Fi中继器一样。无人机接收从远程RFID读取器发送的信号，然后转发它读取附近的标签。由于继电器很小，"
           "这意味着可以使用更小巧的无人机，可以使用塑料零件，可以适应较窄的空间，不会造成人身伤害的危险。"
           "麻省理工学院的Rfly系统本质上是对现有技术的一个聪明的补充，它不仅消除了额外的RFID读取器，"
           "而且由于它是一个更轻的解决方案，允许小型无人机与大型无人机做同样的工作。研究团队正在马萨诸塞州的零售商测试该系统。")

# 将新闻标题存储在title中
title = "麻省理工学院为无人机配备RFID技术，进行仓库货物管理"

# 你的 APPID AK SK
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'

# TODO 检查content和title是否超字数
if len(content) > 3000 or len(title) > 200:

    # TODO 如果超字数，输出指定内容
    print('字符串长度过长，请重新编辑。')
    
    
# TODO 生成自然语言处理客户端，并将结果存储在client中
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# TODO 设置摘要结果的最大长度max_summary_len为50
max_summary_len = 50

# TODO 新建一个空字典options
options={}

# TODO 将标题内容title赋值给options["title"]
options['title'] = title

# TODO 调用newsSummary新闻摘要接口
# 依次传入content, max_summary_len=50和options
# 并将返回结果赋值给result
result = client.newsSummary(content,max_summary_len,options)

# TODO 抽取摘要结果result['summary']，并赋值给summary
summary = result['summary']

# 输出摘要结果summary
print(summary)