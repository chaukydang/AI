import math
import random
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from TSP_Solver import TSPSolver

# Tạo giao diện WinForms
root = tk.Tk()
root.title("TSP Solver")

# Tạo tọa độ ngẫu nhiên cho các vị trí
num_locations = 6
x_coordinates = [random.uniform(0, 10) for _ in range(num_locations)]
y_coordinates = [random.uniform(0, 10) for _ in range(num_locations)]

# Tạo khoảng cách giữa các vị trí
locations = []
for i in range(num_locations):
    row = []
    for j in range(num_locations):
        distance = np.sqrt((x_coordinates[i] - x_coordinates[j]) ** 2 + (y_coordinates[i] - y_coordinates[j]) ** 2)
        row.append(distance)
    locations.append(row)

# Create the TSP solver instance
solver = TSPSolver(locations)

# Function xử lý nút solve
def solve_tsp():
    start = combo_box.current()
    path, distance = solver.solve_tsp(start)
    best_path = [i + 1 for i in path]
    result_label.config(text=f"Best path: {best_path}\nBest distance: {distance:.2f}")
    plot_graph(path)

# Tạo khung cho bản đồ 
frame_map = ttk.Frame(root)
frame_map.pack(pady=10)

# Tạo khung cho các lệnh điều khiển
frame_controls = ttk.Frame(frame_map)
frame_controls.pack(pady=10, padx=10, anchor="w")

# Tạo một label cho điểm bắt đầu
lbl_start_text = ttk.Label(frame_controls, text="Choose a starting point:")
lbl_start_text.grid(row=0, column=0, padx=5, sticky="E")

# Tạo Combobox để chọn vị trí bắt đầu
combo_box = ttk.Combobox(root, values=[f"Location {i+1}" for i in range(num_locations)])
combo_box.pack()

# Tạo nút Solve
solve_button = tk.Button(root, text="Solve", command=solve_tsp)
solve_button.pack()

# Tạo label để hiển thị kết quả
result_label = tk.Label(root)
result_label.pack()

# Tạo hình và trục cho đồ thị
fig, ax = plt.subplots(figsize=(6, 6))

# Tạo canvas để hiển thị biểu đồ
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Hàm vẽ đồ thị
def plot_graph(path):
    ax.clear()

    # Vẽ các vị trí dưới dạng điểm
    scatter = ax.scatter(x_coordinates, y_coordinates, c='red', s=50)

    # Vẽ đường dẫn dưới dạng các đường có dấu mũi tên
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i+1]
        ax.annotate("", xy=(x_coordinates[end], y_coordinates[end]), xytext=(x_coordinates[start], y_coordinates[start]),
                    arrowprops=dict(arrowstyle="->", color="blue"))

    # Kết nối tất cả các điểm với các đường đi
    for i in range(num_locations):
        for j in range(i + 1, num_locations):
            x_start = x_coordinates[i]
            y_start = y_coordinates[i]
            x_end = x_coordinates[j]
            y_end = y_coordinates[j]
            distance = locations[i][j]
            place_names = [f"Location {k + 1}" for k in range(num_locations)]
            ax.plot([x_start, x_end], [y_start, y_end], 'k--', alpha=0.2)
            ax.text((x_start + x_end) / 2, (y_start + y_end) / 2, f"{distance:.2f}", ha='center', va='center')
            if j == num_locations - 1:
                ax.text(x_end, y_end, place_names[j], ha='left', va='bottom')
            ax.text(x_coordinates[i], y_coordinates[i], place_names[i], ha='right', va='top')


    # Đặt màu khác cho điểm bắt đầu đã chọn
    if path:
        start_index = path[0]
        scatter.set_facecolors(['green' if i == start_index else 'red' for i in range(num_locations)])

    # Refresh lại biểu đồ
    plt.tight_layout()
    canvas.draw()


# Đồ thị ban đầu của đồ thị
plot_graph([])

# Bắt đầu vòng lặp WinForms
root.mainloop()