import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = None
label_cs2 = None
label2_cs2 = None
in_data = None
choice_var = None
choice_var2 = None
headers = None
headers2 = None

# Hàm kiểm tra và hiển thị nội dung file Excel
def load_excel_content():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])  # Chọn file CSV
    if file_path:
        try:
            # Đọc file Excel
            df = pd.read_csv(file_path)
            display_excel_content(df)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi đọc file Excel: {str(e)}")

# Hàm tính tổng số sinh viên đạt theo từng chuẩn
def tong():
    global in_data, label_cs2, choice_var, headers
    headers_list = list(headers)
    value1 = choice_var.get()
    n1 = headers_list.index(value1)
    tong = in_data[:, n1 + 2]
    tong_sv = np.sum(tong)
    label_cs2.config(text=f"{tong_sv}")

# Hàm tính phần trăm số sinh viên đạt theo từng chuẩn
def phantram():
    global in_data, label2_cs2, choice_var2, headers2
    headers_list2 = list(headers2)
    value2 = choice_var2.get()
    n2 = headers_list2.index(value2)
    tong2 = in_data[:, n2 + 3]
    tong_sv2 = np.sum(tong2)
    sosv = in_data[:, 2]
    tongsosv = np.sum(sosv)
    tong_sv2 = int(tong_sv2)
    tongsosv = int(tongsosv)

    phantram = float((tong_sv2 / tongsosv) * 100)
    label2_cs2.config(text=f"{phantram}")

# Hàm vẽ biểu đồ
def dothi():
    global in_data, choice_var, headers
    diemA = in_data[:, 4]
    diemB = in_data[:, 7]
    diemC = in_data[:, 9]
    diemD = in_data[:, 11]
    diemF = in_data[:, 12]
    MaLop = in_data[:, 2]

    plt.bar(MaLop, diemA)

    plt.xlabel('Lơp')
    plt.ylabel(' Số sv đạt điểm A ')
    plt.legend(loc='upper right')
    plt.show()

# Hàm hiển thị nội dung file Excel trong cửa sổ thứ hai
def display_excel_content(data_frame):
    global df, in_data, label_cs2, label2_cs2, choice_var, choice_var2, headers, headers2
    # Tạo cửa sổ thứ hai
    second_window = tk.Toplevel(cs, width=1310, height=800)
    second_window.title("Nội dung file Excel")
    in_data = np.array(df.iloc[:, :])
    headers = df.columns[2:]
    headers2 = df.columns[3:]
    text_widget = tk.Text(second_window, width=160)  # Đặt kích thước width và height tại đây
    text_widget.place(x=10, y=10)  # Sử dụng grid để đặt text_widget
    # Hiển thị nội dung từ DataFrame vào Text widget
    text_widget.insert(tk.END, data_frame.to_string())
    choice_var = tk.StringVar(second_window)
    choice_var2 = tk.StringVar(second_window)
    choice_menu = tk.OptionMenu(second_window, choice_var, *headers)
    choice_menu.place(x=400, y=420)
    choice_menu2 = tk.OptionMenu(second_window, choice_var2, *headers2)
    choice_menu2.place(x=400, y=450)

    button_cs2 = tk.Button(second_window, text="Tổng số sinh viên đạt theo từng chuẩn", command=tong)
    button_cs2.place(x=400, y=480)

    label_cs2 = tk.Label(second_window, text="")
    label_cs2.place(x=650, y=480)

    button2_cs2 = tk.Button(second_window, text="Phần trăm số sinh viên đạt theo từng chuẩn", command=phantram)
    button2_cs2.place(x=400, y=510)

    label2_cs2 = tk.Label(second_window, text="")
    label2_cs2.place(x=700, y=510)

    button_dothi = tk.Button(second_window, text="Vẽ biểu đồ", command=dothi)
    button_dothi.place(x=400, y=540)

    second_window.mainloop()

# Tạo cửa sổ giao diện
cs = tk.Tk()
cs.title("Phần mềm thống kê")
cs.resizable(False, False)

main_frame = tk.Frame(cs)
main_frame.pack()

label_cs1 = tk.Label(main_frame, text="Chọn file Excel (CSV)")
label_cs1.grid(row=0, column=0, padx=10, pady=10)

button_cs1 = tk.Button(main_frame, text="Chọn file", command=load_excel_content)
button_cs1.grid(row=0, column=1, padx=10, pady=10)

cs.mainloop()
