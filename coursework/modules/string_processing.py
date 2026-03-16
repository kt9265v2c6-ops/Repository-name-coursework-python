"""Функции для обработки строк."""


def align_text(text: str, width: int = 60) -> tuple[str, str, str]:
    """Вернуть текст, выровненный влево, по центру и вправо."""
    return text.ljust(width), text.center(width), text.rjust(width)


def pseudo_table(headers: list[str], rows: list[list[str]]) -> str:
    """Построить таблицу псевдографикой."""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    line = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def to_row(cells: list[str]) -> str:
        return "|" + "|".join(f" {cells[i].ljust(widths[i])} " for i in range(len(cells))) + "|"

    out = [line, to_row(headers), line]
    for row in rows:
        out.append(to_row(row))
    out.append(line)
    return "\n".join(out)


def remove_chars_from_file_line(filename: str, chars: str) -> str:
    """Считать первую строку из файла и удалить указанные символы."""
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline().rstrip("\n")
    return "".join(ch for ch in line if ch not in chars)


def search_partial_in_file(filename: str, query: str) -> int:
    """Найти последнюю строку, где есть неполное совпадение query."""
    last_index = -1
    with open(filename, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            if query.lower() in line.lower():
                last_index = i
    return last_index


def odd_length_words_from_file(filename: str) -> list[str]:
    """Считать все строки и вернуть слова с нечётной длиной."""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    cleaned = []
    for ch in text:
        if ch.isalnum() or ch.isspace():
            cleaned.append(ch)
        else:
            cleaned.append(" ")

    words = "".join(cleaned).split()
    return [word for word in words if len(word) % 2 == 1]
