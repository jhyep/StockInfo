# [StockInfo] 2021-1 OSP 10조 TEAM PROJECT
2019114283 박지혜      2019117981 박희원      2017113724 손원준      2020111439 조이

----------------------------------------
## StockInfo?
네이버 금융 페이지에서 데이터를 크롤링하여 관심 기업의 재무상태, 사업 분야가 유사한 기업과 자주 언급되는 토픽을 보여주는 서비스

----------------------------------------
## 중간 발표 ppt
![슬라이드1](https://user-images.githubusercontent.com/80496795/122997641-2d8c2f00-d3e7-11eb-9d97-a64866104ba8.PNG)
![슬라이드2](https://user-images.githubusercontent.com/80496795/122997649-2f55f280-d3e7-11eb-90dc-6086f939e0c8.PNG)
![슬라이드3](https://user-images.githubusercontent.com/80496795/122997652-2f55f280-d3e7-11eb-8e15-7cba036e68c0.PNG)
![슬라이드4](https://user-images.githubusercontent.com/80496795/122997655-2fee8900-d3e7-11eb-9984-a60a8e7655da.PNG)
![슬라이드5](https://user-images.githubusercontent.com/80496795/122997656-30871f80-d3e7-11eb-8e78-2273c0e300a6.PNG)
![슬라이드6](https://user-images.githubusercontent.com/80496795/122997659-30871f80-d3e7-11eb-93ef-abdd9adcf4ed.PNG)
![슬라이드7](https://user-images.githubusercontent.com/80496795/122997660-311fb600-d3e7-11eb-9d99-6b1c4481d193.PNG)
![슬라이드8](https://user-images.githubusercontent.com/80496795/122997662-311fb600-d3e7-11eb-9c74-c8db73d8f6c2.PNG)
![슬라이드9](https://user-images.githubusercontent.com/80496795/122997663-31b84c80-d3e7-11eb-8cc6-afde51b50064.PNG)
![슬라이드10](https://user-images.githubusercontent.com/80496795/122997664-3250e300-d3e7-11eb-8e91-01e8564f9e1e.PNG)
![슬라이드11](https://user-images.githubusercontent.com/80496795/122997665-3250e300-d3e7-11eb-9b24-f3e2460375f2.PNG)
![슬라이드12](https://user-images.githubusercontent.com/80496795/122997669-32e97980-d3e7-11eb-9445-3e0f821d247b.PNG)
![슬라이드13](https://user-images.githubusercontent.com/80496795/122997672-32e97980-d3e7-11eb-84d5-5b83b9bcebf8.PNG)
![슬라이드14](https://user-images.githubusercontent.com/80496795/122997678-33821000-d3e7-11eb-8ee4-32012cb710bd.PNG)
![슬라이드15](https://user-images.githubusercontent.com/80496795/122997680-341aa680-d3e7-11eb-88bc-1edae811355a.PNG)

-----------------------------------------
## 기능 설명
### 1. 종목 코드 검색 기능
종목 코드를 입력을 통해 정보를 얻을 수 있는 해당 프로그램의 특성을 고려하여, 사용자에게 편의를 제공하기 위해 종목 코드 검색 기능을 추가로 제공.

### 2. 종목 정보 검색 기능
검색창에 관심 기업의 종목코드를 입력하였을 시, 해당 기업의 간략한 재무 정보와 유사 종목, 뉴스에서 자주 언급되는 단어들을 볼 수 있음.

#### 2-1. tf 분석
네이버 금융의 뉴스/공시 페이지에 접근하여 뉴스 타이틀의 정보를 크롤링 해온 뒤, tf 분석을 통해 자주 언급된 단어를 분석하였음.
해당 기능은 관심 기업에 어떤 일이 화두가 되고 있는지 간단한 키워드로 확인할 수 있게끔 하기 위해 제공됨.
cf) tf-idf 분석 사용 시 오히려 자주 언급 되는 단어가 필터링 되는 상황이 발생하여 제공되는 본 기능의 목적에 부합하지 않아 tf 분석만 사용함.

#### 2-2. Cosine similarity 분석
네이버 금융의 뉴스/공시 페이지에 접근하여 뉴스타이틀의 정보를 크롤링 해온 뒤, 코사인 유사도 분석을 통해 타 종목과의 유사도를 분석하였음.
해당 기능은 여러 테마에 분포해있는 관심 종목들 중 비슷한 종목들을 묶어서 볼 수 있게끔 하기 위해 제공함.

모든 기능은 hfilter, filter_pos 함수를 추가하여 불용어를 제외한 뒤 결과의 정확도를 높이고자 하였음.
