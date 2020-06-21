#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

link_count = int(input('[*] Links count: '))
dns_zone = input('[*] Domain zone ex.[.com](Enter to pass): ')
intext = input('[*] String to be in text(Enter to pass): ')
after = input('[*] URL year(Enter to pass): ')


if dns_zone != '':
    dns_zone = 'site:'+dns_zone
if intext != '':
    intext = 'intext:'+intext
if after != '':
    after = 'after:'+str(int(after)-1)


counter = 0
with open('dork_list.txt', 'r') as dorks:
    for dork in dorks:
        query = 'https://www.google.com/search?q={0} inurl:{1} {2} {3}'.format(intext, dork, after, dns_zone)
        print(query)
        r = requests.get(query)
        soup = BeautifulSoup(r.text, 'html.parser')
        anti_repeat = ''
        for element in soup.find_all('a'):
            if counter >= link_count or link_count == 0:
                print('{0} links successfully grabbed!'.format(link_count))
                exit()
            link = element['href']
            prefix = '/url?q='
            if link.startswith(prefix):
                w = link.split('.')[0][len(prefix) + 8:]
                is_www = w == 'www' or w == 'ww'
                if is_www:
                    if anti_repeat != link.split('.')[1]:
                        anti_repeat = link.split('.')[1]
                        link = link[len(prefix):]
                        print('[URL] ' + link)
                        counter += 1
                elif not is_www and w != 'accounts':
                    if anti_repeat != w:
                        anti_repeat = w
                        link = link[len(prefix):]
                        print('[URL] ' + link)
                        counter += 1
