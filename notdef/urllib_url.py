#網路連線
import urllib.request as request
import json
src="https://data.ntpc.gov.tw/api/datasets/85BFCAA8-9932-4D06-A2EC-731171191883/json/preview"
with request.urlopen(src) as response:
  data=json.load(response)# 利用json模組找json資料
#print(data) #取得API 原始碼
with open("qoo.json",mode="w",encoding="utf-8") as file : #打開檔案
  for company in data:  #抓公司資料並寫入
    data = json.dump(company["Name"]+"\n",file)
  

  




