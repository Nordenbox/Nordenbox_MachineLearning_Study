def AND(x1, x2, w1, w2, theta):
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


w1 = float(input('input number for w1 \n输入权重 w1：'))
w2 = float(input('input number for w2\n输入权重 w2：'))
theta = float(input('input the theta\n输入阈值: '))
print('-----------------------')
print('权重w1,w2 为%f和%f' % (w1, w2), '阈值为: ', theta)
print('逻辑电路 x1*%f + x1*%f = %f 需要输入参数x1和x2：' % (w1, w2, theta))
print('------------------')

x1 = int(input('input 0 or 1 for X1\n 输入 X1的数值，0 或者 1: '))
x2 = int(input('input 0 or 1 for X2\n 输入 X2的数值，0 或者 1: '))
res = AND(x1, x2, w1, w2, theta)

print('-------------\n输入的 X1 和 X2 分别是%d|%d' % (x1, x2), '\n输出为： ', res)

if (x1 * x2 == 0 and x1 + x2 != 0) and res == 1:
    print('这是一个或门电路。')
else:
    print('这是一个与门电路。')
