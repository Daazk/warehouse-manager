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
        print(f"🔄 Количество товара {sklad[product_id]["name"]} обновлено: {new_quantity}.")
    else:
        time.sleep(0.5)
        print("❌ Товар не найден.")

def update_price(product_id, new_price):          # ------------- Изменить цену товара
    sklad = load_json(SKLAD_FILE)
    if product_id in sklad:
        sklad[product_id]["price"] = new_price
        save_json(SKLAD_FILE, sklad)
        time.sleep(0.5)
        print(f"🔄 Цена на товар {sklad[product_id]["name"]} обновлена: {new_price}")
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

        choise = int(input("Введите номер пункта: "))
        if choise == 0:
            time.sleep(0.5)
            print("Выход в главное меню.")
            break

        elif choise == 1:
            time.sleep(0.5)
            pid = input("ID товара: ")
            name = input("Название товара: ")
            category = input("Категория товара:")
            price = int(input("Цена товара: "))
            quantity = int(input("Количество товара: "))
            add_product(pid, name, category, price, quantity)

        elif choise == 2:
            time.sleep(0.5)
            pid = input("Введите ID который хотите удалить: ")
            remove_product(pid)

        elif choise == 3:
            time.sleep(0.5)
            pid = input("ID товара: ")
            new_price = int(input("Введите новую цену: "))
            update_price(pid, new_price)
        
        elif choise == 4:
            time.sleep(0.5)
            pid = input("ID товара: ")
            new_quantity = int(input("Введите новое количество товара: "))
            update_quantity(pid, new_quantity)

        elif choise == 5:
            time.sleep(0.5)
            show_sklad()


if __name__ == "__main__":
    sklad_menu()