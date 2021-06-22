#!/usr/bin/python3

import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def hfilter(s):
	return re.sub(u'[^a-zA-Z\u3130-\u318f\uac00-\ud7a3]',' ',s)

def filter_pos(s):
	return re.sub(u'[와과을를들]',' ',s)

def getnews(stockId):
	news=[]	
	base_url = 'https://finance.naver.com//item/news_news.nhn?code='+stockId+'&page={}&sm=title_entity_id.basic&culsterld='

	for i in range(5):
		url = base_url.format(i+1)	
		webpage = urlopen(url)
		soup=BeautifulSoup(webpage, 'html.parser')

		result = soup.findAll('td', attrs={'class':'title'}) 
		for tag in result:
			content = hfilter(tag.a.text)
			news_title = filter_pos(content)	
			news.append(news_title)
	return news	














