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

        choise = int(input("Введите номер пункта: "))

        if choise == 0:
            time.sleep(0.5)
            print("Выход.")
            break

        elif choise == 1:
            time.sleep(0.5)
            sklad_menu()
        
        elif choise == 2:
            time.sleep(0.5)
            client_menu()

        elif choise == 3:
            time.sleep(0.5)
            order_menu()


if __name__ == "__main__":
    main_menu()