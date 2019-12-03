# a = 3
# b = 2
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a ^ b)

# x = [0, 1, 2, 3, 4]
# y = [5, 6]
# z = [0 ,5]
# j = {
#     "key1": "value",
#     "key2": 12,
#     "key3": []
# }
#
#
# print(x[3])
# print(len(x))
# print(x+y)
# x.append(10)
# print(x)

# tab 사이즈가 space 2 or space 4 을 인지하여 구분함



# def test(a,b):
#     return a+b
#
# def test2(c,d):
#     return c-d
#
# print(test(1,3) + test2(2,4))


a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(s):
	return s.find('@') > -1
# find는 @가 위치하는 곳을 숫자로 반환, 없으면 -1을 반환 함

#결과값
print(check_mail(a))



a = 'spartacodingclub@gmail.com'

def get_mail(s):
	return s.split('@')[1].split('.')[0]

#결과값
print(get_mail(a))



#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(fruits):
  result = {}
  for element in fruits:
    if element in result:
      result[element] += 1
    else:
      result[element] = 1
  return result

#결과값
print(count_list(a))



import random
# random.sample(전체크기, 뽑을 갯수)  전체크기는 배열로 넣어야 함

def get_lotto():
    lotto_range = range(1, 47)
    lotto_nums = random.sample(lotto_range, 6)
    return lotto_nums

print(get_lotto())




import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print (rjson['RealtimeCityAir']['row'][0]['NO2'])