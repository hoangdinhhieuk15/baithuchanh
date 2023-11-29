import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def detect_edges():
    # Yêu cầu người dùng chọn file ảnh
    image_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if image_path:
        # Đọc ảnh từ đường dẫn
        image = cv2.imread(image_path)

        # Chuyển đổi ảnh sang ảnh thang độ xám
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Áp dụng bộ lọc Gaussian để làm mờ ảnh
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Sử dụng thuật toán Canny để phát hiện biên ảnh
        edges = cv2.Canny(blurred, 30, 150)

        # Chuyển đổi ảnh từ OpenCV sang PIL
        edges_pil = Image.fromarray(edges)

        # Chuyển đổi ảnh PIL sang ImageTk
        edges_tk = ImageTk.PhotoImage(edges_pil)

        # Hiển thị ảnh biên trên canvas
        canvas.create_image(0, 0, anchor="nw", image=edges_tk)
        canvas.image = edges_tk

# Tạo cửa sổ tkinter
window = tk.Tk()

# Tạo nút để kích hoạt việc tách biên ảnh
button = tk.Button(window, text="Chọn Ảnh Tách Biên", command=detect_edges)
button.pack(side="top")  

# Tạo canvas để hiển thị ảnh
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Khởi chạy vòng lặp chính của cửa sổ tkinter
window.mainloop()
