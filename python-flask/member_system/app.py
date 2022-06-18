# 初始化 資料庫連線
from unittest import result
import pymongo
client = pymongo.MongoClient("mongodb+srv://user000:user000@cluster0.db3gf.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system
print("資料庫建立成功")

# 初始化 Flask 網站伺服器
from flask import *
app = Flask(
  __name__,
  static_folder = "public",
  static_url_path = "/"
)
app.secret_key = "any string but secret"
# 處理路由
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/member")
def member():
  return render_template("member.html")

# /error?msg=錯誤訊息
@app.route("/error")
def error():
  msg1 = request.args.get("msg","發生錯誤，請重新操作")
  return render_template("error.html",msg2 = msg1)

@app.route("/signup",methods=["POST"])
def signup():
  # 從前端接收資料
  nickname=request.form["nickname"]
  email=request.form["email"]
  password=request.form["password"]
  # 根據收到的資料，和資料庫互動
  collection = db.user
  # 檢查會員資料中是否有相同email的文件資料
  result = collection.find_one(
    {"email":email}
  )
  if result != None:
    return redirect("/error?msg=信箱已經被註冊")
  # 把資料放進資料庫，完成註冊
  collection.insert_one(
    {"nickname":nickname,
     "email":email,
     "password":password}
  )
  return redirect("/")
  

######################
app.run(port=3000)
