from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

app = Flask(
  __name__,
  static_folder = "static",
  static_url_path = "/static",
  )
  
@app.route("/")
def index():
  #基本屬性-注意寫法(m h u p s) (記憶點 mp hp us)
  print(request.method) # print(request.headers.get("method")) 請求方法-method
  print(request.host)   # print(request.headers.get("host"))   主機名稱-host
  print(request.url)    # print(request.headers.get("url"))    完整網址-url
  print(request.path)   # print(request.headers.get("path"))   路徑-path
  print(request.scheme) # print(request.headers.get("scheme")) 通訊協定-scheme
  #標頭-跟基本屬性不同
  print(request.headers.get("user-agent"))
  print(request.headers.get("accept-language"))
  print(request.headers.get("referrer"))
  lang = request.headers.get("accept-language")
  if lang.startswith("zh"):
    return "你好"
  else:
    return "hello,world"

@app.route("/mydata")
def mydata():
  return "My data"

@app.route("/sum")
def sum():
  max = request.args.get("max",100)
  max = int(max)
  min = request.args.get("min",1)
  min = int(min)
  num = 0 
  for i in range(min,max):
    num += i
  return "結果:"+str(num)

@app.route("/redirect")
def re():
  return redirect("/sum")

@app.route("/redirect/render")
def render():
  return render_template("index.txt")







app.run(port=2500)

