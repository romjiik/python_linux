import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import random
import re
import urllib3 #pip install urllib3

http = urllib3.PoolManager()

def function_correction_url(cor_url, main_url):
    #if cor_url.startswith('https://'):
    if (cor_url.find(main_url.split('/')[2].split('.')[0]) != -1)  : #Чтобы только внутренние страницы парсились
        return cor_url
    elif cor_url.startswith('https://') == False:
        return 'https://' + main_url.split('/')[2] + '/' + cor_url
    else: 
        return 'dropnetsya'
        #return 'https://' + main_url.split('/')[2] + '/' + cor_url

def function_download_urls(url):
    
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="lxml")
    
    new_url = []
    for link in soup.find_all('a', href=True):
            new_url.append(link['href'])
    
    drop_nedrujestvenniye_strany_link= ['linkedin','instagram','twitter','meta', 'facebook','dropnetsya']        
    
    for i in range(len(new_url)):
        new_url[i] = function_correction_url(new_url[i], url)
        if any(x in  new_url[i] for x in drop_nedrujestvenniye_strany_link):
            new_url[i] = None

    return list(filter(None, new_url))

glubina = 1
urls = ['https://stackoverflow.com/questions/743806/how-do-i-split-a-string-into-a-list-of-words']

#for i in range(glubina + 1): 
    #new_urls = []
    #for n in range(len(urls)):
        #new_urls = new_urls.append(function_download_urls(urls[n]))
        #print(new_urls)
    #urls = list(set([a for b in new_urls for a in b]))

#print(len(urls))
print(function_download_urls(urls[0]))