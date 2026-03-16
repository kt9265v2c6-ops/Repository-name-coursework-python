"""Функции для работы с файлами."""


def read_from_keyboard_and_print() -> None:
    """Считать строку с клавиатуры и вывести её на экран."""
    text = input("Введите текст: ")
    print(f"Вы ввели: {text}")


def read_from_keyboard_and_write_to_file(filename: str) -> None:
    """Считать строку и записать в файл (с перезаписью)."""
    text = input("Введите текст для записи в файл: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\n")
    print(f"Текст записан в файл: {filename}")


def read_from_file_and_print(filename: str) -> None:
    """Считать содержимое файла и вывести."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("\nСодержимое файла:")
            print(file.read())
    except FileNotFoundError:
        print("Файл не найден.")


def read_from_keyboard_and_write_to_file_start(filename: str) -> None:
    """Считать строку и вставить её в начало файла."""
    text = input("Введите строку для вставки в начало файла: ")

    old_data = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            old_data = file.read()
    except FileNotFoundError:
        # Если файла нет, просто создадим новый.
        old_data = ""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\n" + old_data)

    print(f"Строка добавлена в начало файла: {filename}")
