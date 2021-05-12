from string import punctuation

import aiohttp
import sys
import asyncio
import time
from bs4 import BeautifulSoup
import json
from collections import Counter


# Написать скрипт для обкачки списка урлов с возможностью задавать количество одновременных запросов,
# используя асинхронное программирование. Клиент можно использовать любой, например, из aiohttp.
# Так, 10 одновременных запросов могут задаваться командой:
# python fetcher.py -c 10 urls.txt или python fetcher.py 10 urls.txt

async def download(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        page = await resp.text()
        soup = BeautifulSoup(page, features='html.parser')
        # text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
        # c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
        # print(json.dumps(dict(c.most_common(5)), ensure_ascii=False))


def split_urls(urls, n):
    for i in range(0, len(urls), n):
        yield urls[i:i + n]


async def process_urls(request_num, file_name):
    with open(file_name, 'r') as urls_file:
        urls = list(split_urls(urls_file.read().splitlines(), request_num))
        tasks = []
        t1 = time.time()
        async with aiohttp.ClientSession() as session:
            for urls_part in urls:
                for url in urls_part:
                    tasks.append(asyncio.create_task(download(url, session)))
                await asyncio.gather(*tasks)
                tasks.clear()
        t2 = time.time()
        print('gather: ', t2 - t1)


def parse_args(args):
    request_number = 1
    try:
        request_number = int(args[1])
    except ValueError:
        print('Invalid param value')
        print('Using default request_num = 1')
    return request_number, args[2]


if __name__ == '__main__':
    if len(sys.argv) > 2:
        request_num, file_name = parse_args(sys.argv)
        asyncio.run(process_urls(request_num, file_name))
    else:
        print('Need to specify request_num and file name with urls')
