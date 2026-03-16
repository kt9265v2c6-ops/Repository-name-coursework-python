"""Точка входа для запуска курсового проекта командой: python main.py"""

import os
import sys

# Добавляем папку coursework в путь импорта, чтобы main и modules работали как в структуре задания.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COURSEWORK_DIR = os.path.join(BASE_DIR, "coursework")
if COURSEWORK_DIR not in sys.path:
    sys.path.insert(0, COURSEWORK_DIR)

from main import main  # type: ignore  # noqa: E402


if __name__ == "__main__":
    main()
