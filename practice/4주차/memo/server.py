from flask import Flask, render_template, jsonify, request
import requests
# reqeust 는 Flask 안의 패키지이고, requests는 Ajax의 패키지로 서로 다른 것임.
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

app = Flask(
    __name__
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def saving():
    try:
        url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
        comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        url_image = og_image['content']
        url_title = og_title['content']
        url_description = og_description['content']

        article = {'url': url_receive, 'comment': comment_receive, 'image': url_image,
                   'title': url_title, 'desc': url_description}

        db.articles.insert_one(article)

    except Exception as e:
        print(e)
        # 위의 try 문을 실행시킬 때 문제가 발생하면 여기로 빠져나와 작동
        return jsonify({"result": "fail"})

    return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def list_articles():
    try:
        result = list(db.articles.find({},{'_id':0}))
    except Exception as e:
        print(e)
        return jsonify({
            'articles': [],
            'result': 'fail'
        })
    return jsonify({'result':'success', 'articles':result})



if __name__ == '__main__':
    # 아래 코드 의미는 파이썬이 해당 파일(server.py)을 실행시킬때/ 0.0.0.0은 모든 IP로부터의 요청을 허용한다는 의미
    app.run('0.0.0.0', port=5001, debug=True)
