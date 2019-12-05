# import requests
# from bs4 import BeautifulSoup
#
# from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.naver                      # 'dbsparta'라는 이름의 db를 만듭니다
#
# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')
#
# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')
#
# # movies (tr들) 의 반복문을 돌리기
# rank = 1
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         title = a_tag.text
#         star = movie.select_one('td.point').text
#         print(rank,title,star)
#         doc = {
#             'rank': rank,
#             'title': title,
#             'star': star
#         }
#         db.movies.insert_one(doc)
#         rank += 1


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.naver

# target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
# print (target_movie['star'])


# target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
# target_star = target_movie['star']
#
# movies = list(db.movies.find({'star':target_star}))
#
# for movie in movies:
#     print(movie['title'])


# target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
# target_star = target_movie['star']

#
# db.movies.update_many({'star':target_star},{'$set':{'star':0}})
# result = list(db.movies.find({'star':0}))
# for r in result:
#     print(r)


# star의 type을 float으로 변환
movies = db.movies.find()
for movie in movies:
    db.movies.update_one(
        {'title':movie['title']},
        {'$set':{'star': float(movie['star'])}}
    )


# gte는 grater than & equal, lt는 lower than / 별점이 9.45 이상 9.7 미만을 검색
new_movies = list(db.movies.find({'star':{'$gte':9.45, '$lt':9.7}}))
for movie in new_movies:
    print(movie)