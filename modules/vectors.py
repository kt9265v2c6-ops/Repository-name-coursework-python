"""Модуль для создания и анализа векторов."""

import random


def create_vector(values: list[int]) -> list[int]:
    """Создать вектор из готового списка значений."""
    return values


def print_vector(vector: list[int]) -> None:
    """Вывести вектор на экран."""
    print("Вектор:", vector)


def input_vector() -> list[int]:
    """Считать вектор с клавиатуры (через пробел)."""
    raw = input("Введите элементы вектора через пробел: ")
    return [int(x) for x in raw.split()]


def random_vector(length: int, start: int = 0, end: int = 100) -> list[int]:
    """Создать вектор случайных чисел заданной длины."""
    return [random.randint(start, end) for _ in range(length)]


def random_vector_by_user_range(length: int) -> list[int]:
    """Создать случайный вектор в диапазоне, введённом пользователем."""
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    return random_vector(length, start, end)


def max_even_element(vector: list[int]) -> int | None:
    """Найти максимальный элемент среди чётных."""
    even_numbers = [x for x in vector if x % 2 == 0]
    if not even_numbers:
        return None
    return max(even_numbers)
