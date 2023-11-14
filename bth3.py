import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def hien_thi_hinh_vuong():
    label1.config(text="Cạnh:")
    entry1.pack()
    entry2.pack_forget()
    entry3.pack_forget()

def hien_thi_hinh_chu_nhat():
    label1.config(text="Chiều dài:")
    label2.config(text="Chiều rộng:")
    entry1.pack()
    entry2.pack()
    entry3.pack_forget()

def hien_thi_hinh_tron():
    label1.config(text="Bán kính:")
    entry1.pack()
    entry2.pack_forget()
    entry3.pack_forget()

def ve_hinh():
    shape = shape_selection.get()

    if shape == "Hình vuông":
        if entry1.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập cạnh")
        else:
            canh = float(entry1.get())
            plt.figure()
            plt.gca().add_patch(plt.Rectangle((0, 0), canh, canh, edgecolor='black', fill=None))
            plt.axis('scaled')
            plt.show()

    elif shape == "Hình chữ nhật":
        if entry1.get() == "" or entry2.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập số chiều dài và số chiều rộng")
        else:
            chieu_dai = float(entry1.get())
            chieu_rong = float(entry2.get())
            plt.figure()
            plt.gca().add_patch(plt.Rectangle((0, 0), chieu_dai, chieu_rong, edgecolor='black', fill=None))
            plt.axis('scaled')
            plt.show()

    elif shape == "Hình tròn":
        if entry1.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập bán kính")
        else:
            ban_kinh = float(entry1.get())
            theta = np.linspace(0, 2 * np.pi, 100)
            x = ban_kinh * np.cos(theta)
            y = ban_kinh * np.sin(theta)
            plt.figure()
            plt.gca().plot(x, y, color='black')
            plt.axis('equal')
            plt.show()

def tinh_dien_tich_hinh_vuong():
    canh = float(entry1.get())
    dien_tich = canh ** 2
    return dien_tich

def tinh_chu_vi_hinh_vuong():
    canh = float(entry1.get())
    chu_vi = 4 * canh
    return chu_vi

def tinh_dien_tich_hinh_chu_nhat():
    chieu_dai = float(entry1.get())
    chieu_rong = float(entry2.get())
    dien_tich = chieu_dai * chieu_rong
    return dien_tich

def tinh_chu_vi_hinh_chu_nhat():
    chieu_dai = float(entry1.get())
    chieu_rong = float(entry2.get())
    chu_vi = 2 * (chieu_dai + chieu_rong)
    return chu_vi

def tinh_dien_tich_hinh_tron():
    ban_kinh = float(entry1.get())
    dien_tich = 3.14 * ban_kinh ** 2
    return dien_tich

def tinh_chu_vi_hinh_tron():
    ban_kinh = float(entry1.get())
    chu_vi = 2 * 3.14 * ban_kinh
    return chu_vi

def handle_shape_selection(event):
    shape = shape_selection.get()
    if shape == "Hình vuông":
        hien_thi_hinh_vuong()
    elif shape == "Hình chữ nhật":
        hien_thi_hinh_chu_nhat()
    elif shape == "Hình tròn":
        hien_thi_hinh_tron()

def handle_shape_calculation():
    shape = shape_selection.get()
    try:
        if shape == "Hình vuông":
            if entry1.get() == "":
                messagebox.showerror("Lỗi", "Vui lòng nhập cạnh")
            else:
                dien_tich = tinh_dien_tich_hinh_vuong()
                chu_vi = tinh_chu_vi_hinh_vuong()
                result_label.config(text=f"Diện tích: {dien_tich}, Chu vi: {chu_vi}")
        elif shape == "Hình chữ nhật":
            if entry1.get() == "" or entry2.get() == "":
                messagebox.showerror("Lỗi", "Vui lòng nhập số chiều dài và số chiều rộng")
            else:
                dien_tich = tinh_dien_tich_hinh_chu_nhat()
                chu_vi = tinh_chu_vi_hinh_chu_nhat()
                result_label.config(text=f"Diện tích: {dien_tich}, Chu vi: {chu_vi}")
        elif shape == "Hình tròn":
            if entry1.get() == "":
                messagebox.showerror("Lỗi", "Vui lòng nhập bán kính")
            else:
                dien_tich = tinh_dien_tich_hinh_tron()
                chu_vi = tinh_chu_vi_hinh_tron()
                result_label.config(text=f"Diện tích: {dien_tich}, Chu vi: {chu_vi}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị số hợp lệ")

root = tk.Tk()
root.title("Tính diện tích và chu vi các hình")
root.geometry("400x300")

shape_label = ttk.Label(root, text="Chọn hình:")
shape_label.pack()

shape_selection = ttk.Combobox(root, values=["Hình vuông", "Hình chữ nhật", "Hình tròn"])
shape_selection.bind("<<ComboboxSelected>>", handle_shape_selection)
shape_selection.pack()

label1 = ttk.Label(root)
label1.pack()

label2 = ttk.Label(root)
label2.pack()

entry1 = ttk.Entry(root)
entry1.pack()

entry2 = ttk.Entry(root)
entry2.pack()

entry3 = ttk.Entry(root)
entry3.pack()

calculate_button = ttk.Button(root, text="Tính", command=handle_shape_calculation)
calculate_button.pack()

result_label = ttk.Label(root)
result_label.pack()

draw_button = ttk.Button(root, text="Vẽ", command=ve_hinh)
draw_button.pack()

root.mainloop()
