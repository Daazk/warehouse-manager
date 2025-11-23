import json
import shutil
import logging
from pathlib import Path

# ---------- Настройка путей ---------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CLIENTS_DIR = DATA_DIR / "clients"
ORDERS_DIR = DATA_DIR / "orders"
SKLAD_FILE = DATA_DIR / "sklad.json"
REPORTS_DIR = BASE_DIR / "reports"
REPORT = REPORTS_DIR / "report.xlsx"
LOGGING = REPORTS_DIR / "app.log"

# Создаём необходимые директории
DATA_DIR.mkdir(exist_ok=True)
CLIENTS_DIR.mkdir(exist_ok=True)
ORDERS_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)
LOGGING.mkdir(exist_ok=True)

# ---------- Настройка логирования ------------------
logging.basicConfig(
    filename=LOGGING / "app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------- Вспомагательные функции ----------------
def validate_id(id_value, id_type="ID"):            
    """Безопасная проверка ID от path traversal атак"""

    if "/" in id_value or "\\" in id_value or ".." in id_value:
        print(f"❌ Недопустимые символы в {id_type}.")
        return False
    return True  

def load_json(path):                
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

def save_json(path, data):                           
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

def load_all_clients(folder=CLIENTS_DIR):
    """Загружает всех клиентов из папки clients безопасно"""

    folder = Path(folder)
    clients = {}

    if not folder.exists():
        return clients

    for file in folder.iterdir():
        if file.suffix == ".json":
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                clients[file.stem] = data  
            except json.JSONDecodeError:
                print(f"❌ Ошибка: файл клиента {file} повреждён")
            except Exception as e:
                print(f"❌ Неожиданная ошибка при чтении {file}: {e}")

    return clients

def load_all_orders(folder=ORDERS_DIR):
    """Загружает все заказы из папки orders безопасно"""
    folder = Path(folder)
    orders = {}

    if not folder.exists():
        return orders

    for file in folder.iterdir():
        if file.suffix == ".json":
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                orders[file.stem] = data  
            except json.JSONDecodeError:
                print(f"❌ Ошибка: файл заказов {file} повреждён")
            except Exception as e:
                print(f"❌ Неожиданная ошибка при чтении {file}: {e}")

    return orders

