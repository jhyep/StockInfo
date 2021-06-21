#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getnews(stockId):
	news=[]	
	base_url = 'https://finance.naver.com//item/news_news.nhn?code='+stockId+'&page={}&sm=title_entity_id.basic&culsterld='

	for i in range(5):
		url = base_url.format(i+1)	
		webpage = urlopen(url)
		soup=BeautifulSoup(webpage, 'html.parser')

		result = soup.findAll('td', attrs={'class':'title'}) 
		for tag in result:
			content = tag.a.text
			news.append(content)
	return news	

"""
if __name__ == '__main__':
	company1=getnews('005930')
	str1="".join(company1)
	print(str1)
	company2=getnews('102280')
	str2="".join(company2)
	print(str2)
	company3=getnews('068270')
	str3="".join(company3)
	print(str3)
"""
