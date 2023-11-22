import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Hàm xử lý sự kiện khi người dùng nhấn nút "Áp dụng bộ lọc"
def apply_filter():
    low_cutoff_freq = float(low_cutoff_entry.get())
    high_cutoff_freq = float(high_cutoff_entry.get())
    filter_order = 51
    bandpass_filter = signal.firwin(filter_order, [low_cutoff_freq, high_cutoff_freq], fs=1000, pass_zero=False)
    filtered_bandpass = signal.lfilter(bandpass_filter, 1, x)

    # Biến đổi Fourier của tín hiệu đã lọc
    fft_freq = np.fft.fftfreq(len(filtered_bandpass), d=t[1]-t[0])
    fft_signal = np.fft.fft(filtered_bandpass)

    # Cập nhật đồ thị
    ax2.clear()
    ax2.plot(t, filtered_bandpass)
    ax2.set_title('Bộ lọc thông qua dải tần')
    ax2.set_xlabel('Thời gian')
    ax2.set_ylabel('Amplitude')

    ax3.clear()
    ax3.plot(fft_freq, np.abs(fft_signal))
    ax3.set_title('Phổ tần số')
    ax3.set_xlabel('Tần số (Hz)')
    ax3.set_ylabel('Biên độ')

    canvas.draw()

# Hàm xử lý sự kiện khi người dùng nhấn nút "Cập nhật tín hiệu"
def update_signal():
    global t, x
    signal_type = signal_type_var.get()

    if signal_type == 'Sine':
        frequency = float(signal_frequency_entry.get())
        x = np.sin(2 * np.pi * frequency * t)
    elif signal_type == 'Square':
        frequency = float(signal_frequency_entry.get())
        duty_cycle = float(signal_duty_cycle_entry.get())
        x = signal.square(2 * np.pi * frequency * t, duty=duty_cycle)
    elif signal_type == 'Triangle':
        frequency = float(signal_frequency_entry.get())
        x = signal.sawtooth(2 * np.pi * frequency * t, width=0.5)
    else:
        x = np.zeros_like(t)

    # Cập nhật đồ thị
    ax1.clear()
    ax1.plot(t, x)
    ax1.set_title('Tín hiệu đầu vào')
    ax1.set_xlabel('Thời gian')
    ax1.set_ylabel('Amplitude')

    canvas.draw()

# Tạo giao diện
root = tk.Tk()
root.title('Ứng dụng Bộ lọc thông qua dải tần')

# Tạo khung vẽ đồ thị
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Tạo tín hiệu đầu vào
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

# Vẽ đồ thị gốc
ax1.plot(t, x)
ax1.set_title('Tín hiệu đầu vào')
ax1.set_xlabel('Thời gian')
ax1.set_ylabel('Amplitude')

# Tạo các thành phần giao diện cho tín hiệu đầu vào
signal_frame = tk.Frame(root)
signal_frame.pack(pady=10)

signal_type_label = tk.Label(signal_frame, text='Loại tín hiệu:')
signal_type_label.grid(row=0, column=0)
signal_type_var = tk.StringVar()
signal_type_dropdown = tk.OptionMenu(signal_frame, signal_type_var, 'Sine', 'Square', 'Triangle')
signal_type_dropdown.grid(row=0, column=1)

signal_frequency_label = tk.Label(signal_frame, text='Tần số(HZ):')
signal_frequency_label.grid(row=1, column=0)
signal_frequency_entry = tk.Entry(signal_frame)
signal_frequency_entry.grid(row=1, column=1)

signal_duty_cycle_label = tk.Label(signal_frame, text='Chu kỳ :')
signal_duty_cycle_label.grid(row=2, column=0)
signal_duty_cycle_entry = tk.Entry(signal_frame)
signal_duty_cycle_entry.grid(row=2, column=1)

update_button = tk.Button(signal_frame, text='Cập nhật tín hiệu', command=update_signal)
update_button.grid(row=3, column=0, columnspan=2, pady=10)

# Tạo các thành phần giao diện cho bộ lọc thông qua dải tần
filter_frame = tk.Frame(root)
filter_frame.pack(pady=10)

low_cutoff_label = tk.Label(filter_frame, text='Tần số cắt thấp:')
low_cutoff_label.grid(row=0, column=0)
low_cutoff_entry = tk.Entry(filter_frame)
low_cutoff_entry.grid(row=0, column=1)

high_cutoff_label = tk.Label(filter_frame, text='Tần số cắt cao:')
high_cutoff_label.grid(row=1, column=0)
high_cutoff_entry = tk.Entry(filter_frame)
high_cutoff_entry.grid(row=1, column=1)

apply_button = tk.Button(filter_frame, text='Áp dụng bộ lọc', command=apply_filter)
apply_button.grid(row=2, column=0, columnspan=2, pady=10)

# Hiển thị giao diện
root.mainloop()
