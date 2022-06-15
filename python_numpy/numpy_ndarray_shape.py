from isort import ImportKey
import numpy as np
from pandas import date_range
# 多維陣列維度/形狀操作
# 觀察資料形狀
# data=np.ones(10) #[1,1,1,1,1,1,1,1,1,1]
# print(data.shape) #(10,)一維陣列
# data=np.array([
#   [2,3,1],
#   [2,4,6]
# ])
# print(data.shape) #(2,3)

# 資料轉置
# data=np.array([
#   [2,3,1],
#   [1,5,7]
# ])
# print(data.shape) #(2,3)
# print(data.T) #(3,2) 欄轉列 列轉欄
# print(data.T.shape)

# 扁平化資料
# data=np.array([
#   [2,3,1],
#   [1,5,7]
# ])  # 2x3
# res = data.ravel()  #資料按順序變成1維資料
# print(res)
# print(res.shape) #一維資料

# 重塑資料形狀
# data=np.array([
#   [2,3,1,2],
#   [1,5,7,1],
#   [1,2,2,5]
# ])  # 3x4 = 12
# print(data.reshape(2,2,3))  #資料總數不變 2x2x3=3x4  

# data=np.zeros(18)
# print(data)
# data1=data.reshape(3,6)
# print(data1)
# data2=data.reshape(2,3,3)
# print(data2)

# data=np.arange(9).reshape(3,3) # 0~8的一維矩陣 重塑為(3,3)的二維矩陣
# print(data)
# print(data.T)
# print(np.outer(data,data.T))
# print(data@data.T)