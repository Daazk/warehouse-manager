import json
import os
from pathlib import Path

# ---------- Настройка путей ---------------
BASE_DIR = Path(__file__).resolve().parent
CLIENTS_DIR = BASE_DIR / "clients"
ORDERS_DIR = BASE_DIR / "orders"
SKLAD_FILE = BASE_DIR / "sklad.json"


os.makedirs(CLIENTS_DIR, exist_ok=True)
os.makedirs(ORDERS_DIR, exist_ok=True)

# ---------- Вспомагательные функции ----------------
def load_json(path):                # ------------- Загрузить из файла
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_json(path, data):                           # ----------- Сохранить в файл
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)