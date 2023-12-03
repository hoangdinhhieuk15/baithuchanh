
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

# Định nghĩa hàm Tich_chap() để lọc Trung bình, Trung bình có trọng số và lọc Gaussian

def Tich_chap(img, mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = img[i-1, j-1] * mask[0, 0] \
                   + img[i-1, j] * mask[0, 1] \
                   + img[i-1, j + 1] * mask[0, 2] \
                   + img[i, j-1] * mask[1, 0] \
                   + img[i, j] * mask[1, 1] \
                   + img[i, j + 1] * mask[1, 2] \
                   + img[i + 1, j-1] * mask[2, 0] \
                   + img[i + 1, j] * mask[2, 1] \
                   + img[i + 1, j + 1] * mask[2, 2]
            img_new[i, j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new

# Định nghĩa hàm lọc trung vị
def loc_trung_vi(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img[i - 1, j - 1],
                    img[i - 1, j],
                    img[i - 1, j + 1],
                    img[i, j - 1],
                    img[i, j],
                    img[i, j + 1],
                    img[i + 1, j - 1],
                    img[i + 1, j],
                    img[i + 1, j + 1]]

            temp = sorted(temp)
            img_new[i, j] = temp[4]
    return img_new

def process_image():
    # Chọn ảnh từ tệp
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        # Đọc ảnh gốc
        image = cv2.imread(file_path, 0)

        # Lọc trung vị
        imgTV_3x3 = loc_trung_vi(image)

        # Hiển thị ảnh gốc và ảnh lọc trung vị
        fig = plt.figure(figsize=(10, 8))
        (ax1), (ax2) = fig.subplots(1, 2)
        ax1.imshow(image, cmap='gray')
        ax1.set_title("Ảnh gốc")
        ax2.imshow(imgTV_3x3, cmap='gray')
        ax2.set_title("Ảnh làm mịn")

        # Hiển thị vùng vẽ
        plt.show()


# Tạo cửa sổ Tkinter
window = tk.Tk()
window.title("Ứng dụng xử lý ảnh")

# Tạo một khung để hiển thị ảnh
image_frame = tk.Frame(window)
image_frame.pack()

# Hiển thị ảnh trong khung
image_label = tk.Label(image_frame)
image_label.pack()



# Tạo nút "Xử lý ảnh"
process_button = tk.Button(window, text="Chọn ảnh để xử lý", command=process_image)
process_button.pack()
