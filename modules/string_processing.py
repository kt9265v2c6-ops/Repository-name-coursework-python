"""Модуль для обработки строк."""


def format_text(text: str) -> str:
    """Простое форматирование текста: убрать лишние пробелы и сделать заглавные буквы после точки."""
    clean = " ".join(text.split())
    parts = clean.split(".")
    formatted_parts = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            formatted_parts.append(stripped[0].upper() + stripped[1:])
    return ". ".join(formatted_parts) + ("." if formatted_parts else "")


def pseudo_table(headers: list[str], rows: list[list[str]]) -> str:
    """Сформировать таблицу псевдографикой в виде строки."""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def border() -> str:
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def make_row(cells: list[str]) -> str:
        return "|" + "|".join(f" {cell.ljust(widths[i])} " for i, cell in enumerate(cells)) + "|"

    lines = [border(), make_row(headers), border()]
    for row in rows:
        lines.append(make_row(row))
    lines.append(border())
    return "\n".join(lines)


def remove_characters(text: str, chars: str) -> str:
    """Удалить заданные символы из строки."""
    return "".join(ch for ch in text if ch not in chars)


def search_string_in_file(filename: str, search: str) -> list[int]:
    """Найти строку (подстроку) в файле и вернуть номера строк."""
    line_numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            if search in line:
                line_numbers.append(index)
    return line_numbers


def find_odd_length_words(text: str) -> list[str]:
    """Найти все слова с нечётной длиной."""
    words = text.split()
    return [word for word in words if len(word) % 2 == 1]
