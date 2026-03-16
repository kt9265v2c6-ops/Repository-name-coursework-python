"""Модуль для работы с файлами."""


def read_from_keyboard_and_print() -> None:
    """Считать строку с клавиатуры и вывести её на экран."""
    text = input("Введите строку: ")
    print("Вы ввели:", text)


def read_from_keyboard_and_write_to_file(filename: str) -> None:
    """Считать строку с клавиатуры и записать в файл."""
    text = input("Введите строку для записи в файл: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\n")
    print(f"Данные записаны в файл: {filename}")


def read_from_file_and_print(filename: str) -> None:
    """Считать информацию из файла и вывести на экран."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print("Содержимое файла:")
        print(content)
    except FileNotFoundError:
        print("Файл не найден.")


def read_from_keyboard_and_write_to_file_start(filename: str) -> None:
    """Считать строку и записать её в начало файла."""
    text = input("Введите строку для добавления в начало файла: ")

    old_content = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            old_content = file.read()
    except FileNotFoundError:
        # Если файла нет, просто создадим новый.
        pass

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\n" + old_content)

    print(f"Строка добавлена в начало файла: {filename}")
