# Задание-1

import requests

from pprint import pprint

#
# TOKEN = '2619421814940190'  # константа токена
# urls = [
#     f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
#     f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
#     f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
# ]  # список адресов
#
#
# def requests_get(url_all):
#     # принимает список адресов
#     r = (requests.get(url) for url in url_all)
#     return r
#
# def parser():
#     # функция парсинга интелекта
#     super_man = []
#     for item in requests_get(urls):
#         intelligence = item.json()
#         try:
#             for power_stats in intelligence['results']:
#                 super_man.append({
#                     'name': power_stats['name'],
#                     'intelligence': power_stats['powerstats']['intelligence'],
#                 })
#         except KeyError:
#             print(f"Проверте ссылки urls: {urls}")
#
#     intelligence_super_hero = 0
#     name = ''
#     for intelligence_hero in super_man:
#         if intelligence_super_hero < int(intelligence_hero['intelligence']):
#             intelligence_super_hero = int(intelligence_hero['intelligence'])
#             name = intelligence_hero['name']
#
#     print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")
#
#
# parser()


# Задание-2
import yadisk

from token_yandex import TOKEN

y = yadisk.YaDisk(token=TOKEN)
if y.check_token():
    if not y.is_dir("/test-dir"):
        y.mkdir("/test-dir")
        print('Папка "test-dir" создана')
print('Содержимое папки "test-dir":\n')

for item in y.listdir('/test-dir/'):
    print(f"Название: {item['name']}")
    print(f'Размер: {item["size"]} байт')
    print(f"Тип файла: {item['type']}")
    print(f"Тип документа: {item['media_type']}")
    print(f"Дата создания: {item['created']}\n")

if y.is_file("/test-dir/test.txt"):
    y.remove('/test-dir/', permanently=True)

    # y.remove("/test-dir/test.txt", permanently=False)
else:
    y.upload("test.txt", "/test-dir/test.txt")
if y.is_file('/test-dir/link_list.txt'):
    y.download('/test-dir/link_list.txt', 'link_list.txt')


# y = yadisk.YaDisk(token='y0_AgAAAABpSGeMAADLWwAAAADehcQ7WUPprK7fSPqY6ss7JpsqrI_qgWg')
# print(y.mkdir('тестовая папка 16.03.23'))
# print(y.remove("test.txt", permanently=True))
# print(y.upload("test.txt", "/test.txt"))
# print(y.download("test.txt", "/test.txt"))











# TOKEN = "y0_AgAAAABpSGeMAADLWwAAAADehcQ7WUPprK7fSPqY6ss7JpsqrI_qgWg"
#
#

