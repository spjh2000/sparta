import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.jini

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('table.list-wrap > tbody > tr')

rank = 1
for music in musics:
    title = music.select_one('td.info > a.title')
    singer = music.select_one('td.info > a.artist')

    if rank is not None:
        title_1 = title.text
        singer_1 = singer.text

        print(rank, title_1, singer_1)
        rank += 1