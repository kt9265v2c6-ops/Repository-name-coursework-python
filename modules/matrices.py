"""Модуль для работы с матрицами."""


def create_matrix_from_vectors(vectors: list[list[int]]) -> list[list[int]]:
    """Создать матрицу из списка векторов (строк)."""
    return [row[:] for row in vectors]


def remove_column(matrix: list[list[int]], index: int) -> list[list[int]]:
    """Удалить столбец матрицы по индексу."""
    return [row[:index] + row[index + 1 :] for row in matrix]


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Транспонировать матрицу."""
    return [list(row) for row in zip(*matrix)]


def remove_main_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    """Удалить элементы главной диагонали из строк матрицы."""
    result = []
    for i, row in enumerate(matrix):
        new_row = [value for j, value in enumerate(row) if i != j]
        result.append(new_row)
    return result


def replace_column_from_other_matrix(
    matrix1: list[list[int]], matrix2: list[list[int]], index: int
) -> list[list[int]]:
    """Заменить столбец в первой матрице столбцом из второй."""
    result = [row[:] for row in matrix1]
    for i in range(min(len(matrix1), len(matrix2))):
        result[i][index] = matrix2[i][index]
    return result


def determinant(matrix: list[list[int]]) -> int:
    """Найти детерминант квадратной матрицы (рекурсивно)."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        minor = []
        for row in matrix[1:]:
            minor.append(row[:col] + row[col + 1 :])
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det


def multiply_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """Умножить две матрицы."""
    rows_1 = len(matrix1)
    cols_1 = len(matrix1[0])
    rows_2 = len(matrix2)
    cols_2 = len(matrix2[0])

    if cols_1 != rows_2:
        raise ValueError("Нельзя умножить: число столбцов первой матрицы != числу строк второй")

    result = [[0 for _ in range(cols_2)] for _ in range(rows_1)]
    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(cols_1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def swap_rows(matrix: list[list[int]], row1: int, row2: int) -> list[list[int]]:
    """Поменять местами две строки матрицы."""
    result = [row[:] for row in matrix]
    result[row1], result[row2] = result[row2], result[row1]
    return result
