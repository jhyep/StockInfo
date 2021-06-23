  
#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
import urllib.request
from bs4 import BeautifulSoup
from gensim.summarization.summarizer import summarize
from newspaper import Article
from konlpy.tag import Kkma

kkma = Kkma()

def hfilter(s):
    return re.sub(u'[^.a-zA-Z\u3130-\u318f\uac00-\ud7a3]',' ',s)

if __name__=='__main__':
    
    url = 'https://finance.naver.com/item/news_read.nhn?article_id=0000735435&office_id=366&code=o96770&page=&sm=title_entity_id.basic'
    r=requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all(attrs={'id':'news_read'})

    for tag in result:
        content = tag.text
    #print(content)

    #v = convert_pdf_to_txt('/home/jhp/1624319090497.pdf') 
    #print(v)
    print(summarize(content))
