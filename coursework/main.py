"""Главная программа курсовой работы (текстовое меню)."""

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
            print("Ошибка: нужно ввести целое число.")


def input_matrix_keyboard() -> list[list[int]]:
    rows = input_int("Количество строк: ")
    cols = input_int("Количество столбцов: ")
    matrix = []
    print("Введите строки матрицы (элементы через пробел):")
    for i in range(rows):
        while True:
            parts = input(f"Строка {i + 1}: ").split()
            if len(parts) != cols:
                print("Неверное количество элементов.")
                continue
            matrix.append([int(x) for x in parts])
            break
    return matrix


def menu_files() -> None:
    while True:
        print("\n=== ФАЙЛЫ ===")
        print("1. Считать с клавиатуры и вывести")
        print("2. Считать с клавиатуры и записать в файл")
        print("3. Считать из файла и вывести")
        print("4. Считать с клавиатуры и записать в начало файла")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "1":
            file_operations.read_from_keyboard_and_print()
        elif choice == "2":
            filename = input("Файл: ")
            file_operations.read_from_keyboard_and_write_to_file(filename)
        elif choice == "3":
            filename = input("Файл: ")
            file_operations.read_from_file_and_print(filename)
        elif choice == "4":
            filename = input("Файл: ")
            file_operations.read_from_keyboard_and_write_to_file_start(filename)
        elif choice == "0":
            break
        else:
            print("Неверный пункт.")


def menu_vectors() -> None:
    while True:
        print("\n=== ВЕКТОРЫ ===")
        print("1. Создать массив и вывести")
        print("2. Считать вектор с клавиатуры")
        print("3. Создать случайный вектор")
        print("4. Случайный вектор в диапазоне пользователя + запись в файл")
        print("5. Максимальный элемент среди чётных")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "1":
            vec = vectors.create_vector([1, 2, 3, 4, 5])
            vectors.print_vector(vec)
        elif choice == "2":
            vec = vectors.input_vector()
            vectors.print_vector(vec)
        elif choice == "3":
            n = input_int("Длина: ")
            vectors.print_vector(vectors.random_vector(n))
        elif choice == "4":
            n = input_int("Длина: ")
            filename = input("Файл для записи: ")
            vectors.print_vector(vectors.random_vector_by_user_range(n, filename))
        elif choice == "5":
            vec = vectors.input_vector()
            result = vectors.max_even_element(vec)
            print("Результат:", result if result is not None else "чётных нет")
        elif choice == "0":
            break
        else:
            print("Неверный пункт.")


def menu_vector_ops() -> None:
    while True:
        print("\n=== ОПЕРАЦИИ С ВЕКТОРАМИ ===")
        print("1. Обратная последовательность")
        print("2. Сортировка (по возрастанию/убыванию)")
        print("3. Найти минимум/максимум по ключу")
        print("4. НОД элементов")
        print("5. Сравнить суммы двух векторов")
        print("6. Из строк собрать вектор цифр")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "1":
            vec = vectors.input_vector()
            print(vector_operations.reverse_vector(vec))
        elif choice == "2":
            vec = vectors.input_vector()
            desc = input("Убывание? (y/n): ").lower() == "y"
            print(vector_operations.sort_vector(vec, desc))
        elif choice == "3":
            vec = vectors.input_vector()
            mode = input("Введите min или max: ").strip().lower()
            if mode not in ("min", "max"):
                print("Нужно min или max")
            else:
                print(vector_operations.find_min_or_max(vec, mode))
        elif choice == "4":
            vec = vectors.input_vector()
            print("НОД:", vector_operations.gcd_of_vector(vec))
        elif choice == "5":
            print("Первый вектор:")
            v1 = vectors.input_vector()
            print("Второй вектор:")
            v2 = vectors.input_vector()
            print("Вектор с меньшей суммой:", vector_operations.compare_vector_sums(v1, v2))
        elif choice == "6":
            count = input_int("Сколько строк ввести: ")
            lines = [input(f"Строка {i + 1}: ") for i in range(count)]
            print("Вектор из цифр:", vector_operations.digits_from_mixed_strings(lines))
        elif choice == "0":
            break
        else:
            print("Неверный пункт.")


def menu_matrices() -> None:
    while True:
        print("\n=== МАТРИЦЫ ===")
        print("1. Создать матрицу из нескольких векторов")
        print("2. Удалить столбец по индексу из файла")
        print("3. Транспонировать матрицу")
        print("4. Удалить главную диагональ")
        print("5. Заменить столбец матрицы столбцом другой матрицы")
        print("6. Найти кратный элемент и занулить строку/столбец")
        print("7. Найти детерминант")
        print("8. Умножить матрицу из файла на матрицу с клавиатуры")
        print("9. В матрице заменить строку строкой из файла")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "1":
            count = input_int("Сколько векторов (строк): ")
            m = matrices.create_matrix_from_vectors(matrices.read_vectors_from_keyboard(count))
            matrices.print_matrix(m)
        elif choice == "2":
            m = input_matrix_keyboard()
            idx_file = input("Файл с индексом столбца: ")
            matrices.print_matrix(matrices.remove_column_by_index_from_file(m, idx_file))
        elif choice == "3":
            m = input_matrix_keyboard()
            matrices.print_matrix(matrices.transpose_matrix(m))
        elif choice == "4":
            m = input_matrix_keyboard()
            matrices.print_matrix(matrices.remove_main_diagonal_one_loop(m))
        elif choice == "5":
            print("Основная матрица:")
            m1 = input_matrix_keyboard()
            print("Вторая матрица:")
            m2 = input_matrix_keyboard()
            tc = input_int("Какой столбец заменить в основной матрице: ")
            sc = input_int("Какой столбец взять из второй матрицы: ")
            matrices.print_matrix(matrices.replace_column(m1, m2, tc, sc))
        elif choice == "6":
            m = input_matrix_keyboard()
            k = input_int("Число k: ")
            matrices.print_matrix(matrices.zero_row_or_column_by_divisibility_rule(m, k))
        elif choice == "7":
            m = input_matrix_keyboard()
            try:
                print("Детерминант:", matrices.determinant(m))
            except ValueError as err:
                print(err)
        elif choice == "8":
            filename = input("Файл с первой матрицей: ")
            m1 = matrices.read_matrix_from_file(filename)
            print("Введите вторую матрицу:")
            m2 = input_matrix_keyboard()
            try:
                matrices.print_matrix(matrices.multiply_matrices(m1, m2))
            except ValueError as err:
                print(err)
        elif choice == "9":
            m = input_matrix_keyboard()
            idx = input_int("Номер строки: ")
            filename = input("Файл со строкой: ")
            matrices.print_matrix(matrices.swap_row_with_row_from_file(m, idx, filename))
        elif choice == "0":
            break
        else:
            print("Неверный пункт.")


def menu_matrix_sorting() -> None:
    while True:
        print("\n=== СОРТИРОВКИ МАТРИЦ ===")
        print("1. Сортировка Шелла")
        print("2. Пузырьковая сортировка")
        print("3. Сортировка вставками")
        print("4. Сортировка выбором")
        print("5. Сортировка кучей")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "0":
            break

        m = input_matrix_keyboard()
        methods = {
            "1": "shell",
            "2": "bubble",
            "3": "insertion",
            "4": "selection",
            "5": "heap",
        }
        method = methods.get(choice)
        if method:
            matrices.print_matrix(matrix_sorting.sort_matrix(m, method))
        else:
            print("Неверный пункт.")


def menu_strings() -> None:
    while True:
        print("\n=== СТРОКИ ===")
        print("1. Форматированный текст (лево/центр/право)")
        print("2. Таблица псевдографикой")
        print("3. Удалить из строки файла символы с клавиатуры")
        print("4. Поиск в файле (неполное совпадение), вывести номер последней строки")
        print("5. Слова нечётной длины из файла")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "1":
            text = input("Введите текст: ")
            left, center, right = string_processing.align_text(text)
            print("Лево :", left)
            print("Центр:", center)
            print("Право:", right)
        elif choice == "2":
            headers = ["Имя", "Оценка"]
            rows = [["Анна", "5"], ["Игорь", "4"], ["Мария", "5"]]
            print(string_processing.pseudo_table(headers, rows))
        elif choice == "3":
            filename = input("Файл: ")
            chars = input("Какие символы удалить: ")
            print(string_processing.remove_chars_from_file_line(filename, chars))
        elif choice == "4":
            query = input("Строка для поиска: ")
            filename = input("Файл: ")
            line_num = string_processing.search_partial_in_file(filename, query)
            print("Номер последней строки:", line_num)
        elif choice == "5":
            filename = input("Файл: ")
            print(string_processing.odd_length_words_from_file(filename))
        elif choice == "0":
            break
        else:
            print("Неверный пункт.")


def menu_graphics() -> None:
    while True:
        print("\n=== ГРАФИКА (Tkinter) ===")
        print("1. Квадрат")
        print("2. Треугольник в круге")
        print("3. Круг радиуса 1/4 на случайной вершине треугольника")
        print("4. Гистограмма по вектору")
        print("5. Матрица с выделением min/max")
        print("6. Матрица из файла: раскраска строк по индексу + значению")
        print("7. Матрица из файла: раскраска столбцов по правилу")
        print("8. Отсортированная матрица с градиентом строк")
        print("0. Назад")
        choice = input("Выбор: ")

        if choice == "1":
            graphics.draw_square()
        elif choice == "2":
            r = input_int("Радиус: ")
            graphics.draw_triangle_in_circle(r)
        elif choice == "3":
            r = input_int("Радиус исходного круга: ")
            graphics.overlay_circle_on_triangle(r)
        elif choice == "4":
            vec = vectors.input_vector()
            graphics.draw_histogram(vec)
        elif choice == "5":
            m = input_matrix_keyboard()
            graphics.show_matrix_min_max(m)
        elif choice == "6":
            filename = input("Файл с матрицей: ")
            value = input_int("Значение с клавиатуры: ")
            graphics.color_rows_by_index_plus_value(matrices.read_matrix_from_file(filename), value)
        elif choice == "7":
            filename = input("Файл с матрицей: ")
            graphics.color_columns_reverse_by_first_element(matrices.read_matrix_from_file(filename))
        elif choice == "8":
            filename = input("Файл с матрицей: ")
            method = input("Метод сортировки (shell/bubble/insertion/selection/heap): ").strip().lower()
            matrix = matrices.read_matrix_from_file(filename)
            sorted_matrix = matrix_sorting.sort_matrix(matrix, method)
            graphics.show_sorted_matrix_with_gradient(sorted_matrix)
        elif choice == "0":
            break
        else:
            print("Неверный пункт.")


def main() -> None:
    while True:
        print("\n==============================")
        print(" КУРСОВАЯ РАБОТА ПО PYTHON 3")
        print("==============================")
        print("1. Работа с файлами")
        print("2. Векторы")
        print("3. Операции с векторами")
        print("4. Матрицы")
        print("5. Сортировки матриц")
        print("6. Строки")
        print("7. Графика (Tkinter)")
        print("0. Выход")

        choice = input("Выберите раздел: ")

        try:
            if choice == "1":
                menu_files()
            elif choice == "2":
                menu_vectors()
            elif choice == "3":
                menu_vector_ops()
            elif choice == "4":
                menu_matrices()
            elif choice == "5":
                menu_matrix_sorting()
            elif choice == "6":
                menu_strings()
            elif choice == "7":
                menu_graphics()
            elif choice == "0":
                print("Завершение программы.")
                break
            else:
                print("Неверный пункт.")
        except ValueError:
            print("Ошибка ввода: ожидаются числа в матрицах/векторах.")
        except FileNotFoundError:
            print("Ошибка: файл не найден.")


if __name__ == "__main__":
    main()
