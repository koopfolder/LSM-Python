import numpy as np
import matplotlib.pyplot as plt

n = 10  # ดีกรี n (ยกกกำลัง)

# คำนวณโดยใช้สมการเชิงปกติ
def calc(x, y):
    A = np.zeros((n + 1, n + 1))  # เตรียมเมตริกซ์ A ขนาด (n+1) x (n+1) เป็นเมตริกซ์เริ่มต้นที่มีค่าศูนย์
    b = np.zeros((n + 1, 1))  # เตรียมเวกเตอร์ b ขนาด (n+1) x 1 เป็นเวกเตอร์เริ่มต้นที่มีค่าศูนย์

    for i in range(0, n + 1):
        for j in range(0, n + 1):
            A[i][j] = np.sum(x ** (2 * n - i - j))  # คำนวณสมาชิกในเมตริกซ์ A
        b[i] = np.sum(x ** (n - i) * y)  # คำนวณสมาชิกในเวกเตอร์ b

    X = np.dot(np.linalg.inv(A), b)  # แก้ระบบสมการเชิงเส้นโดยใช้การกลับเมตริกซ์และการคูณเมตริกซ์

    return X

# คำนวณค่าคลาดเคลื่อนเฉลี่ยแต่ละรากที่กำหนดไว้
def RMSE_calc(x, y, Y):
    dist = np.zeros([1, len(x)])  # เตรียมเวกเตอร์ dist ขนาด 1 x len(x) เป็นเวกเตอร์เริ่มต้นที่มีค่าศูนย์
    for i in range(n + 1):
        dist += Y[n - i] * (x ** i)  # คำนวณค่าประมาณ y โดยใช้รากใน Y
    dist = np.sum((dist - y) ** 2)  # คำนวณค่าคลาดเคลื่อนเฉลี่ยแบบรากที่สอง
    RMSE = (dist * 1 / len(x)) ** (1 / 2)  # คำนวณค่าคลาดเคลื่อนเฉลี่ยแบบรากที่สอง

    return RMSE

if __name__ == '__main__':
    # โหลดข้อมูลจากไฟล์ 'example5.dat'
    data = np.loadtxt('example5.dat')

    # แยกค่า x และ y จากข้อมูล
    x = data[:, 0]  # เลือกเฉพาะคอลัมน์ที่ 0 เป็นค่า x
    y = data[:, 1]  # เลือกเฉพาะคอลัมน์ที่ 1 เป็นค่า y

    # คำนวณค่าพหุคูณ Y จากข้อมูล x และ y
    Y = calc(x, y)

    # คำนวณค่าคลาดเคลื่อนเฉลี่ยแบบรากที่สอง
    rmse = RMSE_calc(x, y, Y)
    rmse_text = f'RMSE: {rmse:.4f}'

    # พล็อตกราฟ
    x1 = np.arange(-2, 3, 0.1)  # สร้างอาร์เรย์ x1 โดยเริ่มต้นที่ -2 ถึง 3 ด้วยช่วง 0.1
    y1 = 0
    for i in range(0, n + 1):
        y1 += Y[n - i] * x1 ** i  # คำนวณค่า y จากพหุคูณ Y และ x1
    plt.xlim(-2, 3)  # กำหนดขอบเขตแกน x ให้อยู่ในช่วง -2 ถึง 3
    plt.ylim(-5, 3)  # กำหนดขอบเขตแกน y ให้อยู่ในช่วง -5 ถึง 3
    plt.plot(x1, y1, color="red")  # พล็อตกราฟเส้นสีแดง
    plt.scatter(x, y, color="green", marker="+", clip_on=False)  # พล็อตข้อมูลแบบกระจายสีเขียว
    plt.grid()  # เพิ่มเส้นกริดบนกราฟ

    # Title
    plt.title('Scatter Plot of Data')

    # เพิ่มข้อความ RMSE บนกราฟ
    plt.text(0.5, -4, rmse_text, fontsize=12, ha='center', color='blue')

    plt.show()  # แสดงกราฟ
