import socket
import sys
from collections import Counter
from string import punctuation
import json
import threading

import requests
from bs4 import BeautifulSoup

# - Мастер и воркеры это разные потоки в едином приложении; - Мастер слушает порт, на который клиент будет по TCP
# отправлять урлы для обкачки; - Мастер принимает запрос, читает url от клиента и передаёт этот url одному из
# воркеров; - Воркер обкачивает url по https и возвращает клиенту топ K самых частых слов и их количества в формате
# json; - После каждого обработанного урла сервер должен вывести статистику: сколько урлов было обработано на данный
# момент суммарно всеми воркерами;


# скорее всего нужно асинхронно принимать соединения а потом запускать обработку урла в треде, но
# опять же не очень понятно как создать начальный список тредов и выбирать оттуда незанятый (и как возвращать потом)

def master(n_workers, n_words):
    with socket.socket() as server_sock:
        server_sock.bind(('localhost', 15000))
        server_sock.listen()
        workers = []
        while True:
            connection, addr = server_sock.accept()
            with connection:
                while True:
                    data = connection.recv(4096)
                    if not data:
                        break
                    else:
                        threading.Thread(target=worker, args=(connection, data.decode(), n_words)).start()


def worker(client_socket, url, n_words):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="html.parser")
    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    client_socket.send(json.dumps(dict(c.most_common(n_words)), ensure_ascii=False).encode('utf8'))


def parse_args(args):
    workers_num = 1
    words_num = 1
    prev = None
    for arg in args:
        if prev is not None:
            if prev == '-w':
                workers_num = int(arg)
            elif prev == '-k':
                words_num = int(arg)
        prev = arg
    return workers_num, words_num


if __name__ == '__main__':
    workers_n, words_n = parse_args(sys.argv)
    master(workers_n, words_n)
