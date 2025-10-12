import time
from sklad import sklad_menu
from clients import client_menu
from orders import order_menu

# ------------ Меню (главное) -------------

def main_menu():                    # ------------- Главное меню
    while True:
        print("\n---------Главное меню---------")
        print("1.📦Склад")
        print("2.📋Клиенты")
        print("3.✅Заказы ")
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


if __name__ == "__main__":
    main_menu()