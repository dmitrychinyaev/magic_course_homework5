# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.
import csv

total = 0
max = 0
max_product = ''

with open('sales.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for line in reader:
        sum_of_product = float(line['quantity']) * float(line['price'])
        total += sum_of_product
        if(sum_of_product > max):
            max_product = line['product']

print(total, max_product)