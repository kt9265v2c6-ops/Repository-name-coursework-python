"""Модуль операций с векторами."""

from math import gcd


def reverse_vector(vector: list[int]) -> list[int]:
    """Вернуть вектор в обратном порядке."""
    return vector[::-1]


def sort_vector(vector: list[int], descending: bool = False) -> list[int]:
    """Отсортировать вектор по возрастанию или убыванию."""
    return sorted(vector, reverse=descending)


def find_min_or_max_by_key(vector: list[int], mode: str = "min", key_mode: str = "value") -> int:
    """Найти минимум или максимум по ключу (value или abs)."""
    if key_mode == "abs":
        key_function = abs
    else:
        key_function = lambda x: x

    if mode == "max":
        return max(vector, key=key_function)
    return min(vector, key=key_function)


def gcd_of_vector(vector: list[int]) -> int:
    """Найти НОД всех элементов вектора."""
    result = abs(vector[0])
    for value in vector[1:]:
        result = gcd(result, abs(value))
    return result


def compare_vector_sums(vector1: list[int], vector2: list[int]) -> str:
    """Сравнить суммы двух векторов."""
    sum1 = sum(vector1)
    sum2 = sum(vector2)
    if sum1 > sum2:
        return "Сумма первого вектора больше"
    if sum2 > sum1:
        return "Сумма второго вектора больше"
    return "Суммы векторов равны"


def extract_digits_to_vector(strings: list[str]) -> list[int]:
    """Извлечь все цифры из списка строк и собрать вектор."""
    digits = []
    for item in strings:
        for char in item:
            if char.isdigit():
                digits.append(int(char))
    return digits
