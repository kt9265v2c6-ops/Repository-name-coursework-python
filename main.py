"""Главный файл курсовой работы.

Запуск: python main.py
"""

from modules import file_operations
from modules import graphics
from modules import matrices
from modules import matrix_sorting
from modules import string_processing
from modules import vector_operations
from modules import vectors


def input_int(prompt: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_matrix() -> list[list[int]]:
    """Считать матрицу с клавиатуры."""
    rows = input_int("Количество строк: ")
    cols = input_int("Количество столбцов: ")
    matrix = []
    print("Введите строки матрицы (через пробел):")
    for i in range(rows):
        while True:
            row = input(f"Строка {i + 1}: ").split()
            if len(row) != cols:
                print("Неверное количество элементов. Попробуйте снова.")
                continue
            matrix.append([int(x) for x in row])
            break
    return matrix


def file_menu() -> None:
    while True:
        print("\n--- РАБОТА С ФАЙЛАМИ ---")
        print("1. Считать с клавиатуры и вывести")
        print("2. Считать с клавиатуры и записать в файл")
        print("3. Считать из файла и вывести")
        print("4. Считать с клавиатуры и записать в начало файла")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "1":
            file_operations.read_from_keyboard_and_print()
        elif choice == "2":
            filename = input("Имя файла: ")
            file_operations.read_from_keyboard_and_write_to_file(filename)
        elif choice == "3":
            filename = input("Имя файла: ")
            file_operations.read_from_file_and_print(filename)
        elif choice == "4":
            filename = input("Имя файла: ")
            file_operations.read_from_keyboard_and_write_to_file_start(filename)
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


def vectors_menu() -> None:
    while True:
        print("\n--- ВЕКТОРЫ ---")
        print("1. Создать вектор и вывести")
        print("2. Считать вектор с клавиатуры")
        print("3. Создать случайный вектор")
        print("4. Создать случайный вектор в заданном диапазоне")
        print("5. Найти максимальный элемент среди чётных")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "1":
            vector = [1, 2, 3, 4, 5]
            created = vectors.create_vector(vector)
            vectors.print_vector(created)
        elif choice == "2":
            vector = vectors.input_vector()
            vectors.print_vector(vector)
        elif choice == "3":
            length = input_int("Длина вектора: ")
            vector = vectors.random_vector(length)
            vectors.print_vector(vector)
        elif choice == "4":
            length = input_int("Длина вектора: ")
            vector = vectors.random_vector_by_user_range(length)
            vectors.print_vector(vector)
        elif choice == "5":
            vector = vectors.input_vector()
            result = vectors.max_even_element(vector)
            if result is None:
                print("Чётных элементов нет.")
            else:
                print("Максимальный чётный элемент:", result)
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


def vector_operations_menu() -> None:
    while True:
        print("\n--- ОПЕРАЦИИ С ВЕКТОРОМ ---")
        print("1. Вывести вектор в обратном порядке")
        print("2. Сортировать вектор по возрастанию/убыванию")
        print("3. Найти минимум или максимум по ключу")
        print("4. Найти НОД элементов")
        print("5. Сравнить сумму двух векторов")
        print("6. Извлечь цифры из строк и создать вектор")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "1":
            vector = vectors.input_vector()
            print(vector_operations.reverse_vector(vector))
        elif choice == "2":
            vector = vectors.input_vector()
            desc = input("Убывание? (y/n): ").lower() == "y"
            print(vector_operations.sort_vector(vector, desc))
        elif choice == "3":
            vector = vectors.input_vector()
            mode = input("Введите min или max: ").strip().lower()
            key_mode = input("Ключ (value/abs): ").strip().lower()
            print(vector_operations.find_min_or_max_by_key(vector, mode, key_mode))
        elif choice == "4":
            vector = vectors.input_vector()
            print("НОД:", vector_operations.gcd_of_vector(vector))
        elif choice == "5":
            print("Первый вектор:")
            v1 = vectors.input_vector()
            print("Второй вектор:")
            v2 = vectors.input_vector()
            print(vector_operations.compare_vector_sums(v1, v2))
        elif choice == "6":
            count = input_int("Сколько строк ввести: ")
            data = [input(f"Строка {i + 1}: ") for i in range(count)]
            print(vector_operations.extract_digits_to_vector(data))
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


def matrices_menu() -> None:
    while True:
        print("\n--- МАТРИЦЫ ---")
        print("1. Создать матрицу из векторов")
        print("2. Удалить столбец по индексу")
        print("3. Транспонировать матрицу")
        print("4. Удалить главную диагональ")
        print("5. Заменить столбец из другой матрицы")
        print("6. Найти детерминант")
        print("7. Умножить матрицы")
        print("8. Поменять строки местами")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "1":
            matrix = input_matrix()
            print(matrices.create_matrix_from_vectors(matrix))
        elif choice == "2":
            matrix = input_matrix()
            index = input_int("Индекс столбца: ")
            print(matrices.remove_column(matrix, index))
        elif choice == "3":
            matrix = input_matrix()
            print(matrices.transpose_matrix(matrix))
        elif choice == "4":
            matrix = input_matrix()
            print(matrices.remove_main_diagonal(matrix))
        elif choice == "5":
            print("Первая матрица:")
            matrix1 = input_matrix()
            print("Вторая матрица:")
            matrix2 = input_matrix()
            index = input_int("Индекс столбца: ")
            print(matrices.replace_column_from_other_matrix(matrix1, matrix2, index))
        elif choice == "6":
            matrix = input_matrix()
            print("Детерминант:", matrices.determinant(matrix))
        elif choice == "7":
            print("Первая матрица:")
            matrix1 = input_matrix()
            print("Вторая матрица:")
            matrix2 = input_matrix()
            try:
                print(matrices.multiply_matrices(matrix1, matrix2))
            except ValueError as error:
                print(error)
        elif choice == "8":
            matrix = input_matrix()
            row1 = input_int("Индекс первой строки: ")
            row2 = input_int("Индекс второй строки: ")
            print(matrices.swap_rows(matrix, row1, row2))
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


def sorting_menu() -> None:
    while True:
        print("\n--- СОРТИРОВКИ ---")
        print("1. Сортировка Шелла")
        print("2. Пузырьковая сортировка")
        print("3. Сортировка вставками")
        print("4. Сортировка выбором")
        print("5. Сортировка кучей")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "0":
            break

        vector = vectors.input_vector()
        if choice == "1":
            print(matrix_sorting.shell_sort(vector))
        elif choice == "2":
            print(matrix_sorting.bubble_sort(vector))
        elif choice == "3":
            print(matrix_sorting.insertion_sort(vector))
        elif choice == "4":
            print(matrix_sorting.selection_sort(vector))
        elif choice == "5":
            print(matrix_sorting.heap_sort(vector))
        else:
            print("Неверный пункт меню.")


def strings_menu() -> None:
    while True:
        print("\n--- СТРОКИ ---")
        print("1. Форматирование текста")
        print("2. Вывод таблицы псевдографикой")
        print("3. Удалить символы из строки")
        print("4. Поиск строки в файле")
        print("5. Найти слова с нечётной длиной")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "1":
            text = input("Введите текст: ")
            print(string_processing.format_text(text))
        elif choice == "2":
            headers = ["Имя", "Возраст"]
            rows = [["Анна", "19"], ["Иван", "20"], ["Олег", "18"]]
            print(string_processing.pseudo_table(headers, rows))
        elif choice == "3":
            text = input("Введите строку: ")
            chars = input("Какие символы удалить: ")
            print(string_processing.remove_characters(text, chars))
        elif choice == "4":
            filename = input("Имя файла: ")
            query = input("Что искать: ")
            try:
                lines = string_processing.search_string_in_file(filename, query)
                print("Найдено в строках:", lines)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == "5":
            text = input("Введите текст: ")
            print(string_processing.find_odd_length_words(text))
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


def graphics_menu() -> None:
    while True:
        print("\n--- ГРАФИКА (Tkinter) ---")
        print("1. Нарисовать квадрат")
        print("2. Вписать треугольник в круг")
        print("3. Наложить круг на треугольник")
        print("4. Построить гистограмму по вектору")
        print("5. Вывести матрицу и выделить min/max")
        print("0. Назад")
        choice = input("Выберите пункт: ")

        if choice == "1":
            graphics.draw_square()
        elif choice == "2":
            graphics.draw_triangle_in_circle()
        elif choice == "3":
            graphics.draw_circle_on_triangle()
        elif choice == "4":
            vector = vectors.input_vector()
            graphics.draw_histogram(vector)
        elif choice == "5":
            matrix = input_matrix()
            graphics.show_matrix_with_min_max(matrix)
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


def main() -> None:
    """Главное меню программы."""
    while True:
        print("\n========== КУРСОВАЯ РАБОТА ==========")
        print("1. Работа с файлами")
        print("2. Векторы")
        print("3. Операции с вектором")
        print("4. Матрицы")
        print("5. Сортировки")
        print("6. Строки")
        print("7. Графика")
        print("0. Выход")

        choice = input("Выберите раздел: ")

        if choice == "1":
            file_menu()
        elif choice == "2":
            vectors_menu()
        elif choice == "3":
            vector_operations_menu()
        elif choice == "4":
            matrices_menu()
        elif choice == "5":
            sorting_menu()
        elif choice == "6":
            strings_menu()
        elif choice == "7":
            graphics_menu()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
