import time
import json
import os
from datetime import date
from utils import load_json, save_json, SKLAD_FILE, CLIENTS_DIR, ORDERS_DIR, validate_id

# ---------- Список функций (Заказы) -------------


def create_order(order_id, client_id, items):        # ----------- Создание заказа
    # Безопасная проверка ID
    if not validate_id(order_id, "ID заказа"):
        return
        
    sklad = load_json(SKLAD_FILE)
    client_file = CLIENTS_DIR / f"{client_id}.json"

    if not client_file.exists():
        time.sleep(0.5)
        print("❌ Клиент не найден.")
        return
        
    client = load_json(client_file)
    total = 0
    order_items = []

    for pid, qty in items.items():
        if pid not in sklad:
            time.sleep(0.5)
            print(f"❌ Товар с ID {pid} отсутствует на складе.")
            return
        if sklad[pid]["quantity"] < qty:
            time.sleep(0.5)
            print(f"❌ Недостаточно товара {sklad[pid]["name"]} (на складе {sklad[pid]["quantity"]}).")
            return
        
        price = sklad[pid]["price"] * qty
        total += price
        order_items.append({
            "product_id": pid,
            "quantity": qty,
            "price": sklad[pid]["price"]
        })
        sklad[pid]["quantity"] -= qty

    save_json(SKLAD_FILE, sklad)

    order = {
        "order_id": order_id,
        "client_id": client_id,
        "date": str(date.today()), 
        "items": order_items,
        "total": total,
        "status": "В обработке"
    }

    save_json(ORDERS_DIR / f"{order_id}.json", order)

    client["orders"].append(order_id)
    save_json(client_file, client)

    time.sleep(0.5)
    print(f"✅ Заказ {order_id} создан. Общая сумма: {total}.")

def show_orders():
    files = list(ORDERS_DIR.glob("*.json"))
    if not files:
        time.sleep(0.5)
        print("❌ Заказов пока нет.")
        return
    
    print("\n---------Список заказов---------")
    for order_file in files:
        order = load_json(order_file)
        if order:  # Проверяем, что файл корректно загрузился
            print(f"[{order['order_id']}] Клиент: {order['client_id']} | Сумма: {order['total']} | Статус: {order['status']} | Дата: {order['date']}")

def update_order_status(order_id, new_status):       # ----------- Изменить статус заказа
    # Безопасная проверка ID
    if not validate_id(order_id, "ID заказа"):
        return
        
    order_file = ORDERS_DIR / f"{order_id}.json"

    if not order_file.exists():
        time.sleep(0.5)
        print("❌ Заказ не найден.")
        return
    
    order = load_json(order_file)
    order["status"] = new_status

    save_json(order_file, order)
    time.sleep(0.5)
    print(f"🔄 Статус заказа {order_id} изменён на: {new_status}.")


# ------------ Меню (заказы) ------------

def order_menu():                                    # ----------- Меню заказов
    while True:
        print("\n---------Меню заказов---------")
        print("1.➕ Создать заказ")
        print("2.📋 Список заказов")
        print("3.🔄 Изменить статус заказа")
        print("0.❌ Главное меню")

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
            order_id = input("ID заказа: ").strip()
            client_id = input("ID клиента: ").strip()
            
            if not order_id or not client_id:
                print("❌ ID заказа и клиента не могут быть пустыми.")
                continue

            time.sleep(0.5)
            print("\n-------Текущий склад-------")
            sklad = load_json(SKLAD_FILE)
            for pid, info in sklad.items():
                print(f"[{pid}] {info['name']} | Цена: {info['price']} | Остаток: {info['quantity']}")

            items = {}
            while True:
                pid = input("\nВведите ID товара (или Enter для завершения): ").strip()
                if pid == "":
                    break
                if pid not in sklad:
                    print("❌ Такого товара нет.")
                    continue
                try:
                    qty = int(input("Количество: "))
                    if qty <= 0:
                        print("❌ Количество должно быть положительным числом.")
                        continue
                    items[pid] = qty
                except ValueError:
                    print("❌ Пожалуйста, введите корректное количество.")
                    continue

            if not items:
                time.sleep(0.5)
                print("❌ Заказ пуст, отмена.")
                continue

            create_order(order_id, client_id, items)

        elif choice == 2:
            show_orders()

        elif choice == 3:
            time.sleep(0.5)
            order_id = input("ID заказа: ").strip()
            new_status = input("Новый статус: ").strip()
            if not order_id or not new_status:
                print("❌ ID заказа и статус не могут быть пустыми.")
                continue
            update_order_status(order_id, new_status)