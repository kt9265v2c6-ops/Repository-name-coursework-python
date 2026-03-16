"""Функции для работы с матрицами."""


from typing import Iterable


def create_matrix_from_vectors(vectors: list[list[int]]) -> list[list[int]]:
    """Создать матрицу из списка векторов (строк)."""
    return [row[:] for row in vectors]


def read_matrix_from_file(filename: str) -> list[list[int]]:
    """Считать матрицу из текстового файла."""
    matrix: list[list[int]] = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                matrix.append([int(x) for x in line.split()])
    return matrix


def write_matrix_to_file(filename: str, matrix: list[list[int]]) -> None:
    """Записать матрицу в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for row in matrix:
            file.write(" ".join(str(x) for x in row) + "\n")


def print_matrix(matrix: list[list[int]]) -> None:
    """Красивый вывод матрицы."""
    for row in matrix:
        print(" ".join(f"{x:5d}" for x in row))


def remove_column_by_index_from_file(matrix: list[list[int]], index_filename: str) -> list[list[int]]:
    """Удалить столбец по индексу, который хранится в файле."""
    with open(index_filename, "r", encoding="utf-8") as file:
        col = int(file.read().strip())
    return [[value for j, value in enumerate(row) if j != col] for row in matrix]


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Транспонировать матрицу."""
    return [list(row) for row in zip(*matrix)]


def remove_main_diagonal_one_loop(matrix: list[list[int]]) -> list[list[int]]:
    """Удалить элементы главной диагонали одним циклом по строкам."""
    result = [row[:] for row in matrix]
    for i, row in enumerate(result):
        if i < len(row):
            row.pop(i)
    return result


def replace_column(matrix: list[list[int]], source_matrix: list[list[int]], target_col: int, source_col: int) -> list[list[int]]:
    """Заменить столбец target_col матрицы столбцом source_col из другой матрицы."""
    result = [row[:] for row in matrix]
    rows = min(len(result), len(source_matrix))
    for i in range(rows):
        result[i][target_col] = source_matrix[i][source_col]
    return result


def zero_row_or_column_by_divisibility_rule(matrix: list[list[int]], k: int) -> list[list[int]]:
    """Найти элемент, кратный k, и занулить строку/столбец по условию следующего элемента."""
    result = [row[:] for row in matrix]
    rows = len(result)
    cols = len(result[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if k != 0 and result[i][j] % k == 0:
                next_j = j + 1
                next_value = result[i][next_j] if next_j < cols else 1
                if next_value % 2 == 0:
                    for c in range(cols):
                        result[i][c] = 0
                else:
                    for r in range(rows):
                        result[r][j] = 0
                return result
    return result


def determinant(matrix: list[list[int]]) -> int:
    """Вычислить детерминант квадратной матрицы (рекурсивно)."""
    n = len(matrix)
    if n == 0:
        return 0
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det


def multiply_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Умножить две матрицы."""
    if not a or not b:
        return []
    if len(a[0]) != len(b):
        raise ValueError("Число столбцов первой матрицы должно равняться числу строк второй")

    rows_a = len(a)
    cols_b = len(b[0])
    cols_a = len(a[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for t in range(cols_a):
                result[i][j] += a[i][t] * b[t][j]
    return result


def swap_row_with_row_from_file(matrix: list[list[int]], row_index: int, row_filename: str) -> list[list[int]]:
    """Поменять строку матрицы с номером row_index на строку из файла."""
    with open(row_filename, "r", encoding="utf-8") as file:
        new_row = [int(x) for x in file.read().strip().split()]

    result = [row[:] for row in matrix]
    if 0 <= row_index < len(result) and len(new_row) == len(result[row_index]):
        result[row_index] = new_row
    return result


def read_vectors_from_keyboard(count: int) -> list[list[int]]:
    """Считать несколько векторов с клавиатуры."""
    vectors = []
    for i in range(count):
        row = [int(x) for x in input(f"Вектор {i + 1} (через пробел): ").split()]
        vectors.append(row)
    return vectors
