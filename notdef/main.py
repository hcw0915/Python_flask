# import geometry.point as gp
# res = gp.distance(3,4)
# print(res)

# import geometry.line
# res = geometry.line.slope(1,1,3,3)
# print(res)

# 儲存檔案
# file = open("data.txt",mode="w",encoding="utf-8") # 開啟
# file.write("Hello File.\nSecond Line\n好棒棒") # 操作
# file.close() # 關閉
# with open("data.txt",mode="w",encoding="utf-8") as file:
#   file.write("5\n2")  #最佳實務
# # 讀取檔案
# # 把檔案中的數字資料
# sum = 0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#   for line in file:
#     sum += int(line)
# print(sum)    

# data = file.read()
# print(data)
# 使用
# import json

# with open("config.json",mode="r") as file:
#   res = json.load(file)
# #修改變數資料  
# res["name"]="New NAme"
# #把最新資料複寫回檔案
# with open("config.json",mode="w") as file:
#   json.dump(res,file) #dump 是Python的json寫入檔案的語法
# print("name",res["name"])
# print("verson",res["verson"])