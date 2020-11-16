import requests
from bs4 import BeautifulSoup
import json

URL = 'http://dop.edu.ru/organization/list?orientation=3&region=42&page=1&perPage=20'
#'http://dop.edu.ru/organization/list?orientation=3&region=42%2C25%2C15&page=1&perPage=20'
KORT = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
st_res = []


def getting_document(url, params=None):
    '''Using for getting html document with params'''
    zap_1 = requests.get(url, headers=KORT, params=params)
    return zap_1

def content_maker(document):
    '''Using to form structured content from a html-page'''
    maker = str(BeautifulSoup(document, 'html.parser'))
    bugai = json.loads(maker)
    for i in range(len(bugai['data']['list'])):
        fale1.write('\n')
        fale1.write(bugai['data']['list'][i]['name'] + ',' + bugai['data']['list'][i]['full_name'] + ',' + bugai['data']['list'][i]['site_url'])


def parsing():
    '''Using for parsing html-document'''
    document = getting_document(URL)
    if document.status_code == 200:
        content_maker(document.text)
    else:
        print('ERROR: no response received from the site')

fale1 = open('thebest.csv', 'w', encoding='utf-8')
fale1.write('name,full_name,website_address')
parsing()
print('finished!')
