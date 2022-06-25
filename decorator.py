# # 定義裝飾器
# def myDeco(cb):
#   def run():
#     print("裝飾器中的程式碼")
#     cb(6)
#   return run
# # 使用裝飾器
# @myDeco
# def test(n):
#   print("普通函式的程式碼",n)
# test()

# 定義一個裝飾器，計算1~50
def calculate(callback):
  def run():
    # 裝飾器想要執行的程式碼
    result = 0 
    for n in range(51):
      result+=n
    # print(result)
    # 把計算結果透過參數傳到被裝飾的普通函式中
    callback(result)
  return run

# 使用裝飾器
@calculate
def show(n):
  print(n)

show()