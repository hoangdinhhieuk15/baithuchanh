import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

entries_A = []
entries_b = []
result_labels = []

def giai_he_phuong_trinh():
    # Lấy dữ liệu từ các ô nhập liệu
    A = []
    b = []
    try:
        for i in range(len(entries_A)):
            row = []
            for j in range(len(entries_A[0])):
                entry = entries_A[i][j]
                value = float(entry.get())
                row.append(value)
            A.append(row)

            entry = entries_b[i]
            value = float(entry.get())
            b.append(value)

        # Giải hệ phương trình tuyến tính
        x = np.linalg.solve(A, b)

        # Xóa các hiển thị kết quả cũ (nếu có)
        for label in result_labels:
            label.destroy()

        result_labels.clear()

        # Hiển thị kết quả
        result_frame = tk.Frame(frame)
        result_frame.pack(side=tk.LEFT)

        for i in range(len(x)):
            result_label = tk.Label(result_frame, text=f'x{i+1} = {x[i]}')
            result_label.pack()
            result_labels.append(result_label)

        # Vẽ biểu đồ
        plt.plot(x)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Biểu đồ giá trị của x')
        plt.show()
    except ValueError:
        error_label = tk.Label(frame, text="Lỗi: Vui lòng nhập số.")
        error_label.pack()
        result_labels.append(error_label)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính")

# Tạo thanh cuộn
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Tạo canvas để chứa nội dung và kết nối thanh cuộn với canvas
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH)

# Thiết lập thanh cuộn để hoạt động với canvas
scrollbar.config(command=canvas.yview)

# Tạo khung chứa nội dung của canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Tạo ô nhập liệu cho số phương trình và số ẩn
n_label = tk.Label(frame, text="Số phương trình và số ẩn:")
n_label.pack()
n_entry = tk.Entry(frame)
n_entry.pack()

# Tạo nút "Xác nhận" để nhập dữ liệu
confirm_button = tk.Button(frame, text="Xác nhận", command=lambda: create_input_fields())
confirm_button.pack()

# Hàm tạo các ô nhập liệu cho ma trận A và vectơ b dựa trên số phương trình và số ẩn
def create_input_fields():
    global entries_A, entries_b, result_labels
    n = int(n_entry.get())

    # Xóa các widget cũ (nếu có)
    for widget in frame.winfo_children():
        widget.destroy()

    result_labels.clear()

    # Tạo khung chứa ô nhập liệu cho ma trận A
    input_frame = tk.Frame(frame)
    input_frame.pack(side=tk.LEFT)

    # Tạo các ô nhập liệu cho ma trận A
    entries_A = []
    for i in range(n):
        row = []
        for j in range(n):
            label = tk.Label(input_frame, text=f"A{i+1}{j+1}:")
            label.pack()
            entry = tk.Entry(input_frame)
            entry.pack()
            row.append(entry)
        entries_A.append(row)

    # Tạo khung chứa ô nhập liệu cho vectơ b
    input_frame_b = tk.Frame(frame)
    input_frame_b.pack(side=tk.LEFT)

    # Tạo các ô nhập liệu cho vectơ b
    entries_b = []
    for i in range(n):
        label = tk.Label(input_frame_b, text=f"X{i+1}:")
        label.pack()
        entry = tk.Entry(input_frame_b)
        entry.pack()
        entries_b.append(entry)

    # Tạo nút "Giải" để thực hiện tính toán
    solve_button = tk.Button(frame, text="Giải", command=lambda: giai_he_phuong_trinh())
    solve_button.pack()

    # Cập nhật kích thước của canvas khi có sự thay đổi nội dung
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Khởi chạy ứng dụng
root.mainloop()
