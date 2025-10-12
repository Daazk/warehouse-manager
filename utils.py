import json
import os
import shutil
from pathlib import Path

# ---------- Настройка путей ---------------
BASE_DIR = Path(__file__).resolve().parent
CLIENTS_DIR = BASE_DIR / "clients"
ORDERS_DIR = BASE_DIR / "orders"
SKLAD_FILE = BASE_DIR / "sklad.json"

# Создаём необходимые директории
CLIENTS_DIR.mkdir(exist_ok=True)
ORDERS_DIR.mkdir(exist_ok=True)

# ---------- Вспомагательные функции ----------------
def validate_id(id_value, id_type="ID"):             # ----------- Валидация ID
    """Безопасная проверка ID от path traversal атак"""
    if "/" in id_value or "\\" in id_value or ".." in id_value:
        print(f"❌ Недопустимые символы в {id_type}.")
        return False
    return True

def load_json(path):                # ------------- Загрузить из файла
    """Безопасная загрузка JSON с обработкой ошибок"""
    path = Path(path)
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            print(f"❌ Ошибка чтения файла {path}")
            return {}
        except Exception as e:
            print(f"❌ Неожиданная ошибка при чтении {path}: {e}")
            return {}
    return {}

def save_json(path, data):                           # ----------- Сохранить в файл
    """Атомарное сохранение JSON в файл"""
    path = Path(path)
    temp_path = path.with_suffix('.tmp')
    
    try:
        # Создаём временный файл
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        # Атомарно перемещаем временный файл в целевой
        shutil.move(str(temp_path), str(path))
    except Exception as e:
        # Удаляем временный файл в случае ошибки
        if temp_path.exists():
            temp_path.unlink()
        print(f"❌ Ошибка сохранения файла {path}: {e}")
        raise