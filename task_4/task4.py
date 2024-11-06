#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.
import csv

with open('employees.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for line in reader:
        if int(line['salary']) > 50000:
            print(line)