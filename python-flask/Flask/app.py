from re import template
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import json
from flask import session


# 建立Application 物件，可以設定靜態檔案的路徑
app = Flask(
    __name__,
    static_folder="static",  # 靜態檔案的資料夾名稱(可更改)，但是實際放檔案的資料夾也要同步更改不然找不到
    static_url_path="/abc",  # 靜態檔案對應的路址路徑(可更改)→基本上就可以決定API的樣式
)  # 圖片網址 http://127.0.0.1:3000/abc/HOU.jpg
# 所有在(static)資料夾底下的檔案，都對應到網址路徑 /abc/ 檔案名稱(可設為 /static/ ，主要看url_path指定到哪裡)
app.secret_key = "antonio"    # 設定 Session密鑰
"""
問題 - folder裡面只可以有一個嗎? 要如何多設其他不同資料夾去拿不同檔案? 相對的路徑呢?
"""

#  使用GET方法，建立路徑 / 對應的處理函式


@app.route("/", methods=["GET"])  # 可不寫 預設就是 GET
def index():  # 用來回應路徑 / 的處理函式
    # -----------request 基本屬性  (m h u p s) (記憶點 mp hp us)
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)

    # -----------request 附加資訊(標頭 headers)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))
    """
    問題 -request.headers.get() 跟 a = request.get()  a.headers 差別在哪裡?
    """
    lang = request.headers.get("accept-language")
    print("語言偏好", request.headers.get("accept-language"))  # 從headers 去找使用者的語言偏好
    if lang.startswith("en"):  # 可以判斷進入網址的使用者語言偏好設定比重，去判斷進入後的語言偏好
        return json.dumps({       # 藉由json模組的json.dumps 把字典資料轉為json格式的字串 再return回去
            "status": "ok",
            "text": "Hello Flask",
        })  # 回傳網站首頁的內容
    else:
        return json.dumps({
            "status": "ok",
            "text": "你好，歡迎光臨",
        }, ensure_ascii=False)   # json.dumps({},ensure_ascii = )  表示不要用 ASCII 編碼處理中文


# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handledata():
    user = request.headers.get("accept-language")
    if user.startswith("en"):
        return redirect("/en/")    # 導向到路徑 /en/
    # return redirect("https://www.google.com/")  #也可以導向到一個網址
    elif user.startswith("zh"):
        return redirect("/zh/")


@app.route("/en/")
def handledata_en():
    return "english test"
# 如果 進入/data的時候，使用者偏好為英文(en) 則引導到 /en/ 頁面(def handledata_en)


@app.route("/zh/")
def handledata_zh():
    return "中文 測試"
# 如果 進入/data的時候，使用者偏好為中文(zh) 則引導到 /zh/ 頁面(def handledata_zh)


@app.route("/templates")
def rendertemplates():
    # 樣板檔案中的變數name 必須要用 {{ name }} 表示
    return render_template("index.txt", name="小明")

# 動態路由：建立路徑 /user/使用者名稱 對應的處理函式


@app.route("/user/<username>")
def handleuser(username):
    if username == "HOU":
        return "你好", username
    else:
        return "Hello", username


# 建立路徑 /getSum 對應的處理函式
# 利用要求字串(Query String)提供彈性  #/getSum?min=最小數字&max=最大數字&.......
@app.route("/getSum")
def getSum():  # min+(min+1).....+max
    maxNumber = request.args.get("max", 100)
    # ("參數名稱",預設值) 參數名稱就是 ?("max")= 這裡  沒預設值就掛 None
    maxNumber = int(maxNumber)  # 取得的資料一定是字串形式，要自己另外轉型
    # 前端網頁 /getSum?max=50 則 maxNumber = 50
    # 前端網頁 /getSum 沒有收到 ?max= 的指令 則 maxNumber = 預設值(100)
    minNumber = request.args.get("min", 1)  # 設定最小值
    minNumber = int(minNumber)
    # 前端網頁 /getSum?max=50 則 maxNumber = 50
    # 前端網頁 /getSum 沒有收到 ?min= 的指令 則 minNumber = 預設值(1)
    result = 0
    for n in range(minNumber, maxNumber+1):
        result += n
    return "結果:"+str(result)


@app.route("/show", methods=["POST"])
def show():
    # 接受GET方法的 Query String 用 request.args.get()
    # name = request.args.get("n", "")   # 這裡的 "n" 要跟表單裡的 name="n" 相同!!
    # 接受POST方法的 Query String 用 request.form["n"]
    name = request.form["n"]  # name = request.form.get("n") 也可以
    return "hello", name


@app.route("/html")
def html():
    return render_template("index.html")  # 後端互動用return_template 導到 index.html

# 使用 GET 方法處理路徑 /hello?name=使用者的名字


@app.route("/hello")
def hello():
    name = request.args.get("name", "")  # name預設是空白的
    session["username"] = name  # session["欄位名稱"]=資料
    return '你好，'+name

# 使用 GET 方法處理路徑 /talk


@app.route("/talk")
def talk():
    name = session["username"]  # 來自/hello 儲存的session的name裡面
    return name+",很高興認識你"


# 啟動網站伺服器，可透過port 參數指定埠號
app.run(port=3000)
