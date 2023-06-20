import numpy as np
import matplotlib.pyplot as plt

n = 10

def calc(x,y):
    A = np.zeros((n+1, n+1))
    B = np.zeros((n+1,1))

    for i in range(0, n+1):
        for j in  range(0, n+1):
            A[i][j] = np.sum(x ** (2 * n-i-j))
        B[i] = np.sum(x ** (n - i) * y)

    X = np.dot(np.linalg.inv(A),B)

    return X

def RSME_calc(x, y, Y):
    dist = np.zeros([1, len(x)])
    for i in range(n+1):
        dist += Y[n-i]*(x**i)
    dist = np.sum((dist - y) ** 2)
    RMSE = (dist * 1 / len(x)) ** (1/2)

    return RMSE

if __name__ == '__main__':
    data = np.loadtxt('example5.dat')

    x = data[:,0]
    y = data[:,1]

    Y = calc(x,y)

    rmse = RSME_calc(x, y, Y)
    rmse_text = f'RMSE:{rmse:.4f}'

    x1 = np.arange(-2, 3, 0.1)
    y1 = 0
    for i in range(0, n+1):
        y1 += Y[n - i] * x1 ** i
    plt.xlim(-2, 3)
    plt.ylim(-5, 3)
    plt.plot(x1, y1, color="red")
    plt.scatter(x, y, color="green", marker="+", clip_on=False)
    plt.grid()

    plt.title('Scatter Plot of Data')

    plt.text(0.5, -4, rmse_text, fontsize=12, ha="center", color="blue")

    plt.show() 