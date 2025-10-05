import time
import json
import os
from utils import load_json, save_json, SKLAD_FILE, CLIENTS_DIR

# ---------- Список функций (Работа с клиентом) ------------

def add_client(client_id, name, phone, email):    # ------------- Добавить клиента
    client_file = f"{CLIENTS_DIR}/{client_id}.json"
    if os.path.exists(client_file):
        print("❌ Клиент с таким ID существует.")
        return
    
    client = {
        "ID": client_id,
        "name": name,
        "phone": phone,
        "email": email,
        "orders": []
    }

    with open(client_file, "w", encoding="utf-8") as f:
        json.dump(client, f, indent=4, ensure_ascii=False)
    print(f"✅ Клиент {name} добавлен.")

def show_clients():                               # ------------- Список клиентов
    files = os.listdir(CLIENTS_DIR)
    if not files:
        print("📋 Список клиентов пуст.")
        return
    print("\n---------Список клиентов---------")
    for fname in files:
        with open(f"{CLIENTS_DIR}/{fname}", "r", encoding="utf-8") as f:
            client = json.load(f)
            print(f"[{client['ID']}] {client['name']} | Телефон: {client['phone']} | Заказов: {len(client['orders'])}")

def remove_client(client_id):                     # ------------- Удаление клиента
    client_file = f"{CLIENTS_DIR}/{client_id}.json"
    if os.path.exists(client_file):
        os.remove(client_file)
        print(f"🗑️ Клиент {client_id} удалён.")
    else:
        print("❌ Клиент не найден.")

# ------------ Меню (клиенты) --------------

def client_menu():                  # ------------- Меню клиентов
    while True:
        print("\n---------Клиенты---------")
        print("1.✅Добавить клиента")
        print("2.🗑️ Удалить клиента")
        print("3.📋Список клиентов")
        print("0.❌Главное меню")

        choise = int(input("Введите номер пункта: "))

        if choise == 0:
            time.sleep(0.5)
            print("Выход в главное мею.")
            break

        elif choise == 1:
            client_id = input("ID клиента: ")
            name = input("Имя клиента: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            time.sleep(0.5)
            add_client(client_id, name, phone, email)

        elif choise == 2:
            time.sleep(0.5)
            show_clients()
            client_id = input("Введите ID клиента которого хотите удалить: ")
            remove_client(client_id)

        elif choise == 3:
            time.sleep(0.5)
            show_clients()


if __name__ == "__main__":
    client_menu()