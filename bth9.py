import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

alpha = 1.5  # Giá trị mặc định của alpha
beta = 0  # Giá trị mặc định của beta

def adjust_contrast(image):
    global alpha, beta
    adjusted_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image

def process_image(img):
    def update_alpha(event):
        global alpha
        alpha = alpha_slider.get()
        update_image()

    def update_beta(event):
        global beta
        beta = beta_slider.get()
        update_image()

    def update_image():
        img_copy = img.copy()
        img_copy = cv.cvtColor(img_copy, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(img_copy)

        v = cv.equalizeHist(v)

        img_contrast = adjust_contrast(v)

        img_merge = cv.merge((h, s, img_contrast))
        img_eq = cv.cvtColor(img_merge, cv.COLOR_HSV2BGR)

        cv.imshow('img_eq', img_eq)

    # Create a tkinter window
    window = tk.Tk()
    window.title("Image Processing")
    window.geometry("400x200")
    window.resizable(False, False)

    # Create alpha slider
    alpha_label = ttk.Label(window, text="Alpha")
    alpha_label.pack()
    alpha_slider = ttk.Scale(window, from_=0.1, to=3.0, length=300, orient=tk.HORIZONTAL, command=update_alpha)
    alpha_slider.set(alpha)
    alpha_slider.pack()

    # Create beta slider
    beta_label = ttk.Label(window, text="Beta")
    beta_label.pack()
    beta_slider = ttk.Scale(window, from_=-100, to=100, length=300, orient=tk.HORIZONTAL, command=update_beta)
    beta_slider.set(beta)
    beta_slider.pack()

    # Display the original image
    cv.imshow('img', img)

    # Run the tkinter event loop
    window.mainloop()

def open_image():
    file_location = filedialog.askopenfilename()
    img = cv.imread(file_location)
    img = cv.resize(img, (640, 480))
    process_image(img)

# Create a tkinter window
root = tk.Tk()
root.title("Image Processing")
root.geometry("200x100")

# Create open button
open_button = ttk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Run the tkinter event loop
root.mainloop()
