import time
import json
import os
from utils import load_json, save_json, SKLAD_FILE, CLIENTS_DIR, validate_id

# ---------- Список функций (Работа с клиентом) ------------


def add_client(client_id, name, phone, email):    # ------------- Добавить клиента
    # Безопасная проверка ID
    if not validate_id(client_id, "ID клиента"):
        return
        
    client_file = CLIENTS_DIR / f"{client_id}.json"
    if client_file.exists():
        print("❌ Клиент с таким ID существует.")
        return
    
    client = {
        "ID": client_id,
        "name": name,
        "phone": phone,
        "email": email,
        "orders": []
    }

    save_json(client_file, client)
    print(f"✅ Клиент {name} добавлен.")

def show_clients():                               # ------------- Список клиентов
    files = list(CLIENTS_DIR.glob("*.json"))
    if not files:
        print("📋 Список клиентов пуст.")
        return
    print("\n---------Список клиентов---------")
    for client_file in files:
        client = load_json(client_file)
        if client:  # Проверяем, что файл корректно загрузился
            print(f"[{client['ID']}] {client['name']} | Телефон: {client['phone']} | Заказов: {len(client['orders'])}")

def remove_client(client_id):                     # ------------- Удаление клиента
    # Безопасная проверка ID
    if not validate_id(client_id, "ID клиента"):
        return
        
    client_file = CLIENTS_DIR / f"{client_id}.json"
    if client_file.exists():
        client_file.unlink()
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

        try:
            choice = int(input("Введите номер пункта: "))
        except ValueError:
            print("❌ Пожалуйста, введите число.")
            continue

        if choice == 0:
            time.sleep(0.5)
            print("Выход в главное меню.")
            break

        elif choice == 1:
            client_id = input("ID клиента: ").strip()
            name = input("Имя клиента: ").strip()
            phone = input("Телефон: ").strip()
            email = input("Email: ").strip()
            
            if not all([client_id, name, phone, email]):
                print("❌ Все поля обязательны для заполнения.")
                continue
            
            # Простая валидация email
            if "@" not in email or "." not in email.split("@")[1]:
                print("❌ Неверный формат email.")
                continue
                
            time.sleep(0.5)
            add_client(client_id, name, phone, email)

        elif choice == 2:
            time.sleep(0.5)
            show_clients()
            client_id = input("Введите ID клиента которого хотите удалить: ").strip()
            if not client_id:
                print("❌ ID не может быть пустым.")
                continue
            remove_client(client_id)

        elif choice == 3:
            time.sleep(0.5)
            show_clients()


if __name__ == "__main__":
    client_menu()