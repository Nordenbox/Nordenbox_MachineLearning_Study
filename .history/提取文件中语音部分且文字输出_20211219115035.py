# 使用from...import从moviepy.editor导入VideoFileClip
from moviepy.editor import VideoFileClip

from aip import AipSpeech
APP_ID = '25354259'

API_KEY = 'zwS0ATsCgqik3GBQPNhQ8OjC'

SECRET_KEY = 'VHIipSdOzZmkNsbjD08HP11ZW04bgiOR'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 使用VideoFileClip()加载视频文件
video = VideoFileClip("/Users/nordenbox/Movies/IMG_9354.mov")
# 使用VideoFileClip类中的audio方法获取加载后视频文件的音频
audio = video.audio

# 使用write_audiofile()函数将音频文件写入
audio.write_audiofile("/Users/nordenbox/Movies/IMG_9354.wav")

# 使用from...import从pydub导入AudioSegment
from pydub import AudioSegment

# 使用AudioSegment类中的from_wav()函数读取音频文件
sound = AudioSegment.from_wav("/Users/nordenbox/Movies/IMG_9354.wav")
# 使用set_frame_rate()函数设置采样率为16000
sound = sound.set_frame_rate(16000)
# 使用set_channels()函数设置声道数为1，即单声道
sound = sound.set_channels(1)

# 使用from...import从pydub.silence导入split_on_silence
from pydub.silence import split_on_silence

# 使用split_on_silence()切分音频，并传入参数sound,min_silence_len = 500,silence_thresh = -50
min_silence_len = 500
silence_thresh = -50
pieces = split_on_silence(sound,min_silence_len,silence_thresh)

# 输出pieces查看结果. 对列表的audio_segement.AudioSeagment 对象似乎不能直接用 from_wav 方法
# 要用 export 方法。
# print(pieces)
count = 0
for i in pieces:
    i.export('/Users/nordenbox/Movies/'+str(count)+'.wav',format='wav')
    count += 1
    
# 定义文件读取函数read_file()，传入参数文件地址filePath
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
for i in range(count):##
    wavsample = read_file('/Users/nordenbox/Movies/'+str(i)+".wav")
    # 输出查看wavsample结果
    print(wavsample)
    
for i in range(count):
    # 调用文件读取函数read_file()，读取所有音频片段文件
    wavsample = read_file('/Users/nordenbox/Movies/'+str(i)+".wav")
    # 调用语音识别函数audio2text()，获取语音识别结果
    text = audio2text(wavsample)
    # 输出查看text
    print(text)