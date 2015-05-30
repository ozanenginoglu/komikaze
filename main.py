#!/usr/bin/env python

import os
import datetime
import argparse
import urllib.request
from bs4 import BeautifulSoup
from time import sleep, strftime

if not os.path.exists('arşiv'):
    os.makedirs('arşiv')

def sayfayıYükle(tarih):
    url = 'http://www.komikaze.net/komikaze/'
    url += tarih
    while True:
        try:
            kaynak_kodu = urllib.request.urlopen(url)
            break
        except:
            sleep(1)
            print('Bir saniye bekleniyor.')
    soup = BeautifulSoup(kaynak_kodu)
    return soup

def öncekiGün(tarih):
    tarih = datetime.date(*map(int, tarih.split('-')))
    öncekiGün = tarih - datetime.timedelta(days=1)
    öncekiGün.strftime('%Y-%m-%d')
    return str(öncekiGün)

def karikatürURL(soup):
    link = soup.find('img', {'class': 'caricature-img'})
    url = link['src']
    alt = link['alt']
    return alt, url

def karikatürİndir(URL, öncekiURL, tarih):
    if URL[1] != öncekiURL:
        try:
            karikatür = urllib.request.urlretrieve(URL[1], 'arşiv/' + URL[0] + '.jpg')
            print('[+] ' + URL[0] + ' - ' + URL[1] + ' [' + tarih + ']')
        except:
            print('[-] Karikatür indirilirken problem oluştu. URL: ' + URL[1])

tarih = strftime('%Y-%m-%d')
kullanıcıGirişi = int(input('Kaç günlük karikatür arşivi indirilecek >> '))
geçiciDeğişken = ''

for i in range(kullanıcıGirişi):
    soup = sayfayıYükle(tarih)
    çıktı = karikatürURL(soup)
    karikatürİndir(çıktı, geçiciDeğişken, tarih)
    geçiciDeğişken = çıktı[1]
    tarih = öncekiGün(tarih)
