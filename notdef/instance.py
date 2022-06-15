# # Point 實體物件的設計: 平面座標上的點
# class Point:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y
# # 建立第一個實體物件
# p1=Point(3,4)
# print(p1.x,p1.y)
# print(p1) #如果只有呼叫p1，他會給予p1這個物件的資料 <__main__.Point object at 0x000001956C5BC9D0>

# # 建立第二個實體物件
# p2=Point(5,6)
# print(p2.x,p2.y)

# # FullName 實體物件的設計: 分開紀錄姓、名資料的全名
# class FullName:
#   def  __init__(self,first,last):
#     self.first=first
#     self.last=last

# n1=FullName("Hou","Antonio")
# print(n1.first,n1.last)
# n2=FullName("Hou","Bob")
# print(n2.first,n2.last)

# Point 實體物件的是設計: 平面座標上的點
class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  # 實體定義方法
  def show(self,a,b):    
    print(self.x,self.y)
  def distance(self,targetX,targerY):
    data = (((self.x-targetX)**2)+((self.y-targerY)**2))**0.5
    return data
p=Point(3,4)
p.show()  #呼叫實體方法/函式
result = p.distance(0,0) #計算(3,4)到(0,0)的距離
print(result) # 因為 用 return 所以要print出來

# File 實體物件的設計:包裝檔案讀取的程式

# class File:
#   # 初始化函式
#   def  __init__(self,name):
#     self.name=name
#     self.file=None # 尚未開啟檔案: 初期為None
#   # 定義實體方法
#   def open(self): #方法1 開啟功能
#     self.file = open(self.name,mode="r",encoding="utf-8")
#   def read(self): #方法2 讀取功能
#     return self.file.read()
# #讀取第一個檔案
# f1=File("instance_data1.txt")
# f1.open()
# data = f1.read()
# print(data)  
# f2=File("instance_data2.txt")
# f2.open()
# data2=f2.read()
# print(data2)
      
      
      