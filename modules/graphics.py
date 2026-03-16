"""Модуль графики на Tkinter."""

import tkinter as tk


def _create_window(title: str, width: int = 500, height: int = 500) -> tuple[tk.Tk, tk.Canvas]:
    """Вспомогательная функция для создания окна и холста."""
    root = tk.Tk()
    root.title(title)
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()
    return root, canvas


def draw_square(size: int = 200) -> None:
    """Нарисовать квадрат."""
    root, canvas = _create_window("Квадрат")
    x1, y1 = 150, 150
    x2, y2 = x1 + size, y1 + size
    canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=3)
    root.mainloop()


def draw_triangle_in_circle(radius: int = 150) -> None:
    """Вписать треугольник в круг."""
    root, canvas = _create_window("Треугольник в круге")
    cx, cy = 250, 250
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="green", width=3)

    p1 = (cx, cy - radius)
    p2 = (cx - radius * 0.866, cy + radius / 2)
    p3 = (cx + radius * 0.866, cy + radius / 2)
    canvas.create_polygon(*p1, *p2, *p3, outline="red", fill="", width=3)
    root.mainloop()


def draw_circle_on_triangle() -> None:
    """Наложить круг на треугольник."""
    root, canvas = _create_window("Круг и треугольник")
    triangle_points = (250, 100, 100, 400, 400, 400)
    canvas.create_polygon(*triangle_points, outline="purple", fill="", width=3)
    canvas.create_oval(130, 130, 370, 370, outline="orange", width=3)
    root.mainloop()


def draw_histogram(vector: list[int]) -> None:
    """Построить простую гистограмму по вектору."""
    root = tk.Tk()
    root.title("Гистограмма")

    width, height = 700, 450
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    if not vector:
        canvas.create_text(width // 2, height // 2, text="Вектор пуст")
        root.mainloop()
        return

    max_value = max(vector)
    bar_width = max(30, (width - 100) // len(vector))
    x = 50

    for value in vector:
        bar_height = 0 if max_value == 0 else int((value / max_value) * 300)
        canvas.create_rectangle(x, 380 - bar_height, x + bar_width, 380, fill="skyblue", outline="black")
        canvas.create_text(x + bar_width / 2, 395, text=str(value))
        x += bar_width + 10

    root.mainloop()


def show_matrix_with_min_max(matrix: list[list[int]]) -> None:
    """Вывести матрицу и выделить минимум и максимум цветом."""
    root = tk.Tk()
    root.title("Матрица: min и max")

    all_values = [value for row in matrix for value in row]
    min_value = min(all_values)
    max_value = max(all_values)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            color = "white"
            if value == min_value:
                color = "lightgreen"
            if value == max_value:
                color = "lightcoral"
            label = tk.Label(root, text=str(value), width=6, height=2, bg=color, relief="solid")
            label.grid(row=i, column=j, padx=2, pady=2)

    root.mainloop()
