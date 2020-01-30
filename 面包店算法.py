# 每个线程的号码
import threading
import time

number = [0 for _ in range(5)]
# print(number)
# 是否需要号码
entering = [False for _ in range(5)]


# print(entering)

# 获取到资源，这里输出并且沉睡1秒
def achieve_resource(num):
    print('Now is no.{} thread achieve the resource'.format(num))
    time.sleep(1)


def lock(num):
    # 标记未领取号码
    entering[num] = True
    # 领取的号码是当前等待的线程中最大的号码+1
    number[num] = max(number) + 1
    # 标记领取完成
    entering[num] = False
    # 遍历其他线程的号码
    for i in range(5):
        # 如果还有线程没有领取号码，等待
        while entering[i]:
            pass
        # 如果还有线程号码比自己小，等它先抢占
        # 如果两个线程号码相同，线程id小的优先
        while ((number[i] != 0) and (number[num], num) < (number[i], i)):
            pass


# 抢占完毕之后，销毁号码
def unlock(num):
    number[num] = 0


def start_request(num):
    while True:
        lock(num)
        achieve_resource(num)
        unlock(num)


if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=start_request, args=(i,))
        t.start()

