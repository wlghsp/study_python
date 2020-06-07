import json, requests
import pandas as pd


url2 = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/sales/json?page=1&perPage=500"
res = requests.get(url2)   # 리퀘스트 모듈의 get함수를 사용하여 정보를 저장함
text = res.text         # 인간이 이해할 수 있는 문자로 변환을 위해 text함수를 이용함.
corona19_mask = json.loads(text) #MD = MOVIE DATA




# print(json.dumps(corona19_mask,indent=4,sort_keys=True))
# print(corona19_mask.keys())

corona19_mask_list = []
for i in corona19_mask['sales']:
  corona19_mask_list.append([i['created_at'],i['code'],i['remain_stat']])
corona19_mask_dataframe = pd.DataFrame(corona19_mask_list)

print(corona19_mask_dataframe.head(10))