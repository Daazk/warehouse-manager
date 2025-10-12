#!/usr/bin/env python3
"""
Демонстрационный скрипт для тестирования системы управления складом
"""

from sklad import add_product, show_sklad
from clients import add_client, show_clients
from orders import create_order, show_orders
import os

def create_demo_data():
    """Создаёт демонстрационные данные для тестирования"""
    
    print("🚀 Создание демонстрационных данных...")
    
    # Добавляем товары на склад
    print("\n📦 Добавление товаров на склад:")
    add_product("001", "Ноутбук Lenovo", "Электроника", 25000, 10)
    add_product("002", "Мышь Logitech", "Периферия", 1500, 25)
    add_product("003", "Клавиатура механическая", "Периферия", 3500, 15)
    add_product("004", "Монитор 24\"", "Электроника", 15000, 8)
    
    # Добавляем клиентов
    print("\n👥 Добавление клиентов:")
    add_client("123", "Иван Иванов", "+380501234567", "ivan@example.com")
    add_client("456", "Петр Петров", "+380671234567", "petr@example.com")
    add_client("789", "Анна Сидорова", "+380931234567", "anna@example.com")
    
    # Создаём заказы
    print("\n🧾 Создание заказов:")
    create_order("order001", "123", {"001": 1, "002": 2})
    create_order("order002", "456", {"003": 1, "004": 1})
    
    print("\n✅ Демонстрационные данные созданы!")
    print("\n" + "="*50)
    print("ТЕКУЩЕЕ СОСТОЯНИЕ СИСТЕМЫ:")
    print("="*50)
    
    show_sklad()
    show_clients()
    show_orders()

if __name__ == "__main__":
    create_demo_data()
