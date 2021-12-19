# 使用from...import从moviepy.editor导入VideoFileClip，用来做文件的声画分离
from moviepy.editor import VideoFileClip

from aip import AipSpeech  # 导入百度的语音识别模块。（必须先安装在本地）

# 设定登录百度智能云的用户名密码。
APP_ID = '25354259'
API_KEY = 'zwS0ATsCgqik3GBQPNhQ8OjC'
SECRET_KEY = 'VHIipSdOzZmkNsbjD08HP11ZW04bgiOR'

# 设定一个变量，继承和使用 AipSpeech 这个类。
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 使用VideoFileClip()加载视频文件。 video 这个变量继承和使用 VideoFileClip 这个类。类的参数为一个路径。
video = VideoFileClip("/Users/nordenbox/Movies/IMG_9354.mov")  # 
# 使用VideoFileClip类中的audio方法获取加载后视频文件的音频（声画分离），结果存储在 audio 中。
# 这里的 audio 是一个moviepy.audio.io.AudioFileClip.AudioFileClip类型的数据。
audio = video.audio

# 使用write_audiofile()函数将音频文件写入。这里 audio 的类型没有变化。
audio.write_audiofile("/Users/nordenbox/Movies/IMG_9354.wav")

# 使用from...import从pydub（模块）导入AudioSegment（类）
from pydub import AudioSegment

# 使用AudioSegment类中的from_wav()方法读取音频文件.
sound = AudioSegment.from_wav("/Users/nordenbox/Movies/IMG_9354.wav")
# 这里的 sound 的数据类型是pydub.audio_segment.AudioSegment

# 使用set_frame_rate()函数设置采样率为16000
sound = sound.set_frame_rate(16000)
# 使用set_channels()函数设置声道数为1，即单声道
sound = sound.set_channels(1)

# 使用from...import从pydub.silence导入split_on_silence
# 目的即将已经获取的音频信号中的语音切分成一个个分离的碎片（pieces）
from pydub.silence import split_on_silence

# 使用split_on_silence()切分音频，并传入参数sound,min_silence_len = 500,silence_thresh = -50
# min_silence_len：最小的无声时间。就是超过多少毫秒没有语音，就可以做切割点。
# silence_thresh：低于多少分贝的声音即可以算作静音，也可以做切割的依据。
min_silence_len = 500
silence_thresh = -50
pieces = split_on_silence(sound,min_silence_len,silence_thresh)

# 输出pieces查看结果. 对列表的audio_segement.AudioSeagment 对象似乎不能直接用 from_wav 方法
# 要用 export 方法。
# print(pieces)
# 在目标文件夹内写入多个音频文件（即已经分离好的语音碎片，等同于句子）
count = 0
for i in pieces:
    i.export('/Users/nordenbox/Movies/'+str(count)+'.wav',format='wav')
    count += 1
    
# 定义文件读取函数read_file()，传入参数文件地址filePath。目击即读取语音碎片文件然后输出成一个
def read_file(filePath):
    # 使用 with...as 配合open函数以rb 方式，打开路径为filePath的音频
    with open(filePath,"rb") as fp:
        # 使用read()函数读取音频赋值给wavsample
        wavsample = fp.read()
        # 返回音频对象
        return wavsample
    
def audio2text(wav):
    # 调用短语音识别接口把结果赋值给rejson变量
    rejson = client.asr(wav,"wav",16000,{"dev_pid": 1537})
    # if—else语句判定
    # 若错误码为0，则得到语音识别结果
    if rejson["err_no"] == 0:
        # 获取语音识别结果
        # TODO 从返回结果中提取出参数result中的唯一值并赋值给变量msg
        msg = rejson['result'][0]
    # 否则给出"语音识别错误！"提示
    else:
        msg = "语音识别错误！"
    # TODO 返回语音识别结果msg
    return msg

# 通过for循环批量读取切分完的音频文件

    
for i in range(count):
    # 调用文件读取函数read_file()，读取所有音频片段文件
    wavsample = read_file('/Users/nordenbox/Movies/'+str(i)+".wav")
    # 调用语音识别函数audio2text()，获取语音识别结果
    text = audio2text(wavsample)
    # 输出查看text
    print(text)