from aip import AipSpeech

APP_ID = '25354259'

API_KEY = 'zwS0ATsCgqik3GBQPNhQ8OjC'

SECRET_KEY = 'VHIipSdOzZmkNsbjD08HP11ZW04bgiOR'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 使用from...import从moviepy.editor导入VideoFileClip
from moviepy.editor import VideoFileClip

# 使用VideoFileClip()加载视频文件"大话西游.mp4"
video = VideoFileClip("/Users/yequ/大话西游.mp4")
# 使用VideoFileClip类中的audio属性获取加载后视频文件的音频
audio = video.audio
# 使用write_audiofile()函数将音频文件写入"大话西游.wav"
audio.write_audiofile("/Users/yequ/大话西游.wav")

# 使用from...import从pydub导入AudioSegment
from pydub import AudioSegment

# TODO 使用AudioSegment类中的from_wav()函数读取音频文件"大话西游.wav"
sound = AudioSegment.from_wav("/Users/yequ/大话西游.wav")
# TODO 使用set_frame_rate()函数设置采样率为16000
sound= sound.set_frame_rate(16000)
# TODO 使用set_channels()函数设置声道数为1，即单声道
sound= sound.set_channels(1)