#!/usr/bin/env python

import os
import datetime
import urllib.request
from bs4 import BeautifulSoup
from time import sleep, strftime
from termcolor import colored


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
            karikatür = urllib.request.urlretrieve(URL[1].replace(' ','%20'), 'arşiv/' + URL[0] + '.jpg')
            print(colored('[+]', 'green'),'{0:>25} | [{2}] | .{1} '.format(URL[0],URL[1][23:],tarih))
        except:
            print(colored('[-]', 'red'), 'URL: ' + URL[1] + ' Alt: ' + URL[0])

tarih = strftime('%Y-%m-%d')
kullanıcıGirişi = input('Komikaze.NET karikatür arşivi indirilecek. Onaylıyor musunuz [E/H] >> ')
geçiciDeğişken = ''

if kullanıcıGirişi == 'E' or kullanıcıGirişi == 'e':
    if os.path.exists('arşiv'):
        print(colored('[+]','green'), colored('Arşiv klasörü bulundu.', 'blue'))
    else:
        os.makedirs('arşiv')
        print(colored('[+]','green'), colored('Arşiv klasörü oluşturuldu.', 'blue'))

    print(colored('Komikaze.NET','red'))
    while tarih != '2014-01-12':
        sayfaKaynakKodu = sayfayıYükle(tarih)
        karikatür = karikatürURL(sayfaKaynakKodu)
        karikatürİndir(karikatür, geçiciDeğişken, tarih)
        geçiciDeğişken = karikatür[1]
        tarih = öncekiGün(tarih)
