# pip3 install pymongo[srv]
# 載入 pymongo 套件
from bson import ObjectId
import pymongo
# 連線到 pymongo 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://user000:user000@cluster0.db3gf.mongodb.net/?retryWrites=true&w=majority")
# 把資料放進資料庫中
db = client.website_test # 選擇要操作 test 資料庫 (如果資料庫沒有則自動創建)
collection = db.users # 選擇操作 test / users (資料庫 / 集合) (如果資料庫沒有則自動創建)
# 篩選結果排序
cursor = collection.find(
  {"$or":[{"email":"lQQQ@gmail.com"},{"level":3}]},   # 滿足其一條件
  sort = [("level", pymongo.DESCENDING)] # 按照大到小 DESCENDING)   小到大 ASCENDING)
)
for doc in cursor:
  print(doc)
  
# 複合篩選條件
# data = collection.find_one(
#   {"$and":[{"email":"lQQQ@gmail.com"},{"level":3}]} # 滿足全部條件
#   
# )  
# print("取得的資料",data)
# 查詢、篩選集合中的文件資料
# data = collection.find_one(
#   {"email":"lQQQ@gmail.com"}
# )
# print("取得的資料的名字欄位",data["name"])  # 代表整理資料 要取得其中欄位就用dict方式去print就好。



# # 刪除集合中的一筆文件資料 ( 刪除資料室整筆刪除 並不是只有篩選的條件被刪除
# result = collection.delete_one(
#   {"email":"love233031@gmail.com"}
# )
# print("實際刪除的資料數量",result.deleted_count)
# # 刪除集合中的多筆文件資料 
# result = collection.delete_many(
#   {"level":1}
# )
# print("實際刪除的資料數量",result.deleted_count)

# 更新集合中的一筆文件資料(先篩選，再決定要改甚麼)
# result = collection.update_one(
#   {"email":"love233031@gmail.com"},
#   # {"$set":{"description":"hello.I am HOUHOU"}}
#   # {"$unset":{"description":""}} # $unset 清除欄位 須完整有 key 跟 value 
#   # {"$inc":{"level":5}}  # increase 增加/正數  減少/負數
#   # {"$mul":{"level":0.5}}  # multiply 乘/大於1  除/小於1
# )
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)

# 更新集合中的多筆文件資料(先篩選，再決定要改甚麼)
# result = collection.update_many(    
#   {"name":"侯侯"},
#   {"$set":{"name":"緯緯"}}
# )
# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)

# # 取得集合中的第一筆文件資料
# data = collection.find_one()
# print(data)

# # 根據 ObjectId 取得特定文件資料 #要載入 from bson import ObjectId
# data = collection.find_one(ObjectId("62ac13fbf07754f2ad3bec67"))
# print(data)

# # 取得文件資料中的欄位
# print(data["_id"])  # dict格式去搜尋
# print(data["email"])

# # 一次取得多筆文件資料
# cursor = collection.find()
# print(cursor)
# for doc in cursor :
#   print(doc["email"])

# 一次新增多筆資料，取得多筆資料的編號
# result = collection.insert_many([{
#   "name":"采采",
#   "gender":"女",
#   "email":"lQQQ@gmail.com",
#   "level":1
# },{
#   "name":"侯侯",
#   "gender":"男",
#   "email":"lQQQ@gmail.com",
#   "level":3
# }])
# print("資料新增成功!!")
# print(result.inserted_ids) # 新增多筆資料記得改 id"s"

# # # 把資料新增到集合中，取得新增資料的編號
# result = collection.insert_one({
#   "name":"采采",
#   "gender":"女",
#   "email":"lQQQ@gmail.com",
#   "level":1
# })
# print("資料新增成功!!")
# print(result.inserted_id)