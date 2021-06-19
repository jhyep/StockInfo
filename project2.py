#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = 'https://finance.naver.com//item/news_news.nhn?code=005930&page={}&sm=title_entity_id.basic&culsterld='

for i in range(5):
	url = base_url.format(i+1)	
	webpage = urlopen(url)
	soup=BeautifulSoup(webpage, 'html.parser')

	result = soup.findAll('td', attrs={'class':'title'}) 
	for tag in result:
		print(tag.a.text)
