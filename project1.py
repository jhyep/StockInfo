#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

r=requests.get("https://finance.naver.com//item/news_news.nhn?code=005930&page=&sm=title_entity_id.basic&culsterld=")
soup=BeautifulSoup(r.text, 'html.parser')

result = soup.findAll('td', attrs={'class':'title'}) 
for tag in result:
	print(tag.a.text)
