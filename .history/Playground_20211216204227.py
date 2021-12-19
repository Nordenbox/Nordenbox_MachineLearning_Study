# 使用from...import从moviepy.editor导入VideoFileClip
from moviepy.editor import VideoFileClip
# 将视频存储地址"/yequ/西游记.mp4"赋值给变量filePath
filePath = "/Users/nordenbox/Movies/09112021_190414.mp4"
# 将单声道音频保存地址"/yequ/西游记1.wav"赋值给变量targetPath1
targetPath1 = "/Users/nordenbox/Movies/09112021_190414_1.wav"
# 将多声道音频保存地址"/yequ/西游记2.wav"赋值给变量targetPath2
targetPath2 = "/Users/nordenbox/Movies/09112021_190414_2.wav"
# 使用VideoFileClip()加载视频文件"西游记.mp4"，并赋值给变量video
video = VideoFileClip(filePath)
# 使用VideoFileClip类中的audio属性获取加载后视频文件的音频，并赋值给变量audio
audio = video.audio
# 使用write_audiofile()函数将音频文件写入targetPath1和targetPath2
audio.write_audiofile(targetPath1)
audio.write_audiofile(targetPath2)

# TODO 使用from...import从pydub导入AudioSegment
from pydub import AudioSegment

# TODO 使用AudioSegment类中的from_wav()函数读取音频文件"/yequ/西游记1.wav"，赋值给sound1
sound1 = AudioSegment.from_wav("/Users/nordenbox/Movies/09112021_190414_1.wav")
# TODO 对sound1使用set_frame_rate()函数设置采样率为16000
sound1 = sound1.set_frame_rate(16000)
# TODO 对sound1使用set_channels()函数设置声道数为1，即单声道
sound1 = sound1.set_channels(1)
# TODO 对sound1使用export()函数保存修改后的音频文件，格式为wav
sound1.export(sound1,format='wav')

# 使用AudioSegment类中的from_wav()函数读取音频文件"/yequ/西游记2.wav"，赋值给sound2
sound2 = AudioSegment.from_wav(targetPath2)
# 对sound2使用set_frame_rate()函数设置采样率为32000
sound2 = sound2.set_frame_rate(32000)
# 对sound2使用set_channels()函数设置声道数为2，即多声道
sound2 = sound2.set_channels(2)
# 对sound2使用export()函数保存修改后的音频文件
sound2.export(targetPath2,format="wav")