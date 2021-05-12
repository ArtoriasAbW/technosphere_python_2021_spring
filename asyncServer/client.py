import socket
import threading
import sys

# - Подготовить файл с запросами (порядка 100 URL разных); - На вход клиенту передаётся два аргумента --- файл с
# URL'ами и M (количество потоков); - Клиент отправляет параллельно M запросов на сервер и печатает ответ сервера в
# стандартый вывод, то есть, например: `xxx.com: {'word1': 100, 'word2': 50}`
import time

host = 'localhost'
port = 15000


def send_url(url):
    with socket.create_connection((host, port), 5) as s:
        # set socket read timeout
        s.settimeout(10)
        try:
            s.send(url.encode())
            most_common = s.recv(4096)
        except socket.timeout:
            print('send data timeout')
        except socket.error as ex:
            print('send data error: ', ex)
        else:
            print('{}: {}'.format(url, most_common.decode()))


def split_urls(urls, n):
    for i in range(0, len(urls), n):
        yield urls[i:i + n]


def process_urls(num_threads, file_name):
    with open(file_name, 'r') as urls_file:
        urls = split_urls(urls_file.read().splitlines(), num_threads)
    for urls_part in urls:
        threads = [threading.Thread(target=send_url, args=(url,)) for url in urls_part]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    begin = time.time()
    process_urls(int(sys.argv[1]), sys.argv[2])
    end = time.time()
    print(end - begin)
