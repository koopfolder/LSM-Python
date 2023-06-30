import csv
import numpy as np
import matplotlib.pyplot as plt

n=10 # n次式

# 正規方程式を用いた計算
def calc(x, y):
    A = np.zeros((n+1, n+1))
    b = np.zeros((n+1, 1))

    for i in range(0, n+1):
        for j in range(0, n+1):
            A[i][j] = np.sum(x**(2*n-i-j))
        b[i] =  np.sum(x**(n-i)*y)  

    X = np.dot(np.linalg.inv(A), b)

    return X

# 二乗平均平方根誤差の算出
def RMSE_calc(x, y, Y):
    print(Y)
    dist = np.zeros([1, len(x)])
    for i in range(n+1):
        dist += Y[n-i]*(x**i)
    print(dist)
    dist = np.sum((dist-y)**2)
    # print(dist)
    RMSE = (dist* 1/len(x))**(1/2)

    print("RMSE:",RMSE)

if __name__ == '__main__':
    with open('example4.csv') as f:
        reader = csv.reader(f)
        coordinate = np.array([row for row in reader])
    
    coordinate = coordinate.T
    x = np.array([float(i) for i in coordinate[0]])
    y = np.array([float(i) for i in coordinate[1]])
    Y = calc(x, y)
    RMSE_calc(x, y, Y)
    
    x1 = np.arange(-2, 3, 0.1)
    y1 = 0
    for i in range(0, n+1):
        y1 += Y[n-i]*x1**i
    plt.xlim(-2, 3)
    plt.ylim(-5, 3)
    plt.plot(x1, y1, color="red")
    plt.scatter(x, y, color="green", marker="+",clip_on=False)
    plt.grid()
    plt.show()

