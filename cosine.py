#!/usr/bin/python3
import numpy
from nltk import word_tokenize
import project

word_d={}
sent_list=[]








def process_new_sentence(s):
	sent_list.append(s)
	tokenized = word_tokenize(s)
	for word in tokenized:
		if word not in word_d.keys():
			word_d[word]=0
		word_d[word]+=1

def make_vector(i):
	v=[]
	s=sent_list[i]
	tokenized = word_tokenize(s)
	for w in word_d.keys():
		val=0
		for t in tokenized:
			if t==w:
				val+=1
		v.append(val)
	return v	

if __name__ == '__main__':
	process_new_sentence(str(project.getnews('005930')))
	process_new_sentence(str(project.getnews('102280')))
	process_new_sentence(str(project.getnews('068270')))
	v1=make_vector(0)
	v2=make_vector(1)
	v3=make_vector(2)

	dotpro1 = numpy.dot(v1,v2)
	cossimil1 = dotpro1 / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2))
	dotpro2 = numpy.dot(v2, v3)	
	cossimil2 = dotpro2 / (numpy.linalg.norm(v2) * numpy.linalg.norm(v3)) 
	dotpro3 = numpy.dot(v1, v3)
	cossimil3 = dotpro3 / (numpy.linalg.norm(v1) * numpy.linalg.norm(v3))
	print("dot product(첫번째 회사, 두번째 회사) = ", dotpro1)
	print("cos similarity(첫번째 회사, 두번째 회사) =", cossimil1)
	print("dot product(두번째 회사, 세번째  회사) = ", dotpro2)
	print("cos similarity(두번재 회사, 세번째 회사) = ", cossimil2)
	print("dot product(첫번째 회사, 세번째 회사) = ", dotpro3)
	print("cos similarity(첫번째 회사, 세번째 회사) = ", cossimil3)	


