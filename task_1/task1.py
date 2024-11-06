# Напишите программу, которая сравнивает два JSON-файла
# (file1.json и file2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.
import json

def compare_json(filepath1 : str, filepath2 : str):
        
    with open(filepath1, 'r') as f1:
        json1 = json.load(f1)
    with open(filepath2, 'r') as f2:
        json2 = json.load(f2)

    for key in json1.keys():
        if key not in json2:
            print(f"Ключ '{key}' присутствует в {filepath1}, но отсутствует в {filepath2}")
        if json1[key] != json2[key]:
            print(f"Значение для ключа '{key}' разное в {filepath1} и {filepath2}: {json1[key]} vs {json2[key]}")
        
    for key in json2.keys():
        if key not in json1:
            print(f"Ключ '{key}' присутствует в {filepath2}, но отсутствует в {filepath1}")

compare_json('file1.json', 'file2.json')              

#Красивый вывод подсмотрел) 