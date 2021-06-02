#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
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
