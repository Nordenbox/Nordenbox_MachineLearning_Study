"""极大似然估计的程序。
   生成一个随机黑白小球的序列，找到白球出现的概率，将其封闭。
   然后对封闭小球序列进行抽样。每次抽取一个球，记录白球的次数，然后不断的重复，
   直到这个白球出现的概率等于之前计算的概率，抽样结束，最后我们获得了抽取的次数。
   实际上就是在盲抽取的情况下估算原有白球的个数概率，实际上我们并不需要知道原有
   的序列有多少小球。
"""
import random

balls = ['{}'.format(random.randint(0, 3)) for i in range(1, 100)]
balls_new = []
white_numbers = 0
black_numbers = 0
for i in balls:
    if i == '0':
        i = 'white'
        white_numbers += 1
    else:
        i = 'black'
        black_numbers += 1
    balls_new.append(i)

print(balls_new)
print('black numbers is ', black_numbers)
print('white_numbers is ', white_numbers)
print('Original probability of white balls in all is ',
      white_numbers/len(balls_new))
print('.....................')

pick_value_white = 0
pick_times = 0
stop_pick = True

while stop_pick:
    pick_times += 1
    pick_value = random.choice(balls_new)
    # print(pick_value)
    if pick_value == 'white':
        pick_value_white += 1
    if pick_value_white/pick_times == white_numbers/len(balls_new):
        stop_pick = False
print('Sampling calculating starting')
print('white times is {}, all pick up time is {}, probability of white balls in all is {} '.format(
    pick_value_white, pick_times, (pick_value_white/pick_times)))
print(pick_times)
