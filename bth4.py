import tkinter as tk
from tkinter import Text, Button, Label, Scrollbar
import pandas as pd
from numpy import array
import numpy as np
import matplotlib.pyplot as plt

in_data = None  # Khởi tạo biến in_data ở mức biến toàn cục

# Hàm tính toán thống kê
def calculate_statistics():
    global in_data
    df = pd.read_csv('diemPython.csv', index_col=0, header=0)
    in_data = array(df.iloc[:, :])

    result = "Tong so sinh vien tham gia mon hoc: {}\n".format(np.sum(in_data[:, 1]))
    result += 'Tong sinh vien dat diem A: {}\n'.format(np.sum(in_data[:, 3]))
    result += 'Tong sinh vien dat diem B+: {}\n'.format(np.sum(in_data[:, 4]))
    result += 'Tong sinh vien dat diem B: {}\n'.format(np.sum(in_data[:, 5]))
    result += 'Tong sinh vien dat diem C+: {}\n'.format(np.sum(in_data[:, 6]))
    result += 'Tong sinh vien dat diem C: {}\n'.format(np.sum(in_data[:, 7]))
    result += 'Tong sinh vien dat diem D+: {}\n'.format(np.sum(in_data[:, 8]))
    result += 'Tong sinh vien dat diem D: {}\n'.format(np.sum(in_data[:, 9]))
    result += 'Tong sinh vien dat diem F: {}\n'.format(np.sum(in_data[:, 10]))

    maxx = 0
    minn = 9999999
    lopp = lopmin = 0
    for i in range(0, 9):
        sum1 = 0
        for j in range(3, 10):
            sum1 += np.sum(in_data[i, j])
        if sum1 >= maxx:
            maxx = sum1
            lopp = in_data[i, 0]
        if sum1 <= minn:
            minn = sum1
            lopmin = in_data[i, 0]
        result += "Lop {}: {}\n".format(in_data[i, 0], sum1)

    result += "Lop {} co nhieu sinh vien duoc diem >= D nhieu nhat voi {} sinh vien\n".format(lopp, maxx)
    result += "Lop {} co it sinh vien duoc diem >= D nhieu nhat voi {} sinh vien\n".format(lopmin, minn)

    diemL1 = np.sum(in_data[:, 11])
    diemL2 = np.sum(in_data[:, 12])

    if diemL1 > diemL2:
        result += "Co nhieu sinh vien qua L1 hon L2\n"
    elif diemL1 < diemL2:
        result += "Co nhieu sinh vien qua L2 hon L1\n"
    else:
        result += "So sinh vien qua L1 va L2 la nhu nhau\n"

    display_result(result)

# Hàm hiển thị kết quả trong vùng văn bản
def display_result(result):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Hàm hiển thị biểu đồ
def display_graphs():
    global in_data
    diemA = in_data[:, 3]
    diemBc = in_data[:, 4]
    diemB = in_data[:, 5]
    diemCc = in_data[:, 6]
    diemC = in_data[:, 7]
    diemDc = in_data[:, 8]
    diemD = in_data[:, 9]
    diemF = in_data[:, 10]

    plt.figure(figsize=(10, 6))

    # Biểu đồ cột
    plt.subplot(2, 1, 1)
    plt.bar(range(len(diemA)), diemA, label="Diem A")
    plt.bar(range(len(diemBc)), diemBc, label="Diem B+")
    plt.bar(range(len(diemB)), diemB, label="Diem B")
    plt.bar(range(len(diemCc)), diemCc, label="Diem C+")
    plt.bar(range(len(diemC)), diemC, label="Diem C")
   

    plt.bar(range(len(diemDc)), diemDc, label="Diem D+")
    plt.bar(range(len(diemD)), diemD, label="Diem D")
    plt.bar(range(len(diemF)), diemF, label="Diem F")
    plt.xlabel("Lop")
    plt.ylabel("So sinh vien")
    plt.title("Biểu đồ điểm theo lớp")
    plt.legend()

    # Biểu đồ đường
    plt.subplot(2, 1, 2)
    plt.plot(range(len(diemA)), diemA, label="Diem A")
    plt.plot(range(len(diemBc)), diemBc, label="Diem B+")
    plt.plot(range(len(diemB)), diemB, label="Diem B")
    plt.plot(range(len(diemCc)), diemCc, label="Diem C+")
    plt.plot(range(len(diemC)), diemC, label="Diem C")
    plt.plot(range(len(diemDc)), diemDc, label="Diem D+")
    plt.plot(range(len(diemD)), diemD, label="Diem D")
    plt.plot(range(len(diemF)), diemF, label="Diem F")
    plt.xlabel("Lop")
    plt.ylabel("So sinh vien")
    plt.title("Biểu đồ điểm theo lớp")
    plt.legend()

    plt.tight_layout()
    plt.show()

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Phân tích điểm Python")

# Vùng văn bản chứa kết quả
result_text = Text(root, height=15, width=50)
result_text.pack()

# Nút tính toán thống kê
calculate_button = Button(root, text="Tính toán thống kê", command=calculate_statistics)
calculate_button.pack()

# Nút hiển thị biểu đồ
display_graphs_button = Button(root, text="Hiển thị biểu đồ", command=display_graphs)
display_graphs_button.pack()

# Thanh cuộn cho vùng văn bản
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

root.mainloop()
