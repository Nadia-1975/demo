# ЗАДАНИЕ-2



import requests
import json
from pprint import pprint






def best_hero(heroes: list):
    result=0
    heroes_dict = {}  # Определяем пустой словарь, где ключи - это имена героев, а значения - их интелект
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    answer_site = requests.get(
        url)  # Используя библиотеку requests, делаем get запрос по url. Полученный ответ сохраняем в переменную
    if answer_site.status_code != 200:  # Проверяем имеем ли статус 200
        print('Ошибка сервера.')
    else:
        print('200, веселуха началась')
    list_heroes = answer_site.json()  # Получаем данные из ответа и сохраняем в переменную. Здесь у нас список из геров, который хранится в отдельном словаре
    for hero in list_heroes:  # Проходим в цикле по героям
        name_heroes = hero['name']  # Получаем имя героя из словаря и сохраняем в переменную
        if name_heroes in heroes:  # Проверяем есть ли герой в искомом списке супергероев
            heroes_dict[name_heroes] = hero['powerstats']['intelligence']  # Сохраняем героя в наш ранее созданный словарь
            hero_name, hero_intellect = max(heroes_dict.items(), key=lambda x: x[1])  # Получаем героя с максимальным интелектом, где вернется кортеж и распаковываем его сразу в две переменные
            result = (f"\nСамый умный супергерой: {hero_name} - его интелект: {hero_intellect}")
    return result

print(best_hero(['Hulk', 'Captain America', 'Thanos']))