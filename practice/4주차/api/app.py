from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
#"__name__"은 파이썬 문법에서 app.py를 지정하는 역할을 수행

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.naver                     # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
# # route 안의 '/' 는 실질적으로 홈(메인)화면 주소를 가리키는 것
# # "NOT FOUND 404" 오류코드의 404는 웹서버응답 Http status code 중 Not found에 해당하는 코드임
def home():
   return render_template('index.html')
#
# # 아래 @가 붙어있는 것은 그 아래 함수를 꾸며주는 데코이므로 곧바로 붙여서해야만 동작
# @app.route('/mypage')
# def mypage():
#     return 'This is Mypage!'

## API 역할을 하는 부분
# @app.route('/test', methods=['POST'])
# def test_post():
#    title_receive = request.form['title_give']
#    # POST method는 body에 클라이언트 정보가 있으므로 form을 써서 받아옴
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
#
# @app.route('/test', methods=['GET'])
# def test_get():
#    title_receive = request.args.get('title_give')
#    # GET method는 url에 클라이언트 정보가 있으므로 args.get을 써서 받아옴
#    print(title_receive)
#    # 딕셔너리 자료를 jsonify 통해서 json 형태로 변환하여 클라이언트에 반환하는 코드임.
#    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

# @app.route('/test', methods=['GET'])
# def test_get():
#     # rank_give로 클라이언트가 준 rank을 가져오기
#     rank_receive = request.args.get('rank_give')
#
#     # rank_receive를 숫자로 만들어주기 (db엔 숫자로 저장되어있으니까!)
#     rank_receive = int(rank_receive)
#
#     # rank의 값이 받은 rank와 일치하는 document 찾기 & _id 값은 출력에서 제외하기
#     movie_info = db.movies.find_one({'rank':rank_receive},{'_id':0})
#
#     # info라는 키 값으로 영화정보 내려주기
#     return jsonify({'result':'success', 'info':movie_info})
#
#
# ## API 역할을 하는 부분
# @app.route('/test', methods=['POST'])
# def test_post():
#     # rank_give로 클라이언트가 준 rank을 가져오기 & 숫자변환
#     rank_receive = request.form['rank_give']
#     rank_receive = int(rank_receive)
#
#     # star_give로 클라이언트가 준 star를 가져오기 & 숫자변환
#     star_receive = request.form['star_give']
#     star_receive = float(star_receive)
#
#     # 해당 순위의 영화를 받은 score로 업데이트 해주기
#     db.movies.update_one({'rank': rank_receive}, {'$set': {'star': star_receive}})
#
#     # 다했으면 성공여부만 보냄
#     return jsonify({'result': 'success'})



@app.route('/new', methods=['POST'])
def new_post():
   rank_receive = int(request.form['rank_give'])
   star_receive = request.form['star_give']
   title_receive = request.form['title_give']

   db.movies.insert_one({'rank': rank_receive, 'star': star_receive, 'title':title_receive})

   return jsonify({'result': 'success'})
# jsonify는 파이썬의 딕셔너리를 Json Response로 바꿔주는 Flask 내장 함수



if __name__ == '__main__':
    # 아래 코드 의미는 파이썬이 해당 파일(server.py)을 실행시킬때
   app.run('0.0.0.0',port=5000,debug=True)