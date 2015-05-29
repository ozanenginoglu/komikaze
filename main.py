#!/usr/bin/env python

import urllib.request
import datetime
from time import sleep, strftime
from bs4 import BeautifulSoup

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
    bugün = datetime.date(*map(int, tarih.split('-')))
    öncekiGün = bugün - datetime.timedelta(days=1)
    öncekiGün.strftime('%Y-%m-%d')
    return öncekiGün

öncekiGün()
tarih = strftime('%Y-%m-%d')
