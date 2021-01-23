import time
def mad(n):
    n = 3.4*n*(1-n)
    print(n, '\n')
    time.sleep(0.2)
    mad(n)



mad(0.1)