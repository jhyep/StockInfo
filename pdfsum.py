#!/usr/bin/python3
#-*- coding: utf-8 -*-

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from gensim.summarization.summarizer import summarize
from newspaper import Article
from konlpy.tag import Kkma
import re

kkma = Kkma()

def convert_pdf_to_txt(file_path):
    
    output_string = StringIO()
    with open(file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string,laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())

def hfilter(s):
    return re.sub(u'[^.a-zA-Z\u3130-\u318f\uac00-\ud7a3]',' ',s)

#def preprocessing(s):
    #total_text = ''

    #for line in range(len(s)):

if __name__=='__main__':
    
    v = convert_pdf_to_txt('/home/jhp/1624319090497.pdf') 
    #print(v)
    print(summarize(v, ratio=0.1))
