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

def newssum(url):
    
    r=requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    result = soup.find_all(attrs={'id':'news_read'})

    for tag in result:
        content = tag.text

    return summarize(content)
