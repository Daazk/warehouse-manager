import time
from utils import logging, load_json, load_all_clients, load_all_orders, SKLAD_FILE, CLIENTS_DIR, ORDERS_DIR
from reporting import generate_report
from sklad import sklad_menu
from clients import client_menu
from orders import order_menu


# ------------ Меню (главное) -------------

def main_menu():     
    """Функция выводит главное меню"""

    while True:
        print("\n---------Главное меню---------")
        print("1.📦Склад")
        print("2.📋Клиенты")
        print("3.✅Заказы ")
        print("4.📊Отчёт")
        print("0.❌Выход")
        try:
            choice = int(input("Введите номер пункта: "))
        except ValueError:
            print("❌ Пожалуйста, введите число.")
            continue

        if choice == 0:
            time.sleep(0.5)
            print("Выход.")
            break

        elif choice == 1:
            time.sleep(0.5)
            sklad_menu()
        
        elif choice == 2:
            time.sleep(0.5)
            client_menu()

        elif choice == 3:
            time.sleep(0.5)
            order_menu()

        elif choice == 4:
            sklad_data = load_json(SKLAD_FILE)
            clients_data = load_all_clients(CLIENTS_DIR)
            orders_data = load_all_orders(ORDERS_DIR)
            
            generate_report(
                sklad=sklad_data,
                clients=clients_data,
                orders=orders_data
            )

            time.sleep(0.5)
            print("📊 Отчёт успешно создан!")
            logging.info("Отчёт успешно создан.")

if __name__ == "__main__":
    main_menu()