#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
import math
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk import word_tokenize
#from konlpy.tag import Kkma
import project

word_d = {}
sent_list = []

#특수문자 걸러내기
def hfilter(s):
    return re.sub(u'[^a-zA-Z\u3130-\u318f\uac00-\ud7a3]',' ',s)

#조사 접미사 걸러내기
def filter_pos(s):
    return re.sub(u'[와과을를들]',' ',s)

#토큰화
def process_new_sentence(s):
    sent_list.append(s)
    tokenized = word_tokenize(s)
    #tokenized = Kkma().pos(s)
    #print(tokenized)
    for word in tokenized:
        if word not in word_d.keys():
            word_d[word]=0
        word_d[word] += 1

#tf 계산
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

#idf 계산
def compute_idf():
    Dval = len(sent_list)
    bow = set()

    for i in range(0, len(sent_list)):
        tokenized = word_tokenize(sent_list[i])
        for tok in tokenized:
            bow.add(tok)

    idf_d = {}
    for t in bow:
        cnt = 0
        for s in sent_list:
            if t in word_tokenize(s):
                cnt += 1
        idf_d[t] = math.log(Dval/float(cnt))
    
    return idf_d


if __name__ == '__main__':

    base_url = 'https://finance.naver.com//item/news_news.nhn?code=005380&page={}&sm=title_entity_id.basic&culsterld='

    for i in range(5):
        url = base_url.format(i+1)
        webpage = urlopen(url)
        soup=BeautifulSoup(webpage, 'html.parser')

        result = soup.findAll('td', attrs={'class':'title'})
        for tag in result:
            title_no_mark = hfilter(tag.a.text)
            news_title = filter_pos(title_no_mark)
            process_new_sentence(news_title)

    #중복 단어 걸러내기 위한 딕셔너리 생성
    tfidf = {}

    idf_d = compute_idf()
    for i in range(0, len(sent_list)):
        tf_d = compute_tf(sent_list[i])

        for word, tfval in tf_d.items():
            #딕셔너리에 단어: tfidf 값 추가
            tfidf[word] = tfval*idf_d[word]
    #많이 나오는 단어가 값이 낮게 나와 추가한 오름차순 정렬(...)
    tfidf = sorted(tfidf.items(), key=lambda item:item[1])
    print(tfidf[:20])
