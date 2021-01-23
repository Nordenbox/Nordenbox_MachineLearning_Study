import time
def mad(n):
    n = 2.6*n*(1-n)
    print(n, '\n')
    time.sleep(0.5)
    mad(n)



mad(0.3)