import tkinter as tk
from sympy import *
from sympy.plotting import plot

def calculate_derivative():
    expression = entry.get()
    if 'x' not in expression:
        result_label.config(text="Chú ý: Biểu thức chỉ nhập biến x")
        return

    x = symbols('x')
    f = sympify(expression)
    df = diff(f, x)
    result_label.config(text="Đạo hàm của hàm số f(x): " + str(df))
    plot_graph(f, df)

def calculate_integral():
    expression = entry.get()
    if 'x' not in expression:
        result_label.config(text="Chú ý: Biểu thức chỉ nhập biến x")
        return

    x = symbols('x')
    f = sympify(expression)
    integral = integrate(f, x)
    df = diff(f, x)
    result_label.config(text="Tích phân của hàm số f(x): " + str(integral))
    plot_graph(f, df)

def calculate_limit():
    expression = entry.get()
    if 'x' not in expression:
        result_label.config(text="Chú ý: Biểu thức chỉ nhập biến x")
        return

    x, a = symbols('x a')
    f = sympify(expression)
    limit_val = limit(f, x, a)
    df = diff(f, x)
    result_label.config(text="Giới hạn của hàm số f(x) khi x tiến đến a: " + str(limit_val))
    plot_graph(f, df)

def plot_graph(f, df=None):
    x = symbols('x')
    p = plot(f, df, show=False)
    p.title = "Biểu đồ hàm số"
    p.xlabel = "x"
    p.ylabel = "f(x)"
    p.show()

window = tk.Tk()
window.title("Phần mềm Giải tích")
window.geometry("400x250")

expression_label = tk.Label(window, text="Nhập biểu thức toán học:")
expression_label.pack()

entry = tk.Entry(window)
entry.pack()

calculate_derivative_button = tk.Button(window, text="Tính đạo hàm", command=calculate_derivative)
calculate_derivative_button.pack()

calculate_integral_button = tk.Button(window, text="Tính tích phân", command=calculate_integral)
calculate_integral_button.pack()

calculate_limit_button = tk.Button(window, text="Tính giới hạn", command=calculate_limit)
calculate_limit_button.pack()



result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
