"""Графические задачи на Tkinter."""

import random
import tkinter as tk


def _window(title: str, width: int = 700, height: int = 500) -> tuple[tk.Tk, tk.Canvas]:
    root = tk.Tk()
    root.title(title)
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack(fill="both", expand=True)
    return root, canvas


def draw_square(size: int = 200) -> None:
    root, canvas = _window("Квадрат")
    x1, y1 = 120, 120
    canvas.create_rectangle(x1, y1, x1 + size, y1 + size, outline="blue", width=3)
    root.mainloop()


def draw_triangle_in_circle(radius: int) -> None:
    root, canvas = _window("Треугольник в круге")
    cx, cy = 350, 240
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="black", width=2)

    p1 = (cx, cy - radius)
    p2 = (cx - radius * 0.866, cy + radius / 2)
    p3 = (cx + radius * 0.866, cy + radius / 2)
    canvas.create_polygon(*p1, *p2, *p3, outline="red", fill="", width=2)
    root.mainloop()


def overlay_circle_on_triangle(radius: int) -> None:
    root, canvas = _window("Круг на треугольнике")
    cx, cy = 350, 240
    p1 = (cx, cy - radius)
    p2 = (cx - radius * 0.866, cy + radius / 2)
    p3 = (cx + radius * 0.866, cy + radius / 2)
    vertices = [p1, p2, p3]

    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="gray", width=2)
    canvas.create_polygon(*p1, *p2, *p3, outline="darkgreen", fill="", width=2)

    small_r = radius // 4
    vx, vy = random.choice(vertices)
    canvas.create_oval(vx - small_r, vy - small_r, vx + small_r, vy + small_r, outline="blue", width=2)
    root.mainloop()


def draw_histogram(vector: list[int]) -> None:
    root, canvas = _window("Гистограмма")
    if not vector:
        canvas.create_text(350, 240, text="Пустой вектор")
        root.mainloop()
        return

    max_v = max(vector)
    bar_w = max(20, 500 // len(vector))
    x = 60
    for value in vector:
        h = 0 if max_v == 0 else int((value / max_v) * 300)
        canvas.create_rectangle(x, 420 - h, x + bar_w, 420, fill="skyblue")
        canvas.create_text(x + bar_w // 2, 435, text=str(value))
        x += bar_w + 10
    root.mainloop()


def show_matrix_min_max(matrix: list[list[int]]) -> None:
    root = tk.Tk()
    root.title("Матрица min/max")
    all_values = [x for row in matrix for x in row]
    min_v, max_v = min(all_values), max(all_values)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            color = "white"
            if value == min_v:
                color = "lightgreen"
            if value == max_v:
                color = "lightcoral"
            tk.Label(root, text=str(value), width=6, height=2, bg=color, relief="ridge").grid(
                row=i, column=j, padx=1, pady=1
            )
    root.mainloop()


def color_rows_by_index_plus_value(matrix: list[list[int]], value: int) -> None:
    root = tk.Tk()
    root.title("Цвет строк")
    colors = ["#fde2e4", "#fad2e1", "#e2ece9", "#bee1e6", "#cddafd", "#f0efeb"]

    for i, row in enumerate(matrix):
        color = colors[(i + value) % len(colors)]
        for j, item in enumerate(row):
            tk.Label(root, text=str(item), width=6, height=2, bg=color, relief="solid").grid(row=i, column=j)
    root.mainloop()


def color_columns_reverse_by_first_element(matrix: list[list[int]]) -> None:
    root = tk.Tk()
    root.title("Цвет столбцов")
    colors = ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff", "#bdb2ff"]
    first = matrix[0][0]
    cols = len(matrix[0])

    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            idx = (len(colors) - 1 - j - first) % len(colors)
            tk.Label(root, text=str(item), width=6, height=2, bg=colors[idx], relief="solid").grid(row=i, column=j)
    root.mainloop()


def show_sorted_matrix_with_gradient(matrix: list[list[int]]) -> None:
    root = tk.Tk()
    root.title("Градиент по диагонали")
    n = min(len(matrix), len(matrix[0]))
    diag = [matrix[i][i] for i in range(n)]

    min_d = min(diag)
    max_d = max(diag)

    def color_by_value(v: int) -> str:
        if max_d == min_d:
            ratio = 0.5
        else:
            ratio = (v - min_d) / (max_d - min_d)
        r = int(255 * ratio)
        b = int(255 * (1 - ratio))
        return f"#{r:02x}88{b:02x}"

    for i, row in enumerate(matrix):
        color = color_by_value(matrix[i][i] if i < n else min_d)
        for j, item in enumerate(row):
            tk.Label(root, text=str(item), width=6, height=2, bg=color, relief="solid").grid(row=i, column=j)
    root.mainloop()
