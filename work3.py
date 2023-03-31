import time
import sys
from datetime import datetime, timedelta
import requests


def time_now():  # Определяем функцию где будем получать текущее время
    time = datetime.today() - timedelta(days=2)  # Из текущей даты отнимаем два дня
    return time.strftime('%Y-%m-%d')  # Преобразуем дату в удобный формат


def data_now(data):  # Определяем функцию, которая преобразует timestamp в удобный вид
    result = datetime.fromtimestamp(data)  # Передаем timestamp, получаем дату с временем и сохраняем в переменную
    return result  # Возвращаем данные


def get_page(page_num):  # Определяем функцию, которая выполняет запрос. На вход функция принимает номер страницы
    response = requests.get(
        "https://api.stackexchange.com/2.3/questions",
        headers={'Accept': 'application/json'},
        params={
            "tagged": "Python",  # Указываем tag
            "fromdate": time_now(),  # Вызываем функцию, которая вернет дату за вычетом два дня
            "order": "desc",  # Сортируем в обратном порядке
            "site": "stackoverflow",
            "sort": "creation",  # Сортируем по дате создания
            "page": page_num,  # Передаем переменную, содержащую страницу
            "pagesize": 100,  # Указываем лимит
        }
    )
    if response.status_code != 200:
        sys.exit("Ошибка в запросе")
    return response.json()


def all_questions():  # Определяем функцию, где будем выводить на консоль все вопросы
    page_num = 1  # Создаем переменную, означающую что это первая страница
    while True:  # Определяем бесконечный цикл, чтобы получить все данные, т.к. может быть несколько страниц с данными
        temp_page_list = get_page(
            page_num)  # Вызываем функцию, которая делает запрос и передаем в нее переменную, содержащую страницу. Ответ сохраняем в переменную
        page_list = temp_page_list["items"]  # Получаем из ответа запроса данные
        for page in page_list:  # Проходим в цикле по данным
            print(page['title'])  # Печатаем заголовок
            print(data_now(page['creation_date']))  # В функцию преобразования даты передаем дату создания вопроса
            print(f'\n{"-" * 30}\n')
        if not temp_page_list['items'] :  # Если больше данных нет, то прерываем бесконечный цикл.
            break
#        print(page_num)
        page_num += 1  # Увеличиваем страницу на один
        time.sleep(0.3)  # Делаем паузу на пол секунды, чтобы не заблокировал ресурс из-за большого количества запросов за короткий промежуток времени


if __name__ == '__main__':
    all_questions()  # Вызываем функцию вывода вопросов
