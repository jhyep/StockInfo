#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
from flask import Flask, render_template

def filter(string):
    return re.sub('[^0-9,.]',' ',string)


def getStockInfo(stockId):
    
    url = 'https://finance.naver.com/item/main.nhn?code='+stockId
    res = requests.get(url)
    
    html = BeautifulSoup(res.content, "html.parser")
    html_chart = html.find(attrs={'class':'section cop_analysis'})
    chart = html_chart.find('tbody')
    data = chart.find_all('tr')

    #2020/12 공시 매출액, 영업이익, 당기순이익, PER
    indices=[0,1,2,10]
    keys=["공시 매출액", "영업이익", "당기순이익", "PER"]
    dictionary=dict()
    for n in range(4):
        data_f = filter(data[indices[n]].get_text()).split()
        dictionary[keys[n]]=float(re.sub(',','',data_f[2]))
    
    return dictionary


def getIndex():
    #KOSPI, KOSDAQ 지수
    url2 = 'https://finance.naver.com/sise/'

    fp = urllib.request.urlopen(url2)
    source = fp.read()
    fp.close()

    html2 = BeautifulSoup(source, "html.parser")
    html2 = html2.findAll("span", class_="num")

    kospi_value = html2[0].string
    kosdaq_value = html2[1].string
    print('코스피 지수: ' + kospi_value)
    print('코스닥 지수: ' + kosdaq_value)

if __name__=='__main__':
    print(getStockInfo('005930'))
