import time
from utils import load_json, save_json, SKLAD_FILE

# ---------- Список функций (Работа со складом) ----------------

def add_product(product_id, name, category, price, quantity):      # --------- Добавление товара на склад
    sklad = load_json(SKLAD_FILE)
    sklad[product_id] = {
        "name": name,
        "category": category,
        "price": price, 
        "quantity": quantity
    }
    save_json(SKLAD_FILE, sklad)
    time.sleep(0.5)
    print(f"Товар {name} добавлен на склад.")

def remove_product(product_id):                      # ------------ Удаление товара из склада
    sklad = load_json(SKLAD_FILE)
    if product_id in sklad:
        deleted = sklad.pop(product_id)
        save_json(SKLAD_FILE, sklad)
        time.sleep(0.5)
        print(f"🗑️ Товар {deleted['name']} удалён со склада.")
    else:
        time.sleep(0.5)
        print("❌ Товар не найден.")

def show_sklad():                                  # ------------ Показать склад
    sklad = load_json(SKLAD_FILE)
    if not sklad:
        print("📦 Склад пуст.")
        return
    time.sleep(0.5)
    print("\n---------Ассортимент склада---------")
    for pid, info in sklad.items():
        print(f"[{pid}] {info['name']} | Категория: {info['category']} | Цена: {info['price']} | Кол-во: {info['quantity']}")

def update_quantity(product_id, new_quantity):    # ------------ Изменить кол-во товара
    sklad = load_json(SKLAD_FILE)
    if product_id in sklad:
        sklad[product_id]["quantity"] = new_quantity
        save_json(SKLAD_FILE, sklad)
        time.sleep(0.5)
        print(f"🔄 Количество товара {sklad[product_id]['name']} обновлено: {new_quantity}.")
    else:
        time.sleep(0.5)
        print("❌ Товар не найден.")

def update_price(product_id, new_price):          # ------------- Изменить цену товара
    sklad = load_json(SKLAD_FILE)
    if product_id in sklad:
        sklad[product_id]["price"] = new_price
        save_json(SKLAD_FILE, sklad)
        time.sleep(0.5)
        print(f"🔄 Цена на товар {sklad[product_id]['name']} обновлена: {new_price}")
    else:
        time.sleep(0.5)
        print("❌ Товар не найден.")


# -------------- Меню --------------------

def sklad_menu():                   # ------------- Меню склада
    while True:
        print("\n---------Склад---------")
        print("1.➕ Добавить товар")
        print("2.🗑️ Удалить товар")
        print("3.🔄 Изменить цену")
        print("4.🔄 Изменить количество")
        print("5.📦 Показать все товары")
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
            time.sleep(0.5)
            pid = input("ID товара: ").strip()
            name = input("Название товара: ").strip()
            category = input("Категория товара: ").strip()
            try:
                price = int(input("Цена товара: "))
                quantity = int(input("Количество товара: "))
                if price < 0 or quantity < 0:
                    print("❌ Цена и количество должны быть положительными числами.")
                    continue
                if not pid or not name or not category:
                    print("❌ Все поля обязательны для заполнения.")
                    continue
                add_product(pid, name, category, price, quantity)
            except ValueError:
                print("❌ Пожалуйста, введите корректные числа для цены и количества.")

        elif choice == 2:
            time.sleep(0.5)
            pid = input("Введите ID который хотите удалить: ").strip()
            if not pid:
                print("❌ ID не может быть пустым.")
                continue
            remove_product(pid)

        elif choice == 3:
            time.sleep(0.5)
            pid = input("ID товара: ").strip()
            if not pid:
                print("❌ ID не может быть пустым.")
                continue
            try:
                new_price = int(input("Введите новую цену: "))
                if new_price < 0:
                    print("❌ Цена должна быть положительным числом.")
                    continue
                update_price(pid, new_price)
            except ValueError:
                print("❌ Пожалуйста, введите корректную цену.")
        
        elif choice == 4:
            time.sleep(0.5)
            pid = input("ID товара: ").strip()
            if not pid:
                print("❌ ID не может быть пустым.")
                continue
            try:
                new_quantity = int(input("Введите новое количество товара: "))
                if new_quantity < 0:
                    print("❌ Количество должно быть положительным числом.")
                    continue
                update_quantity(pid, new_quantity)
            except ValueError:
                print("❌ Пожалуйста, введите корректное количество.")

        elif choice == 5:
            time.sleep(0.5)
            show_sklad()


if __name__ == "__main__":
    sklad_menu()