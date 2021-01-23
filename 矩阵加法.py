import numpy as np

test1 = np.array([[1, -2, 3],
                  [2, 3, -4],
                  [-3, 4, 5]])  # 给定一个数组

test2 = np.array([[5, 6, 7],
                  [33, -19, 23],
                  [1, 33, -90]])


def native_add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape # 断言两个矩阵石头等秩

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j] # 对应位置元素相加

    return x


print(native_add(test1, test2))