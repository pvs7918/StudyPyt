# Задание №3
# Написать программу, которая считывает список из 10 URL-адресов и
# одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте асинхронный подход.

import asyncio
import aiohttp
import time
import requests

urls = [
    'https://python.org',
    'https://mail.ru',
    'https://practicum.yandex.ru',
    'https://gb.ru/geek_university/developer/programmer/python',
    'https://netology.ru/programs/python',
    'https://synergyacademy.com/program/python-razrabotchik',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://tproger.ru/articles/podrobnoe-opisanie-jazyka-python-dlja-nachinajushhih',
    'https://github.com/python',
    'https://habr.com/ru/articles/450474/'
]

async def download(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = f'site_{i}.html'
            text = await response.text()

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)
            print(url)

async def main():
    tasks = []
    for index, url in enumerate(urls):
        tasks.append(asyncio.create_task(download(url, index)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end = time.time()

    print(end - start)
    print('Готово!')
