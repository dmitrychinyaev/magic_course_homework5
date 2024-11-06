# В файле users.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.
import json

def show_user_over_30_by_prof(profession : str):
    with open('users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        for user in data:
            if user["age"] > 30 and user["profession"] == profession:
                print(user)

prof_to_find = input("Введите профессию для поиска: ")
show_user_over_30_by_prof(prof_to_find)