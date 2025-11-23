"""
Тесты для основного модуля warehouse-manager
"""
import unittest
from pathlib import Path
import sys

# Добавляем корневую директорию проекта в путь
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from utils import load_json, SKLAD_FILE, CLIENTS_DIR, ORDERS_DIR


class TestMainModule(unittest.TestCase):
    """Тесты для основного модуля"""

    def test_sklad_file_exists(self):
        """Проверка существования файла склада"""
        self.assertTrue(SKLAD_FILE.exists(), f"Файл {SKLAD_FILE} не найден")

    def test_clients_dir_exists(self):
        """Проверка существования директории клиентов"""
        self.assertTrue(CLIENTS_DIR.exists(), f"Директория {CLIENTS_DIR} не найдена")

    def test_orders_dir_exists(self):
        """Проверка существования директории заказов"""
        self.assertTrue(ORDERS_DIR.exists(), f"Директория {ORDERS_DIR} не найдена")

    def test_load_sklad(self):
        """Проверка загрузки данных склада"""
        data = load_json(SKLAD_FILE)
        self.assertIsInstance(data, dict, "Данные склада должны быть словарём")


if __name__ == '__main__':
    unittest.main()


