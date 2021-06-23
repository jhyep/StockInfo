#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


base_url = 'https://finance.naver.com/item/news_read.nhn?article_id=0001852070&office_id=016&code=005930&page=&sm=title_entity_id.basic'
r=requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')
result = soup.find_all(attrs={'id':'news_read'})

for tag in result:
	content = tag.text
print(content)	


