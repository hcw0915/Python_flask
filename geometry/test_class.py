#定義類別、與類別屬性(封裝在類別中的變數與函式)
#定義一個類別IO，有兩個屬性supportedSrc 和 read
class IO:
  supportedSrcs=["console","file"]
  def read(src):
    if src not in IO.supportedSrcs: #不能純使用supportedSrcs 要包含class的定義類別去使用
      print("Not Support.")
    else:
      print("Read from",src)
#使用類別
data = IO.supportedSrcs
print(data)
IO.read("file")
IO.read("Internet")

