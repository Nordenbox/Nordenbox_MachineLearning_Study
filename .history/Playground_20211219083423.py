# 使用from...import从moviepy.editor导入VideoFileClip
from moviepy.editor import VideoFileClip

# 使用VideoFileClip()加载视频文件"大话西游.mp4"
video = VideoFileClip("/Users/nordenbox/Movies/ChinaS2Trailer.mov")
# 使用VideoFileClip类中的audio方法获取加载后视频文件的音频
audio = video.audio

# 使用write_audiofile()函数将音频文件写入"大话西游.wav"
audio.write_audiofile("/Users/nordenbox/Movies/ChinaS2Trailer.wav")

# 使用from...import从pydub导入AudioSegment
from pydub import AudioSegment

# 使用AudioSegment类中的from_wav()函数读取音频文件"大话西游.wav"
sound = AudioSegment.from_wav("/Users/nordenbox/Movies/ChinaS2Trailer.wav")
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

# 输出pieces查看结果
print(pieces)