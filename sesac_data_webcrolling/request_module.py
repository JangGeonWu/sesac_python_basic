import requests

URL = 'http://httpbin.org/get'
#URL = 'https://naver.com'
# get, post, put, delete예 따라 호출하는 메서드도 달라짐
# response = requests.get(URL)

# print(response.status_code)
# print(response.text)

# response_p = requests.post('http://httpbin.org/post')

# print(response_p.status_code)
# print(response_p.text)

# data 크롤링에서는 대부분 get 방식을 사용, 가끔씩 post를 사용하는
# 경우도 있음

# params = {'data1':'data1', 'data2':'data2'}
# response = requests.get(URL, params = params)

# headers = {'Content-Type':'application/json; charset=utf-8'}
# response = requests.get(URL, headers=headers)
# print(response.text)

# body에 데이터를 입력하여 request 가능, 주로 post, put, delete에서 주로 사용한다.
datas = {'data1':'data1', 'data2':'data2'}
URL2 = 'http://httpbin.org/post'
response = requests.post(URL2, data=datas)

print(response.text)