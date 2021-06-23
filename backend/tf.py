#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
import math
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk import word_tokenize
#from konlpy.tag import Kkma

word_d = {}
sent_list = []

def hfilter(s):
    return re.sub(u'[^0-9a-zA-Z\u3130-\u318f\uac00-\ud7a3]',' ',s)

def filter_pos(s):
    return re.sub(u'[와과을를들는]',' ',s)

def process_new_sentence(s):
    sent_list.append(s)
    tokenized = word_tokenize(s)
    #tokenized = Kkma().pos(s)
    #print(tokenized)
    for word in tokenized:
        if word not in word_d.keys():
            word_d[word]=0
        word_d[word] += 1

def compute_tf(s):
    bow = set()
    wordcount_d = {}

    tokenized = word_tokenize(s)
    for tok in tokenized:
        if tok not in wordcount_d.keys():
            wordcount_d[tok] = 0
        wordcount_d[tok] += 1
        bow.add(tok)

    tf_d = {}
    for word, count in wordcount_d.items():
        tf_d[word] = count / float(len(bow))

    return tf_d

def getnews(stockId):
    news=[]
    base_url = 'https://finance.naver.com//item/news_news.nhn?code='+stockId+'&page={}&sm=title_entity_id.basic&culsterld='

    for i in range(5):
        url = base_url.format(i+1)
        webpage= urlopen(url)
        soup = BeautifulSoup(webpage, 'html.parser')

        result = soup.findAll('td', attrs={'class':'title'})
        for tag in result:
            content = hfilter(tag.a.text)
            news_title = filter_pos(content)
            news.append(news_title)
    return news

if __name__ == '__main__':
    
    titles = filter_pos(hfilter((str(getnews('352820')))))
    process_new_sentence(titles)
    
    tf = {}
    
    for i in range(0, len(sent_list)):
        tf_d = compute_tf(sent_list[i])
        
        for word, tfval in tf_d.items():
            tf[word] = tfval
    tf = sorted(tf.items(), key=lambda item:item[1], reverse=True)
    
    #빈도수 가장 높은 단어 20개 출력
    print(tf[:20])
