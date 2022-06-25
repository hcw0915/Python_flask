# def test(arg):
#   # print(arg)  # <function handle at 0x000001BBAF67ADD0> 
#   arg("Hello") # 呼叫回呼函式、帶入參數

# # 定義一個回呼函式
# def handle(da):
#   print(da)

# test(handle)

def add(n1,n2,cb):
  print(n1+n2)

def handle1(result):
  print("結果是",result)

def handle2(result):
  print("Result od add is",result)

add(3,4,handle1)
add(5,6,handle2)