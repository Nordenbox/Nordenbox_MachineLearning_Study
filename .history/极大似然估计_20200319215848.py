"""极大似然估计的程序。
   生成一个随机黑白小球的序列，找到白球出现的概率，将其封闭。
   然后对封闭小球序列进行抽样。每次抽取一个球，记录白球的次数，然后不断的重复，
   直到这个白球出现的概率等于之前计算的概率，抽样结束，最后我们获得了抽取的次数。
   实际上就是在盲抽取的情况下估算原有白球的个数概率，实际上我们并不需要知道原有
   的序列有多少小球。
"""
import random

def rendering_original_balls_set(ball_numbers = 1000):
    balls = ['{}'.format(random.randint(0, 3)) for i in range(1, ball_numbers)] # create a random balls set
    balls_new = []
    white_ball_numbers = 0
    black_ball_numbers = 0
    for i in balls:
        if i == '0':  # 按照 0 和 1 的不同，替换成黑与白
            i = 'white'
            white_ball_numbers += 1
        else:
            i = 'black'
            black_ball_numbers += 1
        balls_new.append(i)

    print(balls_new)
    print('black ball numbers is ', black_ball_numbers)
    print('white_ball_numbers is ', white_ball_numbers)
    print('Original probability of white balls in all is ',
        white_ball_numbers/len(balls_new))
    print('.....................')

    return balls_new


pick_value_white = 0
pick_times = 0
stop_pick = True



while stop_pick:
    pick_times += 1
    pick_value = random.choice(rendering_original_balls_set(ball_numbers = 1000))   # 每次在新的球的序列中提取一个小球
    # print(pick_value)
    if pick_value == 'white': # 如果是白球，记录一次白球的个数
        pick_value_white += 1
    if pick_value_white/pick_times == white_ball_numbers/len(balls_new):
        stop_pick = False   #如果白球的次数和总次数的概率等于原始设定概率，无限循环停止。
print('Sampling calculating starting')
print('white times is {}, all pick up time is {}, probability of white balls in all is {} '.format(
    pick_value_white, pick_times, (pick_value_white/pick_times)))

