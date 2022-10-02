import requests
from bs4 import BeautifulSoup
from lxml import html
import urllib3
import os
import time
import shutil

if not os.path.isdir("data"):
     os.mkdir("data")
path = os.getcwd()
try:
    shutil.rmtree(path + '/data')
except OSError as error:
    print(error)
    print('Не получается удалить файл')
except FileNotFoundError as e:
    print('Папки data нет в данной директории')
if not os.path.isdir("data"):
     os.mkdir("data")
f = open('urls.txt', 'w')
f.close()


def function_save_page(k,url): 
    response = requests.get(url)
    f = open(f'data/{k + 1}.html', 'w' )
    f.write(response.text)
    f.close()


def function_correction_url(cor_url, main_url):
    if (cor_url.find(main_url.split('/')[2].split('.')[0]) != -1) and (cor_url.startswith('https://') == True)  : #Чтобы только внутренние страницы парсились
        return cor_url
    else: 
        return 'dropnetsya'


def function_download_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    new_url = []
    for link in soup.find_all('a', href=True):
            new_url.append(link['href'])
    drop_nedrujestvenniye_strany_link= ['linkedin','instagram','twitter','meta', 'facebook','dropnetsya','discord','twitch','tl.net']       
    for i in range(len(new_url)):
        new_url[i] = function_correction_url(new_url[i], url)
        if any(x in  new_url[i] for x in drop_nedrujestvenniye_strany_link):
            new_url[i] = None
    g = open('urls.txt', 'r')
    lines = g.readlines()
    try:
        n = int(lines[-1].split()[0])
    except IndexError:
        n = 0
    g.close()
    nn = list(filter(None, new_url))[0:4] #ограничение на кол-во выгружаемых ссылок. Поставили, чтобы быстрее работало и сайт не банил
    f = open('urls.txt', 'a')
    for i in range(len(nn)):
        f.write(str(i + 1 + n)+' '+nn[i] + '\n')
        function_save_page(i + n, nn[i])
    f.close()
    return nn
    

print('Введите начальный url:')
url = input()
print('Введите глубину обхода:')
glubina = int(input())
urls = [url]

for i in range(glubina + 1): 
    new_urls = []
    for n in range(len(urls)):
        new_urls.append(function_download_urls(urls[n]))
    urls = list(filter(None,list(set([a for b in new_urls for a in b]))))
