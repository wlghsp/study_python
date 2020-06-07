import json, requests
import pandas as pd


url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=50ee936c7380f8675b6bb4de9a74212e&targetDt=20200501"
res = requests.get(url)   # 리퀘스트 모듈의 get함수를 사용하여 정보를 저장함
text = res.text         # 인간이 이해할 수 있는 문자로 변환을 위해 text함수를 이용함.
MD_json = json.loads(text) #MD = MOVIE DATA

#print(json.dumps(MD_json,indent=4,sort_keys=True))

# print(MD_json.keys())
# print(MD_json['boxOfficeResult'].keys())

movie = []

for i in MD_json['boxOfficeResult']['dailyBoxOfficeList']:
  movie.append([i['rank'],i['rankOldAndNew'],i['movieCd'],i['movieNm'],i['salesAmt']])
data = pd.DataFrame(movie)



