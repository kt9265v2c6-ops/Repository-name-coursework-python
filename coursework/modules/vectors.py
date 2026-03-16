"""Функции для базовой работы с векторами (списками)."""

import random


def create_vector(values: list[int]) -> list[int]:
    """Создать вектор из готового списка."""
    return values[:]


def print_vector(vector: list[int]) -> None:
    """Вывести вектор в читаемом виде."""
    print("Вектор:", vector)


def input_vector() -> list[int]:
    """Считать вектор с клавиатуры."""
    raw = input("Введите элементы вектора через пробел: ").split()
    return [int(x) for x in raw]


def random_vector(length: int, low: int = -50, high: int = 50) -> list[int]:
    """Создать случайный вектор заданной длины."""
    return [random.randint(low, high) for _ in range(length)]


def random_vector_by_user_range(length: int, filename: str | None = None) -> list[int]:
    """Создать случайный вектор в диапазоне пользователя и при необходимости записать в файл."""
    low = int(input("Нижняя граница: "))
    high = int(input("Верхняя граница: "))
    vector = random_vector(length, low, high)

    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(" ".join(str(x) for x in vector))
        print(f"Вектор записан в файл: {filename}")

    return vector


def max_even_element(vector: list[int]) -> int | None:
    """Найти максимальный чётный элемент вектора."""
    evens = [x for x in vector if x % 2 == 0]
    if not evens:
        return None
    return max(evens)
