"""Операции над векторами."""

import math


def reverse_vector(vector: list[int]) -> list[int]:
    """Вернуть вектор в обратном порядке."""
    return vector[::-1]


def sort_vector(vector: list[int], descending: bool = False) -> list[int]:
    """Сортировка вектора по возрастанию/убыванию."""
    return sorted(vector, reverse=descending)


def find_min_or_max(vector: list[int], mode: str) -> int:
    """Найти минимум или максимум в зависимости от режима."""
    if mode == "min":
        return min(vector)
    return max(vector)


def gcd_of_vector(vector: list[int]) -> int:
    """Найти НОД всех элементов вектора."""
    if not vector:
        return 0
    result = abs(vector[0])
    for number in vector[1:]:
        result = math.gcd(result, abs(number))
    return result


def compare_vector_sums(v1: list[int], v2: list[int]) -> list[int]:
    """Сравнить суммы двух векторов и вернуть тот, где сумма меньше."""
    return v1 if sum(v1) <= sum(v2) else v2


def digits_from_mixed_strings(lines: list[str]) -> list[int]:
    """Из нескольких строк собрать вектор цифр."""
    digits = []
    for line in lines:
        for symbol in line:
            if symbol.isdigit():
                digits.append(int(symbol))
    return digits
