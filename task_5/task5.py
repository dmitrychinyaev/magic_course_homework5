# Система учета заказов

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.

# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.
import json

with open("orders.json", "r") as file:
    data = json.load(file)

    orders = data['orders']
    max_client = ''
    max_price = 0

    for order in orders:
        price = 0
        for item in order['items']:
            price = item['quantity'] * item['price']
             
        print(price)
        if price > max_price:
            max_price = price
            max_client = order['customer']['name']

    print(max_client, max_price)




