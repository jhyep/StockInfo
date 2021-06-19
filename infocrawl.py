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


if __name__ == '__main__':
    
    #종목 코드 받아오는 기능 추가할 것

    url = 'https://finance.naver.com/item/main.nhn?code=005930'
    res = requests.get(url)
    
    html = BeautifulSoup(res.content, "html.parser")
    html_chart = html.find(attrs={'class':'section cop_analysis'})
    chart = html_chart.find('tbody')
    data = chart.find_all('tr')

    #2020/12 공시 매출액, 영업이익, 당기순이익, PER
    for n in [0,1,2,10]:
        data_f = filter(data[n].get_text()).split()
        print(data_f[2])

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

